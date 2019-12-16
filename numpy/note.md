# Numpy 

## dot运算

关于dot运算（这里指考虑对array的运算），有以下几种情况：

- 一维数组（行向量）与一维数组（行向量）之间进行dot运算

  这种情况下dot计算的是两个向量之间的内积。

  ```python
  a = np.array([1, 2, 3, 4])
  b = np.ones(4) * 2
  c = np.ones(3) * 2
  print(a.dot(b)) # 20
  # 当两个向量的维度不匹配时会报错
  print(a.dot(c))
  # ValueError: shapes (4,) and (3,) not aligned: 4 (dim 0) != 3 (dim 0)
  ```

- 二维数组（矩阵）与一维数组（行向量）之间进行dot运算

  这种情况下，一维数组会根据情况转化为列向量或者行向量，然后进行矩阵乘法。比如二维数组是m*n矩阵，一维数组是1\*n向量，则dot会自动将向量变为n\*1的列向量，计算得到m\*1的矩阵（向量）。如果无论是行向量还是列向量都不能满足矩阵乘法的条件，则会报错

  注意：只有向量会根据情况调整，矩阵不会自动调整为自己的转置

  ```python
  a = np.array([[1, 2, 1], [3, 4, 1]])
  b = np.array([2, 2])
  c = np.array([[1, 2], [3, 4]])
  print(b.dot(a)) # [8 12 4]
  print(b.dot(c)) # [8 12]
  print(c.dot(b)) # [6 14]
  # a是2*3矩阵，b是1*2向量，无论是行向量（1*2）还是列向量（2*1），都不能运算
  print(a.dot(b)) 
  # ValueError: shapes (2,3) and (2,) not aligned: 3 (dim 1) != 2 (dim 0)
  ```

- 二维数组（矩阵）与二维数组（矩阵）之间进行dot运算

  这种情况下两个矩阵直接进行矩阵乘法，如果不满足维度条件会报错

  ```python
  a = np.array([[1, 2], [3, 4]])
  b = np.array([[1, 2, 3], [4, 5, 6]])
  print(a.dot(b))
  # [[ 9 12 15]
  #  [19 26 33]]
  c = np.array([[1, 2], [3, 4], [5, 6]])
  print(a.dot(c))
  print(a.dot(c))
  # ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)
  
  ```

## 广播

**当操作两个array时，numpy会逐个比较它们的shape（构成的元组tuple），只有在下述情况下，两arrays才算兼容：**

1. 相等
2. 其中一个为1，（进而可进行拷贝拓展已至，shape匹配）

广播机制只适用于按位加和按位减，不适用于乘法

```python
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[1], [1], [1]])
c = np.array([1, 1])
print(a + b + c)

# [[3 4]
#  [5 6]
#  [7 8]]

```

a中每个元素都加了2，因为b，c跟a满足广播机制

