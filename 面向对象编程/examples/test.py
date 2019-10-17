# 类和实例
# class Student(object):
#   pass

# st = Student()
# st.number = 1
# print(st.number) # 1
# class Student(object):

#   def __init__(self, name, score):
#     self.name = name
#     self.score = score

# st = Student('mzw', 100)
# print(st.name, st.score) # mzw 100
# class Student(object):

#   def __init__(self, name, score):
#     self.name = name
#     self.score = score
#   def printGrade(self, text):
#     print(text + ':' + self.name + ',' + str(self.score))

# st = Student('mzw', 100)
# st.printGrade('my name and grade') # my name and grade:mzw,100

# 私有变量
# class Student():
  
#   def __init__(self, name, score):
#     self.__name = name
#     self.__score = score
#   def getName(self):
#     return self.__name
#   def setName(self, newName):
#     self.__name = newName

# st = Student('mzw', 100)
# # print(st.__name) # AttributeError: 'Student' object has no attribute '__name'
# # print(st._Student__name) # mzw
# # st.setName('baxiyi')
# # print(st.getName()) # baxiyi

# st.__name = 'zzz'
# print(st.__name) # zzz
# print(st.getName()) # mzw

# 继承和多态
# class Animal:
#   def run(self):
#     print('Animal runnning')
# class Dog(Animal):
#   def run(self):
#     print('Dog running')
# class Cat(Animal):
#   def run(self):
#     print('Cat running')

# animal = Animal()
# animal.run() # Animal runnning
# dog = Dog()
# dog.run() # Dog running
# cat = Cat()
# cat.run() # Cat running

# print(isinstance(dog, Animal)) # True
# print(isinstance(cat, Animal)) # True

# def animalRun(animal):
#   animal.run()
# a = Animal()
# b = Dog()
# c = Cat()
# animalRun(a) # Animal runnning
# animalRun(b) # Dog running
# animalRun(c) # Cat running

# class Person:
#   def run(self):
#     print('person running')
# person = Person()
# animalRun(person) # person running

# 获取对象信息
# 类型判断
# 基本数据类型
# print(type(123) == int) # True
# print(type('123') == str) # True
# # 引入types可判断function，lambda，generator等类型
# import types
# def fn():
#   pass
# # 自定义的function
# print(type(fn) == types.FunctionType) # True
# # 内置的function
# print(type(abs) == types.FunctionType) # False
# print(type(abs) == types.BuiltinFunctionType) # True

# print(type(lambda  x: x*x) == types.LambdaType) # True
# print(type(x*x for x in range(0, 10)) == types.GeneratorType) # True
# import types
# print(isinstance(lambda x: x*x, types.LambdaType))
# print(isinstance([1, 2, 3, 4], (list, tuple))) # True

# 获取属性和方法  
# print(dir('123'))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# class Test:
#   def __init__(self):
#     self.a = 1
#   def testPrint(self):
#     print('test')
# test = Test()
# print(hasattr(test, 'a')) # True
# print(hasattr(test, 'testPrint')) # True
# setattr(test, 'b', 2)
# print(hasattr(test, 'b')) # True
# b = getattr(test, 'b')
# print(b)
# # getattr的第三个参数可用来设置没有该属性时的返回值
# c = getattr(test, 'c', 'no c')
# print(c) # no c

class Student:
  type = 'student'
st = Student()
st1 = Student()
print(st.type) # student
print(st1.type) # student
print(Student.type) # student
st.type = 'senior'
print(st.type) # senior
print(Student.type) # student