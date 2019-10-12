# 高级特性笔记

## 1. 切片

slice（切片）方法可用于list，tuple，str对象，取出其中的部分元素

用法：

```python
s[i:j:k] # slice of s from i to j with step k
```

若取出元素的下标为x，则`x = i + n*k(n=0,1,2....) (i<=x<j)`，这里区间范围是[i,j)。

注意由于三个值都可以为负数，这里不一定是数学关系的i<j，如对于一个len为5的list arr来说，arr[0:-1]也是合法的，可以理解为i在j的位置之前。

三个值都可以省略，当k省略时，默认k=1；

k>0的时候，需保证i的位置在j之前，否则截取的是空，；k<0的时候，则需要保证i的位置在j之后；**规定k不能为0**。

当i和j省略的时候，需根据k的正负取默认值，当k>0，默认i = 0, j = len(s) ;当k<0时，默认i = - 1，j = -len(s) - 1。

```python
# s[i:j:k]： slice of s from i to j with step k (k!=0)
arr = [1, 2, 3, 4, 5]
print(arr[0:3]) # [1, 2, 3]
# 0可以省略
print(arr[:3]) # [1, 2, 3]
# 起始和结束位置都省略相当于对list做一个拷贝
print(arr[:]) # [1, 2, 3, 4, 5]
# slice也支持负数，代表倒数第几个元素
print(arr[-1:]) # [5]
print(arr[-4:3]) # [2, 3]
print(arr[-2:3]) # []

# 有k的情况
print(arr[::2]) # [1, 3, 5]
print(arr[::-2]) # [5, 3, 1]
print(arr[1:4:2]) # [2, 4]
print(arr[3:0:-2]) # [4, 2]
print(arr[-2:0:-2]) # [4, 2]
```

## 2. 迭代

迭代即通过for ... in ... 循环对一个可迭代对象进行遍历

如何判断一个对象是否是可迭代对象？

```python
from collections.abc import Iterable
print(isinstance([1, 2, 3], Iterable)) # True
print(isinstance('ABC', Iterable)) # True
print(isinstance(123, Iterable)) # False
```

tuple，list，str，dict，set都是可迭代对象

迭代dict默认是迭代key，如果想要迭代value或同时迭代key和value可以使用如下方式:

```python
d = {'a': 1, 'b': 2, 'c': 3}
# 迭代value
for value in d.values():
  print(value)
# 同时迭代key和value
for k, v in d.items():
  print('key:', k, ',', 'value:', v)
```

## 3. 列表生成式

基本结构是：生成结果 + for ... in ...循环(可以多层) + 条件判断（生成结果和条件判断中用到的变量需要在中间的for...in...循环中声明）

```python
arr = [1, 2, 3, 4]
# 生成平方数组
res = [x*x for x in arr]
print(res) # [1, 4, 9, 16]
# 生成列表内相乘的所有元素
res = [x*y for x in arr for y in arr] 
print(res)
# [1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12, 4, 8, 12, 16]
# 带条件判断
# 所有偶数乘2的列表
res = [x*2 for x in arr if x % 2 == 0]
print(res) # [4, 8]
# 一个for...in...中也可以有多个变量
d = {'a': 1, 'b': 2, 'c': 3}
res = [k + '=' + str(v) for k, v in d.items()]
print(res) # ['a=1', 'b=2', 'c=3']
```

## 4. 生成器

generator（生成器）可以一边循环一遍求值，即generator中保存的是方法而不是结果。

创建generator可以通过列表生成式或函数的方式。

#### 通过列表生成式创建generator：

只需要将列表生成式的[]换为()即可，返回的generator可以通过不断调用next()运行，更常用的方式是对generator进行for循环遍历

```python
arr = [1, 2, 3, 4]
g = (x*x for x in arr)
# next()调用
print(next(g)) # 1
print(next(g)) # 4
print(next(g)) # 9
print(next(g)) # 16
print(next(g)) # StopIteration错误

# 通过for进行遍历
for i in g:
  print(i) # 1 4 9 16
```

#### 通过函数生成generator：

当函数内部使用yield的时候，该函数就会生成一个generator

```python
# for循环遍历
def odd():
  print('step 1')
  yield 1
  print('step 2')
  yield 2
  print('step 3')
  yield 3
  print('done')
  return 4
g = odd()
for i in g:
  print(i)
# step 1
# 1
# step 2
# 2
# step 3
# 3
# done
```

通过上面for循环的方式无法获得reutrn的值4，要获得这个值需要捕获StopInteration错误，从e.value中才能获取

```python
def odd():
  print('step 1')
  yield 1
  print('step 2')
  yield 2
  print('step 3')
  yield 3
  print('done')
  return 4
g = odd()
while True:
  try:
    x = next(g)
    print(x)
  except StopIteration as e:
    print(e.value)
    break
# step 1
# 1
# step 2
# 2
# step 3
# 3
# done
# 4
```

## 4. 迭代器

可以通过for循环遍历的都是可迭代对象：Iterable

可迭代对象中可以通过next()函数调用的叫迭代器：Iterator

判断一个对象是否是Iterator：

```python
from collections.abc import Iterator
print(isinstance((x*x for x in [1, 2, 3]), Iterator)) # True
```

也可以将Iterable对象通过iter()函数转化为Iterator对象，并通过next()调用

实际上python的for循环的本质就是通过调用next()实现的

```python
arr = [1, 2, 3, 4]
g = iter(arr)
while True:
  try:
    i = next(g)
    print(i)
  except StopIteration:
    break
# 1
# 2
# 3
# 4
```

