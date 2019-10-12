# 切片
# s[i:j:k]： slice of s from i to j with step k (k!=0)
# arr = [1, 2, 3, 4, 5]
# print(arr[0:3]) # [1, 2, 3]
# # 0可以省略
# print(arr[:3]) # [1, 2, 3]
# # 起始和结束位置都省略相当于对list做一个拷贝
# print(arr[:]) # [1, 2, 3, 4, 5]
# # slice也支持负数，代表倒数第几个元素
# print(arr[-1:]) # [5]
# print(arr[-4:3]) # [2, 3]
# print(arr[-2:3]) # []

# # 有k的情况
# print(arr[::2]) # [1, 3, 5]
# print(arr[::-2]) # [5, 3, 1]
# print(arr[1:4:2]) # [2, 4]
# print(arr[3:0:-2]) # [4, 2]
# print(arr[-2:0:-2]) # [4, 2]

# 迭代
# from collections.abc import Iterable
# print(isinstance([1, 2, 3], Iterable)) # True
# print(isinstance('ABC', Iterable)) # True
# print(isinstance(123, Iterable)) # False
# # 迭代dict
# d = {'a': 1, 'b': 2, 'c': 3}
# for value in d.values():
#   print(value)
# for k, v in d.items():
#   print('key:', k, ',', 'value:', v)

# 列表生成式
# arr = [1, 2, 3, 4]
# # 生成平方数组
# res = [x*x for x in arr]
# print(res) # [1, 4, 9, 16]
# # 生成列表内相乘的所有元素
# res = [x*y for x in arr for y in arr] 
# print(res)
# # [1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12, 4, 8, 12, 16]
# # 带条件判断
# # 所有偶数乘2的列表
# res = [x*2 for x in arr if x % 2 == 0]
# print(res) # [4, 8]
# # 一个for...in...中也可以有多个变量
# d = {'a': 1, 'b': 2, 'c': 3}
# res = [k + '=' + str(v) for k, v in d.items()]
# print(res) # ['a=1', 'b=2', 'c=3']

# 生成器generator
# 通过列表生成式生成generator：只需要把[]变为()即可
arr = [1, 2, 3, 4]
g = (x*x for x in arr)
print(next(g)) # 1
print(next(g)) # 4
print(next(g)) # 9
print(next(g)) # 16
print(next(g)) # StopIteration错误
# 通过for进行遍历
# for i in g:
#   print(i) # 1 4 9 16

# 通过函数生成generator
# def odd():
#   print('step 1')
#   yield 1
#   print('step 2')
#   yield 2
#   print('step 3')
#   yield 3
#   print('done')
#   return 4
# g = odd()
# # for i in g:
# #   print(i)
# # step 1
# # 1
# # step 2
# # 2
# # step 3
# # 3
# # done
# while True:
#   try:
#     x = next(g)
#     print(x)
#   except StopIteration as e:
#     print(e.value)
#     break
# # step 1
# # 1
# # step 2
# # 2
# # step 3
# # 3
# # done
# # 4

# # 判断Iterator
# from collections.abc import Iterator
# print(isinstance((x*x for x in [1, 2, 3]), Iterator)) # True
# # iter()函数
# arr = [1, 2, 3, 4]
# g = iter(arr)
# while True:
#   try:
#     i = next(g)
#     print(i)
#   except StopIteration:
#     break
# 1
# 2
# 3
# 4

