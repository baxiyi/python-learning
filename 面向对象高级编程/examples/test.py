# __slots__
# class Student:
#   __slots__ = ('name', 'age')
# st = Student()
# st.name = 'mzw'
# print(st.name) # mzw
# st.age = 21
# print(st.age) # 21
# st.score = 100 # 'Student' object has no attribute 'score'
# print(st.score)

# @property
# class Student:
#   def __init__(self):
#     self._name = 'no name'
#   @property
#   def name(self):
#     return self._name
#   # @name.setter
#   # def name(self, val):
#   #   if not isinstance(val, str):
#   #     print('name must be str type')
#   #     return
#   #   self._name = val
# st = Student()
# # st.name = 1 # name must be str type
# st.name = 'mzw' # AttributeError: can't set attribute
# print(st.name) # mzw

# # 多重继承
# class Animal:
#   pass
# class RunnaleMixIn:
#   pass
# class CarnivorousMixIn:
#   pass
# class Tigger(Animal, RunnaleMixIn, CarnivorousMixIn):
#   pass

# 定制类
# __str__
# class Student:
#   def __init__(self, name):
#     self.name = name
#   def __str__(self):
#     return 'Student object (name: %s)' % self.name
#   __repr__ = __str__
# print(Student('mzw')) # Student object (name: mzw)

# __iter__实现斐波那契数列
# class Fib:
#   def __init__(self):
#     self.a, self.b = 0, 1
#   def __iter__(self):
#     return self
#   def __next__(self):
#     self.a, self.b = self.b, self.a + self.b
#     if self.a > 10000:
#       raise StopIteration()
#     return self.a 

# for n in Fib():
#   if (n > 100):
#     break
#   print(n)
# # 1
# # 1
# # 2
# # 3
# # 5
# # 8
# # 13
# # 21
# # 34
# # 55
# # 89

# __getitem__
# class FibList():
#   def __getitem__(self, n):
#     a, b = 1, 1
#     for x in range(n):
#       a, b = b, a + b
#     return a
# fib = FibList()
# print(fib[0]) # 0
# print(fib[5]) # 8

# getattr
# class Student:
#   def __getattr__(self, attr):
#     if attr == 'score':
#       return 0
# st = Student()
# print(st.score)
# st.score = 100
# print(st.score)

# __call__
# class Student:
#   def __init__(self, name):
#     self.name = name
#   def __call__(self):
#     print('My name is %s' % self.name)
# class Test:
#   pass
# st = Student('mzw')
# st() # My name is mzw
# test = Test()
# print(callable(st)) # True
# print(callable(test)) # False
# print(callable(abs)) # True
# print(callable(int)) # True
# print(callable(123)) # False
# print(callable('123')) # False
# print(callable([1, 2, 3])) # False

# from enum import Enum

# Day = Enum('Day', ('Mon', 'Tue', 'Wes', 'Thu', 'Fri', 'Sat', 'Sun'))
# print(Day.Mon) # Day.Mon
# print(Day.Tue.value) # 2
# print(Day(2)) # Day.Tue
# for name, member in Day.__members__.items():
#   print('name:', name, 'member:', member, 'value:', member.value)

# # name: Mon member: Day.Mon value: 1
# # name: Tue member: Day.Tue value: 2
# # name: Wes member: Day.Wes value: 3
# # name: Thu member: Day.Thu value: 4
# # name: Fri member: Day.Fri value: 5
# # name: Sat member: Day.Sat value: 6
# # name: Sun member: Day.Sun value: 7

from enum import Enum, unique
@unique
class WeekDay(Enum):
  Mon = 1
  Tue = 2
  # Tue = 3
  Wes = 3
  Thu = 4
print(WeekDay.Mon) # WeekDay.Mon
print(WeekDay(1)) # WeekDay.Mon
print(WeekDay.Mon.value) # 1