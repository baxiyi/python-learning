# # 高阶函数
# def add(a, b):
#   return a + b
# f = add
# print(f(1, 2)) # 3
# # map函数
# res = list(map(str, [1, 2, 3, 4]))
# print(res) # ['1', '2', '3', '4']
# # reduce函数
# from functools import reduce
# def func(a, b):
#   return a*10 + b
# res = reduce(func, [1, 3, 5, 7])
# print(res) # 1357
# # filter函数
# def odd(n):
#   return n % 2 != 0
# res = list(filter(odd, [1, 2, 3, 4, 5]))
# print(res)
# 使用filter生成所有素数
# def odd_iter():
#   n = 1
#   while True:
#     n = n + 2
#     yield n
# # lamda表达式定义了一个匿名函数
# def f(n):
#   return lambda x : x % n != 0
# def primes():
#   yield 2
#   it = odd_iter()
#   while True:
#     n = next(it)
#     yield n
#     it = filter(f(n), it)
# for num in primes():
#   if (num < 50):
#     print(num)
#   else:
#     break
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
# sorted函数
# res = sorted([-2, 1, 3, -5, 4], key=abs, reverse=True)
# print(res)
# [-5, 4, 3, -2, 1]

# 返回函数
# def lazy_sum(*args):
#   def sum():
#     res = 0
#     for i in args:
#       res += i
#     return res
#   return sum
# fn = lazy_sum(1, 2, 3, 4)
# res = fn()
# print(res) # 10 

def doubleEach(*args):
  fs = []
  for i in args:
    def f():
      return i*2
    fs.append(f)
  return fs
fs = doubleEach(1, 2, 3, 4)
print(fs)
for f in fs:
  print(f())
# 8
# 8
# 8
# 8

# 匿名函数
# res = list(map(lambda x: x*x, [1, 2, 3, 4]))
# print(res)
# # [1, 4, 9, 16]