# 数据类型转化
# print(int('abc')) # ValueError: invalid literal for int() with base 10: 'abc'
# print(int('1243')) # 1243
# print(int(12.43)) # 12
# print(float('12.34')) # 12.34
# print(str(1234)) # 1234
# print(bool('')) # False
# print(bool(0)) # False
# print(bool(0.0)) # False
# print(bool(None)) # False
# print(bool([])) # False
# print(bool(())) # False
# print(bool({})) # False
# print(bool(set())) # False

# 函数定义
# def func(a, b = 0):
#   return a + b
# print(func(2)) # 2
# print(func(2, 3)) # 5
# # pass语句
# def nop():
#   pass
# a = 1
# if (a < 10):
#   pass
# # 参数检查
# def add(a, b):
#   return a + b
# add(1) # TypeError: add() missing 1 required positional argument: 'b'
# 函数参数不会判断类型，也不会做自动的类型转化
# print(add('1', 2)) # TypeError: can only concatenate str (not "int") to str
# def add2(a, b):
#   if (not isinstance(a, (int, float)) or not isinstance(b, (int, float))):
#     raise TypeError('bad type')
#   return a + b
# print(add2('1', 2)) # TypeError: bad type
# def addAndMinus(a, b):
#   return (a + b, a - b)
# (sum, diff) = addAndMinus(4, 2)
# print(addAndMinus(4, 2)) # (6, 2)
# print(sum, diff) # 6 2

# 默认参数为可变对象时
# def func(arr = []):
#   arr.append('end')
#   return arr
# print(func([1, 2, 3])) # [1, 2, 3, 'end']
# print(func()) # ['end']
# print(func()) # ['end', 'end']

# 可变参数
# def sum(*numbers):
#   res = 0
#   for num in numbers:
#     res += num
#   return res
# res = sum(1, 2, 3, 4)
# print(res) # 10
# # 可变参数默认是一个空的tuple
# res = sum()
# print(res) # 10
# # arr1和arr2分开传也可以，最后都被*numbers接收
# arr1 = [1, 2]
# arr2 = [3, 4]
# res = sum(*arr1, *arr2)
# print(res) # 10

# 关键字参数
# def person(name, age, **others):
#   print('name:', name, 'age:', age, 'others:', others)
# # 两种传递值的方式
# person('mzw', 21, gender = 'Male', major = 'software')
# person('mzw', 21, **{'gender': 'Male', 'major': 'software'})

# 命名关键字参数:限制关键字参数的名字
# def person(name, age, *, gender, address = 'Beijing'):
#   print('name: ', name, 'age:', age, 'gender:', gender, 'address:', address)
# person('mzw', 21, gender = 'Male') # name:  mzw age: 21 gender: Male address: Beijing
# person('mzw', 21, **{'gender': 'Male', 'address': 'Dalian'}) # name:  mzw age: 21 gender: Male address: Dalian

# 组合使用
# def person(name, age = 21, *address, gender, **others):
#   print('name:', name, 'age:', age, 'address', address, 'gender:', gender, 'others', others)
# person('mzw', *['Beijing', 'Dalian'], **{'gender': 'Male', 'job': 'software'})
# # name: mzw age: Beijing address ('Dalian',) gender: Male others {'job': 'software'}
# person(*['mzw', 'Beijing', 'Dalian'], **{'gender': 'Male', 'job': 'software'})

# 通过**方式传入dict和直接传入一个dict对象的区别
# 浅层修改
# def func1(args):
#   args['end'] = True
# d1 = {'a': 1, 'b': 2}
# func1(d1)
# print(d1) # {'a': 1, 'b': 2, 'end': True}
# def func2(**args):
#   args['end'] = True
# d2 = {'a': 1, 'b': 2}
# func2(**d2)
# print(d2) # {'a': 1, 'b': 2}
# 深层修改
# def func1(args):
#   args['b']['c'] = 4
# d1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
# func1(d1)
# print(d1) # {'a': 1, 'b': {'c': 4, 'd': 3}}
# def func2(**args):
#   args['b']['c'] = 4
# d2 = {'a': 1, 'b': {'c': 2, 'd': 3}}
# func2(**d2)
# print(d2) # {'a': 1, 'b': {'c': 4, 'd': 3}}

# python没有尾递归优化，仍然会栈溢出
# def func(n, res):
#   if n == 1:
#     return res
#   return func(n - 1, n * res)
# a = func(1000, 1)
# print(a)