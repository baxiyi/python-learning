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

## 2.多线程

多线程是通过python的threading模块实现的，可使用threading的Thread类创建一个线程（指定target，也可以指定name，如果不指定，就默认Thread-1, Thread-2....），通过start开始线程，join等待线程结束。主线程的name为MainThread

```python
import time, threading
from threading import Thread
def loop():
  # 通过current_thread()获取当前线程
  tname = threading.current_thread().name
  print('thread %s is running...' % tname)
  n = 0
  while(n < 3):
    n = n + 1
    print('thread %s >>> %s' % (tname, n))
    time.sleep(1)
  print('thread %s end' % tname)
tname = threading.current_thread().name
print('thread %s is running...' % tname)
t = Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s end' % tname)

# 运行结果：
# thread MainThread is running...
# thread LoopThread is running...
# thread LoopThread >>> 1
# thread LoopThread >>> 2
# thread LoopThread >>> 3
# thread LoopThread end
# thread MainThread end
```

### Lock

当创建一个进程时，父进程的变量也会给子进程一份拷贝，各个进程之间的变量是互不影响的。而一个多线程则共享同一进程中的变量，这样就可能发生多个进程同时修改一个变量，导致变量出错。这是因为线程会在cpu调度下交替执行，这样可能会导致每个线程中的一个语句还没有执行完，就到了另一个线程执行，导致变量错乱。

解决的办法是使用Threading.Lock()，在线程执行中对修改共享变量的语句上锁。

```python
import time, threading
balance = 0
lock = threading.Lock()
def change(n):
  global balance
  balance = balance + n
  balance = balance - n

def run_thread(n):
  for i in range(100000):
    # 通过acquire()获取
    lock.acquire()
    change(n)
    # 改完之后通过release()释放
    lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# 0
```

### 多核

在python的多线程实际上是自带一个GIL锁的，每个线程在运行时得到这个锁，执行100条字节码会释放这个锁，交给别的线程去用，所以python的多线程本质上是在cpu上交替执行的，无法做到多核并行。

要利用多核，只能使用多进程。

代码如下：

```python
import threading, time, multiprocessing

def loop():
  x = 0
  while True:
    x = x + 1
# cpu_count()获取cpu核数
for i in range(multiprocessing.cpu_count()):
  p = multiprocessing.Process(target=loop)
  p.start()
```

每个进程都是死循环，执行上面的代码，查看cpu使用率，可以一段时间发现cpu每个核都被占满。

## 3. ThreadLocal

我们知道，各个线程可以共享一个进程中的变量，但也可以拥有自己的局部变量，并且这种局部变量在一个线程中独立，不用像共享变量那样修改时需要加锁。

但局部变量的缺点是，当线程中多个函数都需要用到这个变量的时候，每次都要在调用时将局部变量作为参数传进去。

像这样：

```python
def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去：
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)
```

如果有一种方法，可以将每个线程的局部变量都存在一个全局变量中，然后根据当前的线程ID从中获取相应的局部变量（类似一个dict），就不用在调用每个函数时传递局部变量了。

python中的ThreadLocal实现了这种功能，用法如下：

```python
import threading
# 获取ThreadLocal
local = threading.local()
def student_run():
  # 从ThreadLocal中获取线程对应的局部变量
  st = local.student
  print('student name %s in thread %s' % (st, threading.current_thread().name))
def thread_run(name):
  # 像ThreadLocal中添加线程对应的局部变量
  local.student = name
  student_run()
t1 = threading.Thread(target=thread_run, args=('Alice',), name='A')
t2 = threading.Thread(target=thread_run, args=('Bob',), name='B')
t1.start()
t2.start()
t1.join()
t2.join()

# 运行结果:
# student name Alice in thread A
# student name Bob in thread B
```

