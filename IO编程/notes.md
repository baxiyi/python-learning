# IO编程

## 1. 文件读写

在python中所有的文件操作都是基于一个文件对象的，所以首先都要通过open函数打开文件得到一个文件对象，才能使用它的read或write方法。

在open的时候可以设置文件的模式，常见的是r（读），w（写），a（追加写），详细的可以参考：https://docs.python.org/3/library/functions.html#open

另外在结束文件操作的时候一定要调用close()关闭文件，否则文件会一直占用操作系统资源

### 读操作

调用read()函数会将全部文件内容转为一个str

```python
import os
f = open(os.path.dirname(__file__)+'/iotest.txt', 'r')
print(f.read())
f.close()
# Hello world!
# I am here for IO test
```

如果前面的IO操作有错误，就不会调用最后的close，所以这种写法存在一定风险，利用python的with语句更加简洁和安全。

```python
import os
with open(os.path.dirname(__file__)+'/iotest.txt', 'r') as f:
  print(f.read())
  
# Hello world!
# I am here for IO test
```

除了调用read()一次读取所有内容，还可以使用read(size)来限制一次读取的最大字节数，适用于数据量较大的情况，还可以使用readlines()获取每一行的内容，返回一个str数组

```python
import os
with open(os.path.dirname(__file__)+'/iotest.txt', 'r') as f:
  content = f.read(5)
  print(content)
  lines = f.readlines()
  print(lines)

# Hello
# [' world!\n', 'I am here for IO test']
```

### 写操作

和读操作一样，打开时可以是w（覆盖写）或a（追加写）

```python
import os
with open(os.path.dirname(__file__)+'/iotest2.txt', 'w') as f:
  f.write('new Hello')
with open(os.path.dirname(__file__)+'/iotest2.txt', 'r') as f:
  print(f.read())
# new Hello
with open(os.path.dirname(__file__)+'/iotest2.txt', 'a') as f:
  f.write('append text')
with open(os.path.dirname(__file__)+'/iotest2.txt', 'r') as f:
  print(f.read())
# new Helloappend text
```

### 二进制读写

在调用open函数的时候，模式中可以添加b模式，就可以用于二进制读写。

```python
import os
with open(os.path.dirname(__file__)+'/iotest.txt', 'rb') as f:
  print(f.read())

# b'Hello world!\nI am here for IO test'
```

## 2. StringIO和BytesIO

### file-like Object

像open函数这样返回的具有read()方法的对象，在python中都称为file-like Object。file-like Object只要求对象具有一个read()方法。

下面的StringIO和BytesIO就是在内存中创建的file-like Object，用来做临时缓冲。

### StringIO

可通过StringIO()创建一个对象，通过write()写入数据，通过getvalue()方法获取数据。

如果是初始化的时候就有数据，那么可以通过read(),read(size),readline()方法读取数据，**但是通过write方法写入的数据吗，只能用getvalue()方法获取**

```python
from io import StringIO
f = StringIO()
f.write('hello')
print(f.getvalue()) # hello
f1 = StringIO('hello world')
print(f1.read(2)) # he

# 注意这里的写是在读过的数据之后追加
f1.write('dddd')

# 读取不到写入的dddd
print(f1.read()) # world

print(f1.getvalue()) # heddddworld
```

### BytesIO

和StringIO用法完全一样，只是读写的是二进制数据。

## 3. 操作目录和文件

通过os.path模块可以获取当前绝对路径，生成创建的目录路径和文件路径，os.mkdir可用来创建目录，open(path, 'w')可用来创建文件

```python
import os
# 查看绝对路径
absPath = os.path.abspath('.')
print(absPath) # /Users/mazhiwei/Desktop/python-learning/IO编程/examples
# 通过join方法生成要创建的文件路径(最好不要用字符串+，因为不同操作系统可能不同)
p = os.path.join(absPath, 'testdir')
print(p) # /Users/mazhiwei/Desktop/python-learning/IO编程/examples/testdir
# 传入路径创建文件夹
os.mkdir(p)
# 使用open方式创建文件（模式必须为w）
open(os.path.join(p, 'test.txt'), 'w')
```

要删除文件或目录，可用os.remove删除文件，使用rmdir删除目录

```python
# 删除文件
os.remove(os.path.join(p, 'test.txt'))
# 删除目录
os.rmdir(p)
```

要合并路径应使用os.path.join()，要拆分路径则需使用os.path.split()函数，如果要获取文件扩展名可使用os.path.splitext()函数

```python
print(l) # /Users/mazhiwei/Desktop/python-learning/IO编程/examples/testdir/test.txt
print(os.path.split(l)) 
# ('/Users/mazhiwei/Desktop/python-learning/IO编程/examples/testdir', 'test.txt')
print(os.path.splitext(l))
# ('/Users/mazhiwei/Desktop/python-learning/IO编程/examples/testdir/test', '.txt')
```

重命名文件可使用os.rename()函数

```python
os.rename(l, os.path.join(p, 'rename.txt'))
```

## 4. 序列化与反序列化

把变量从内存中变成可存储或传输的过程称之为序列化，把变量内容从序列化的对象重新读到内存里称之为反序列化。

为了方便与其它语言进行数据传输，我们一般都使用json进行序列化，python中也提供了json模块。

json其实就是js的对象，{}对应的就是python中的dict，[]对应list

要将一个dict序列化为json，可以用json.dumps()或json.dump()，前者将dict转化为json的字符串，后者可以将josn存储到一个file-like Object中

```python
# 序列化
import json, os
d = dict(a=1, b=2)
s = json.dumps(d)
print(s) # {"a": 1, "b": 2}

with open(os.path.join(os.path.dirname(__file__), 'jsons/test.json'), 'w') as f:
  json.dump(d, f)
# 运行后json文件中确实写入了数据
```

类似的，反序列化可用json.loads()和json.load()实现。

```python
import json, os
d = json.loads('{"a": 1, "b": 2}')
print(d)
# {'a': 1, 'b': 2}
with open(os.path.join(os.path.dirname(__file__), 'jsons/test.json'), 'r') as f:
  d = json.load(f)
print(d)
# {'a': 1, 'b': 2}
```



如果要实现python对象转化为json，需要在dumps, dump的default参数传入python对象转化为dict的函数。

同样，实现json转化为python对象，需在loads和load函数中的object_hook参数传入dict转化为python对象的函数。

比如对于一个Student对象：

```python
class Student():
  def __init__(self, name, age):
    self.name = name
    self.age = age
def StudentToDict(st):
  return {'name': st.name, 'age': st.age}
def DictToStudent(d):
  return Student(d['name'], d['age'])

# 序列化
import json
st = Student('mzw', 21)
s = json.dumps(st, default=StudentToDict)
print(s)
# {"name": "mzw", "age": 21}

# 反序列化
json_str = '{"name": "mzw", "age": 21}'
st = json.loads(json_str, object_hook=DictToStudent)
print(st)
# <__main__.Student object at 0x1047619d0>
print(st.name) # mzw
print(st.age) # 21
```

