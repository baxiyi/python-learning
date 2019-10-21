# 文件读写
# import os
# f = open(os.path.dirname(__file__)+'/iotest.txt', 'r')
# print(f.read())
# f.close()
# # Hello world!
# # I am here for IO test

# import os
# with open(os.path.dirname(__file__)+'/iotest.txt', 'r') as f:
#   content = f.read()
#   print(type(content))
#   print(content)
# # Hello world!
# # I am here for IO test

# import os
# with open(os.path.dirname(__file__)+'/iotest.txt', 'r') as f:
#   content = f.read(5)
#   print(content)
#   lines = f.readlines()
#   print(lines)

# # Hello
# # [' world!\n', 'I am here for IO test']

# import os
# with open(os.path.dirname(__file__)+'/iotest2.txt', 'w') as f:
#   f.write('new Hello')
# with open(os.path.dirname(__file__)+'/iotest2.txt', 'r') as f:
#   print(f.read())
# # new Hello
# with open(os.path.dirname(__file__)+'/iotest2.txt', 'a') as f:
#   f.write('append text')
# with open(os.path.dirname(__file__)+'/iotest2.txt', 'r') as f:
#   print(f.read())
# # new Helloappend text

# import os
# with open(os.path.dirname(__file__)+'/iotest.txt', 'rb') as f:
#   print(f.read())

# # b'Hello world!\nI am here for IO test'

# StringIO
# from io import StringIO
# f = StringIO()
# f.write('hello')
# print(f.getvalue()) # hello
# f1 = StringIO('hello world')
# print(f1.read(2)) # he

# # 注意这里的写是在读过的数据之后追加
# f1.write('dddd')

# # 读取不到写入的dddd
# print(f1.read()) # world

# print(f1.getvalue()) # heddddworld

# 操作文件和目录
# import os
# # 查看绝对路径
# absPath = os.path.abspath('.')
# print(absPath) # /Users/mazhiwei/Desktop/python-learning/IO编程/examples
# # 通过join方法生成要创建的文件路径(最好不要用字符串+，因为不同操作系统可能不同)
# p = os.path.join(absPath, 'testdir')
# print(p) # /Users/mazhiwei/Desktop/python-learning/IO编程/examples/testdir
# # 传入路径创建文件夹
# os.mkdir(p)
# # 使用open方式创建文件（模式必须为w）
# open(os.path.join(p, 'test.txt'), 'w')
# # os.remove(os.path.join(p, 'test.txt'))
# # os.rmdir(p)


# l = os.path.join(p, 'test.txt')
# print(l) # /Users/mazhiwei/Desktop/python-learning/IO编程/examples/testdir/test.txt
# print(os.path.split(l)) 
# # ('/Users/mazhiwei/Desktop/python-learning/IO编程/examples/testdir', 'test.txt')
# print(os.path.splitext(l))
# # ('/Users/mazhiwei/Desktop/python-learning/IO编程/examples/testdir/test', '.txt')
# os.rename(l, os.path.join(p, 'rename.txt'))

# # 序列化
# import json, os
# d = dict(a=1, b=2)
# s = json.dumps(d)
# print(s) # {"a": 1, "b": 2}

# with open(os.path.join(os.path.dirname(__file__), 'jsons/test.json'), 'w') as f:
#   json.dump(d, f)

# # 反序列化
# import json, os
# d = json.loads('{"a": 1, "b": 2}')
# print(d)
# # {'a': 1, 'b': 2}
# with open(os.path.join(os.path.dirname(__file__), 'jsons/test.json'), 'r') as f:
#   d = json.load(f)
# print(d)
# # {'a': 1, 'b': 2}

class Student():
  def __init__(self, name, age):
    self.name = name
    self.age = age
def StudentToDict(st):
  return {'name': st.name, 'age': st.age}
def DictToStudent(d):
  return Student(d['name'], d['age'])

import json
st = Student('mzw', 21)
s = json.dumps(st, default=StudentToDict)
print(s)
# {"name": "mzw", "age": 21}

json_str = '{"name": "mzw", "age": 21}'
st = json.loads(json_str, object_hook=DictToStudent)
print(st)
# <__main__.Student object at 0x1047619d0>
print(st.name) # mzw
print(st.age) # 21

