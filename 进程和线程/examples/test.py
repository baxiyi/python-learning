# fork使用（只适用于Unix内核）
# import os
# print('process %s start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#   print('I am child process %s and my parent process is %s' % (os.getpid(), os.getppid()))
# else:
#   print('I am parent process %s and I created a child process %s' % (os.getpid(), pid))

# # process 4484 start...
# # I am parent process 4484 and I created a child process 4485
# # I am child process 4485 and my parent process is 4484

# multiprocessing模块
# Process
# from multiprocessing import Process
# import os

# def run_proc(name):
#   print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__ == '__main__':
#   print('Parent process %s' % os.getpid())
#   p = Process(target=run_proc, args=('test',))
#   print('child process will start')
#   p.start()
#   p.join()
#   print('child process end')

# # parent process 4587
# # child process will start
# # Run child process test (4588)...
# # child process end

# Pool
# from multiprocessing import Pool
# import os, time, random
# def long_time_task(name):
#   print('Run task %s (%s)...' % (name, os.getpid()))
#   start = time.time()
#   time.sleep(random.random() * 3)
#   end = time.time()
#   print('Task %s runs %0.2f seconds' % (name, (end - start)))

# if __name__ == '__main__':
#   print('Parent process %s ' % os.getpid())
#   p = Pool(20)
#   for i in range(21):
#     p.apply_async(long_time_task, args=(i,))
#   print('waiting for all subprocesses done...')
#   p.close()
#   p.join()
#   print('All subprocess done')

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

# # 进程间通信

# from multiprocessing import Process, Queue
# import os, time, random
# def write(q):
#   print('Process to write %s' % os.getpid())
#   for value in ['A', 'B', 'C']:
#     print('Put %s to queue...' % value)
#     q.put(value)
#     time.sleep(random.random())

# def read(q):
#   print('Process to read %s ' % os.getpid())
#   while True:
#     value = q.get()
#     print('Get %s from queue...' % value)
# if __name__ == '__main__':
#   q = Queue()
#   pw = Process(target=write, args=(q,))
#   pr = Process(target=read, args=(q,))
#   pw.start()
#   pr.start()
#   pw.join()
#   pr.terminate()

# # Process to write 6126
# # Put A to queue...
# # Process to read 6127
# # Get A from queue...
# # Put B to queue...
# # Get B from queue...
# # Put C to queue...
# # Get C from queue...


# 多线程
# import time, threading
# from threading import Thread
# def loop():
#   tname = threading.current_thread().name
#   print('thread %s is running...' % tname)
#   n = 0
#   while(n < 3):
#     n = n + 1
#     print('thread %s >>> %s' % (tname, n))
#     time.sleep(1)
#   print('thread %s end' % tname)
# tname = threading.current_thread().name
# print('thread %s is running...' % tname)
# t = Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s end' % tname)

# # thread MainThread is running...
# # thread LoopThread is running...
# # thread LoopThread >>> 1
# # thread LoopThread >>> 2
# # thread LoopThread >>> 3
# # thread LoopThread end
# # thread MainThread end

# Lock
# import time, threading
# balance = 0
# lock = threading.Lock()
# def change(n):
#   global balance
#   balance = balance + n
#   balance = balance - n

# def run_thread(n):
#   for i in range(100000):
#     lock.acquire()
#     change(n)
#     lock.release()

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# # 0



# 多线程无法利用多核，而多进程可以
# import threading, time, multiprocessing

# def loop():
#   x = 0
#   while True:
#     x = x + 1
# for i in range(multiprocessing.cpu_count()):
#   p = multiprocessing.Process(target=loop)
#   p.start()

# ThreadLocal
import threading
local = threading.local()
def student_run():
  st = local.student
  print('student name %s in thread %s' % (st, threading.current_thread().name))
def thread_run(name):
  local.student = name
  student_run()
t1 = threading.Thread(target=thread_run, args=('Alice',), name='A')
t2 = threading.Thread(target=thread_run, args=('Bob',), name='B')
t1.start()
t2.start()
t1.join()
t2.join()

# student name Alice in thread A
# student name Bob in thread B

