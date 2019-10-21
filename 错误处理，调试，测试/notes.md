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

```python
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    bar('0')
main()
# Traceback (most recent call last):
#   File "test.py", line 26, in <module>
#     main()
#   File "test.py", line 25, in main
#     bar('0')
#   File "test.py", line 23, in bar
#     return foo(s)*2
#   File "test.py", line 21, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
```

如果不进行任何的错误捕获，错误会一直根据调用栈向上进行捕获，最后被python解释器捕获，打印出调用栈的信息

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

## 3. 单元测试

单元测试是对一个模块进行测试，对一个函数或类编写一个单元测试文件，将测试用例写在里面。

python中提供了unittest类用来进行单元测试，比如我们要编写一个Dict类，实现通过d.a这样的方式访问属性，当不存在的时候抛出AttributeError。

mydict.py

```python
class Dict(dict):
  def __init__(self, **kw):
    super().__init__(**kw)
  def __getattr__(self, key):
    try:
      return self[key]
    except KeyError:
      raise AttributeError('Dict object has no attribute %s' % key)
  def __setattr__(self, key, value):
    self[key] = value
```

mydict_test.py

```python
import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
  def test_init(self):
    d = Dict(a=1, b='test')
    self.assertEqual(d.a, 1)
    self.assertEqual(d.b, 'test')
    self.assertTrue(isinstance(d, dict))
  def test_key(self):
    d = Dict()
    d['key'] = 'value'
    self.assertEqual(d.key, 'value')
  def test_attr(self):
    d = Dict()
    d.key = 'value'
    self.assertTrue('key' in d)
    self.assertEqual(d['key'], 'value')
  def test_keyError(self):
    d = Dict()
    with self.assertRaises(KeyError):
      value = d['empty']
  def test_attrError(self):
    d = Dict()
    with self.assertRaises(AttributeError):
      value = td.empty
```

在test文件中以test开头的函数运行测试文件时会自动执行，常用到的方法有assertEqual，assertTrue，assertRaises等。

assertEqual设置两个参数，如果相等，则正常向下运行，不相等则会报对应的错误；assertTrue只接受一个bool参数；assertRaises配合with语句用来检测会不会抛出想要的错误。

要运行test文件，在终端中使用`python -m unittest mydict_test.py`

如果没有assert错误，会成功通过：

```
mazhiweideMacBook-Pro:单元测试 mazhiwei$ python -m unittest mydict_test.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

如果有会报错：

```
mazhiweideMacBook-Pro:单元测试 mazhiwei$ python -m unittest mydict_test.py
..F..
======================================================================
FAIL: test_init (mydict_test.TestDict)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mazhiwei/Desktop/python-learning/错误处理，调试，测试/examples/单元测试/mydict_test.py", line 7, in test_init
    self.assertEqual(d.a, 2)
AssertionError: 1 != 2

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

还可以在test类中定义setUp和tearDown函数，会分别在每个测试方法调用前后调用，如果想要在运行测试函数前后做什么工作（比如连接/断开数据库），可以放在这里。

```python
def setUp(self):
    print('setup...')
  def tearDown(self):
    print('teardown...')
```

终端：

```
mazhiweideMacBook-Pro:单元测试 mazhiwei$ python -m unittest mydict_test.py
setup...
teardown...
.setup...
teardown...
.setup...
teardown...
.setup...
teardown...
.setup...
teardown...
.
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

## 4. 文档测试

把一些交互环境下的测试代码直接放在源代码的注释当中，使用python的doctest模块可以自动提取其中的代码，并进行测试。

如我们刚才写的Dict改为文档测试的方法：

```python
class Dict(dict):
  '''
  Simple dict but also support access as x.y style.

  >>> d1 = Dict()
  >>> d1['x'] = 100
  >>> d1.x
  100
  >>> d1.y = 200
  >>> d1['y']
  200
  >>> d2 = Dict(a=1, b=2, c='3')
  >>> d2.c
  '3'
  >>> d2['empty']
  Traceback (most recent call last):
      ...
  KeyError: 'empty'
  >>> d2.empty
  Traceback (most recent call last):
      ...
  AttributeError: Dict object has no attribute empty
  '''
  def __init__(self, **kw):
    super().__init__(**kw)
  def __getattr__(self, key):
    try:
      return self[key]
    except KeyError:
      raise AttributeError('Dict object has no attribute %s' % key)
  def __setattr__(self, key, value):
    self[key] = value

if __name__ == '__main__':
  import doctest
  doctest.testmod()
```

可以用...代替中间的一些输出；最后需引入doctest模块，并调用testmod方法

终端：

```
mazhiweideMacBook-Pro:文档测试 mazhiwei$ python mydict.py
mazhiweideMacBook-Pro:文档测试 mazhiwei$
```

如果没有错误，什么都不会显示。

如果出错，比如我们把注释中d1.x改为50

```
mazhiweideMacBook-Pro:文档测试 mazhiwei$ python mydict.py
**********************************************************************
File "mydict.py", line 19, in __main__.Dict
Failed example:
    d2.empty
Expected:
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
Got:
    Traceback (most recent call last):
      File "mydict.py", line 28, in __getattr__
        return self[key]
    KeyError: 'empty'
    <BLANKLINE>
    During handling of the above exception, another exception occurred:
    <BLANKLINE>
    Traceback (most recent call last):
      File "/usr/local/Cellar/python/3.7.4_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/doctest.py", line 1329, in __run
        compileflags, 1), test.globs)
      File "<doctest __main__.Dict[8]>", line 1, in <module>
        d2.empty
      File "mydict.py", line 30, in __getattr__
        raise AttributeError('Dict object has no attribute %s' % key)
    AttributeError: Dict object has no attribute empty
**********************************************************************
1 items had failures:
   1 of   9 in __main__.Dict
***Test Failed*** 1 failures.
```

会报错，并分别给出expected和got的内容

