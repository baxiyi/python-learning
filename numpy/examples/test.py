import numpy as np 
# # 一维数组
# arr = np.array([1, 2, 3, 4])
# print(arr)
# print(arr.shape)

# zeorsArr = np.zeros((4, 5))
# onesArr = np.ones((1, 2))
# randomArr = np.random.rand((3))

# print(zeorsArr)
# print(onesArr)
# print(randomArr)

# # 二维数组
# arr1 = np.array([[1, 2], [3, 4]])
# print(arr1[0][0]) # 1
# print(arr1.shape) # (2, 2)
# # 切片
# print(arr1[: ,0]) # [1, 3]
# print(arr1[1, :]) # [3, 4]
# arr2 = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr2[1:3, :])
# # [[3 4]
# #  [5 6]]

# # # 数组运算
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# print(a + b)
# print(a + 1)
# print(a - b)
# print(a - 2)
# print(a * b) # *运算符执行的是点乘
# print(a * 2)
# print(a.dot(b)) # 矩阵乘需要用dot
# print(a / b)
# print(a / 2)
# print(a > b)
# print(a ** 2) # 平方

# # [[ 6  8]
# #  [10 12]]
# # [[2 3]
# #  [4 5]]
# # [[-4 -4]
# #  [-4 -4]]
# # [[-1  0]
# #  [ 1  2]]
# # [[ 5 12]
# #  [21 32]]
# # [[2 4]
# #  [6 8]]
# # [[19 22]
# #  [43 50]]
# # [[0.2        0.33333333]
# #  [0.42857143 0.5       ]]
# # [[0.5 1. ]
# #  [1.5 2. ]]
# # [[False False]
# #  [False False]]
# # [[ 1  4]
# #  [ 9 16]]

# dot运算
# a = np.array([1, 2, 3, 4])
# b = np.ones(4) * 2
# c = np.ones(3) * 2
# print(a.dot(b)) # 20
# print(a.dot(c))
# # ValueError: shapes (4,) and (3,) not aligned: 4 (dim 0) != 3 (dim 0)

# a = np.array([[1, 2, 1], [3, 4, 1]])
# b = np.array([2, 2])
# c = np.array([[1, 2], [3, 4]])
# print(b.dot(a)) # [8 12 4]
# print(b.dot(c)) # [8 12]
# print(c.dot(b)) # [6 14]
# print(a.dot(b)) # ValueError: shapes (2,3) and (2,) not aligned: 3 (dim 1) != 2 (dim 0)

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(a.dot(b))
# # [[ 9 12 15]
# #  [19 26 33]]
# c = np.array([[1, 2], [3, 4], [5, 6]])
# print(a.dot(c))
# print(a.dot(c))
# # ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

# # sum,min,max
# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a.sum())
# # 按列求和
# print(a.sum(axis=0))
# # 按行求和
# print(a.sum(axis=1))

# print(a.max())
# print(a.max(axis=0))
# print(a.max(axis=1))

# print(np.min(a, axis=0))
# print(a.cumsum()) # [ 1  3  6 10 15 21]

# cond = a >= 3
# print(a[cond]) # [3 4 5 6]

# # 广播
# a = np.array([[1, 2], [3, 4], [5, 6]])
# b = np.array([[1], [1], [1]])
# c = np.array([1, 1])
# print(a + b + c)

# # [[3 4]
# #  [5 6]
# #  [7 8]]

# # 创建数组的其它方式
# a = np.arange(12).reshape(3, 4)
# print(a)
# b = np.arange(0, 12, 3) # start,end,step
# print(b)
# indices = [0, 2]
# print(a[indices])
# # 对角线都是1的方阵
# c = np.eye(2, 2)
# print(c)
# # num个均匀间隔的数字
# c = np.linspace(0, 10, num=4)
# print(c)

# # reshape的作用将a从一维数组变成了二维数组
# a = np.array([1, 2, 3, 4])
# print(a)
# b = a.reshape(-1, 1)
# print(b)