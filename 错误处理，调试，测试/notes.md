# 错误处理，调试，测试

## 1. 错误处理

### try...except...finally

将可能出错的代码块放在try中，在except中捕获错误，try和except执行完后会执行finally的内容

```python
try:
  print('try')
  r = 10 / 0
  print('result:', r)
except ZeroDivisionError as e:
  print('except', e)
finally:
  print('finally')
print('end')
# try
# except division by zero
# finally
# end
```

在try中除数为0，被except的ZeroDivisionError捕获，可以看到try中抛出异常后，第三行代码没有执行，最后执行了finally的代码

此外针对一个try还可以写多个except，还可以写用else语句处理没有异常的情况。

```python
try:
  print('try')
  r = 10 / int('a')
  print('result:', r)
except ZeroDivisionError as e:
  print('zero division error:',e)
except ValueError as e:
  print('value error:', e)
else:
  print('no error')
finally:
  print('finally')
print('end')
# try
# value error: invalid literal for int() with base 10: 'a'
# finally
# end
```

也可以在一个except中捕获多个异常，即：`except (ZeroDivisionError, ValueError) as e`

关于错误类型，实际上是一个类，所有错误类型都是继承`BaseException`，使用except语句时，会将该类和该类的子类(所有后代)都包括进去。

关于BaseException的继承树，可参考：https://docs.python.org/3/library/exceptions.html#exception-hierarchy

使用try...except...的时候，跨层调用的时候可以在调用外层捕获。

```python
def foo(s):
  return 10 / int(s)
def bar(s):
  return foo(s)*2
def main():
  try:
    bar('0')
  except Exception as e:
    print('Error', e)
  finally:
    print('finally')
main()
# Error division by zero
# finally
```



### 调用栈

![屏幕快照 2019-10-20 下午9.00.06](/Users/mazhiwei/Desktop/屏幕快照 2019-10-20 下午9.00.06.png)

如图，如果不进行任何的错误捕获，错误会一直根据调用栈向上进行捕获，最后被python解释器捕获，打印出调用栈的信息

### 记录错误

如果不捕获错误，也能通过调用栈信息知道错误出在哪，但是程序会在出错的地方终止运行，通过logging模块，可以将出错的堆栈信息打印出来，并继续向下执行程序

```python
import logging
def foo(s):
  return 10 / int(s)
def bar(s):
  return foo(s)*2
def main():
  try:
    bar('0')
  except Exception as e:
    logging.exception(e)
  finally:
    print('finally')
main()
# ERROR:root:division by zero
# Traceback (most recent call last):
#   File "test.py", line 61, in main
#     bar('0')
#   File "test.py", line 58, in bar
#     return foo(s)*2
#   File "test.py", line 56, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
# finally
```

logging也可以通过配置记录在相关文件中

### 抛出错误

可在代码中用raise主动抛出错误，并进行捕获

```python
def foo(s):
  n = int(s)
  if n == 0:
    raise ZeroDivisionError('invalid value %s' % s)
  return 10 / n
def main():
  try:
    foo('0')
  except Exception as e:
    print('except', e)
main()
# except invalid value 0
```

如果raise不加参数就代表将原错误再向上抛，这种方式经常会用到，很多时候一层函数可能只是记录一下错误，方便后续跟踪，它没有处理错误的能力，所以就要抛给上一层（就好像下级处理不了某个错误需要交给领导一样）

```python
def foo(s):
  n = int(s)
  if n == 0:
    raise ZeroDivisionError('invalid value %s' % s)
  return 10 / n
def bar(s):
  try:
    foo(s)
  except Exception as e:
    print('bar except', e)
    raise
def main():
  try:
    bar('0')
  except Exception as e:
    print('main except', e)
main()
# bar except invalid value 0
# main except invalid value 0
```

有必要的时候还可以根据情况将接受到的错误进行转化再抛出去

## 2. 调试

### print

最简单的方式是用print查看变量的信息，但这种方式显然emmm，比较low

### logging

上一部分中也用到了logging，logging可以将信息同时输出到console和记录文件中

logging有四个级别，从低到高为debug，info，warning，error

可以用`logging.basesicConfig(level=logging.INFO)`的方式进行配置，当设置为高一级别的时候，比它低的信息就不会显示

如：

```python
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.debug('n = %d' % n)
print(10 / n)
# Traceback (most recent call last):
#   File "test.py", line 117, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero
```

并没有显示`logging.debug()`的信息



```python
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
# INFO:root:n = 0
# Traceback (most recent call last):
#   File "/Users/mazhiwei/Desktop/python-learning/错误处理，调试，测试/examples/test.py", line 117, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero
```

level设为INFO之后，可用`logging.info`查看信息



如果要将logging输出到指定文件，也可以通过`logging.basicConfig`进行配置

需要注意的是，需要用`os.path.dirname(__file__)`获取当前路径，否则默认是绝对路径（网上有的可以设置相对路径，但是自己用的不行，为了统一性，最好都先用这种方式获取当前路径）

```python
logging.basicConfig(level=logging.INFO, 
  filename=os.path.dirname(__file__)+'/logs/test.log',format='[%(asctime)s-%(filename)s:-%(levelname)s:%(message)s]',
  filemode='a'
)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
```

这里通过filename属性设置输出到的文件，通过format设置输出的格式，通过filemode可设置写入模式，默认为a（追加模式），还可设置w为覆盖模式

运行后会发现console中没有了info的信息，而log文件中显示如下：

`[2019-10-20 22:59:34,343-test.py:-INFO:n = 0]`

### pdb

pdb是python的调试器，可在终端中通过`python -m pdb test.py`进入pdb调试器

用法如下：

代码：

```python
s = '0'
n = int(s)
print(10 / n)
```

终端：

```
bogon:examples mazhiwei$ python -m pdb test.py
> test.py(123)<module>()
-> s = '0'
(Pdb) l
123  ->	s = '0'
124  	n = int(s)
125  	print(10 / n)
[EOF]
(Pdb) n
> test.py(124)<module>()
-> n = int(s)
(Pdb) n
> test.py(125)<module>()
-> print(10 / n)
(Pdb) p n
0
(Pdb) n
ZeroDivisionError: division by zero
(Pdb) q
```

可通过`l`命令查看代码；通过`n`命令往下执行；通过 `p 变量名` 查看变量的值，通过`q`退出调试

但这样必须通过n命令一步一步运行，更好的方式是通过`pdb.set_trace()`在程序中设置断点

代码：

```python
import pdb
s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)
```

终端：

```
bogon:examples mazhiwei$ python test.py
> test.py(126)<module>()
-> print(10 / n)
(Pdb) p n
0
(Pdb) c
Traceback (most recent call last):
  File "test.py", line 126, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
```

通过正常方式运行py文件，程序会在断点处暂停，可通过`p 变量名` 查看变量的值；通过`c`命令继续执行程序

### IDE调试

使用IDE自带的调试器，如vscode，pycharm



