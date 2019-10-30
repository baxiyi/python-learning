# fork使用（只适用于Unix内核）
import os
print('process %s start...' % os.getpid())
pid = os.fork()
if pid == 0:
  print('I am child process %s and my parent process is %s' % (os.getpid(), os.getppid()))
else:
  print('I am parent process %s and I created a child process %s' % (os.getpid(), pid))
