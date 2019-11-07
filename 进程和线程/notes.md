# 多进程和多线程

## 1. 多进程

### fork()函数

python的os模块中封装了fork函数，可用来创建子进程，fork函数一次调用，返回两次，在父进程中返回子进程的ID，在子进程中返回0。

在子进程中如果想知道父进程的ID，可使用getppid()方法

```python
import os
print('process %s start...' % os.getpid())
pid = os.fork()
if pid == 0:
  print('I am child process %s and my parent process is %s' % (os.getpid(), os.getppid()))
else:
  print('I am parent process %s and I created a child process %s' % (os.getpid(), pid))
  
# 运行结果:
# process 4484 start...
# I am parent process 4484 and I created a child process 4485
# I am child process 4485 and my parent process is 4484
```

fork函数只在Unix/Linux系统上有，windows系统上上述代码无法运行

### multiprocessing模块

python在multiprocessing模块中提供了Process类支持各个平台创建进程。

```python
from multiprocessing import Process
import os

def run_proc(name):
  print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
  print('Parent process %s' % os.getpid())
  # target传入执行函数，args传入参数
  p = Process(target=run_proc, args=('test',))
  print('child process will start')
  # start用来启动进程
  p.start()
  # join方法等待子进程运行结束，用于进程间同步
  p.join()
  print('child process end')
  
# 运行结果:
# parent process 4587
# child process will start
# Run child process test (4588)...
# child process end
```

multiprocess模块中还有Pool类，可以批量创建多个进程

```python
from multiprocessing import Pool
import os, time, random
def long_time_task(name):
  print('Run task %s (%s)...' % (name, os.getpid()))
  start = time.time()
  time.sleep(random.random() * 3)
  end = time.time()
  print('Task %s runs %0.2f seconds' % (name, (end - start)))

if __name__ == '__main__':
  print('Parent process %s ' % os.getpid())
  p = Pool(5)
  for i in range(6):
    p.apply_async(long_time_task, args=(i,))
  print('waiting for all subprocesses done...')
  p.close()
  p.join()
  print('All subprocess done')

# 运行结果：
# Parent process 5356
# waiting for all subprocesses done...
# Run task 0 (5357)...
# Run task 1 (5358)...
# Run task 2 (5359)...
# Run task 3 (5360)...
# Run task 4 (5361)...
# Task 1 runs 1.26 seconds
# Run task 5 (5358)...
# Task 5 runs 0.13 seconds
# Task 0 runs 1.87 seconds
# Task 4 runs 2.18 seconds
# Task 3 runs 2.24 seconds
# Task 2 runs 2.24 seconds
# All subprocess done
```

可以看到，由于创建Pool的时候传入了参数5，所以程序最多同时执行5个进程，当Task1结束后才开始执行Task5。

如果创建Pool时不传入参数，则默认值取决于CPU的核数

### 进程间通信

进程间通信可通过Queue或Pipes实现

下面代码以Queue为例子，创建一个Queue，通过put方法向Queue中写数据，get方法从Queue中拿数据。

```python
from multiprocessing import Process, Queue
import os, time, random
def write(q):
  print('Process to write %s' % os.getpid())
  for value in ['A', 'B', 'C']:
    print('Put %s to queue...' % value)
    q.put(value)
    time.sleep(random.random())

def read(q):
  print('Process to read %s ' % os.getpid())
  while True:
    value = q.get()
    print('Get %s from queue...' % value)
if __name__ == '__main__':
  q = Queue()
  pw = Process(target=write, args=(q,))
  pr = Process(target=read, args=(q,))
  pw.start()
  pr.start()
  pw.join()
  # pr中是死循环，只能强行终止
  pr.terminate()

# 运行结果：
# Process to write 6126
# Put A to queue...
# Process to read 6127
# Get A from queue...
# Put B to queue...
# Get B from queue...
# Put C to queue...
# Get C from queue...
```

Queue模块详解见：https://linuxeye.com/334.html（在q.put()的解释中有一处错误：如果队列当前为满（不是空）且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常。）

