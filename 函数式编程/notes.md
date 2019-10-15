# 函数式编程

## 1. 高阶函数

在python中，函数名本身就是变量，将其赋值给其它变量后也可以调用

```python
def add(a, b):
  return a + b
f = add
print(f(1, 2)) # 3
```

因此函数A也可以作为参数传给另一个函数B，这样的函数B就叫做高阶函数

下面是python中内置的几种高阶函数：

### map/reduce

map接收两个参数，第一个是函数f，第二个是一个Iterable对象，返回一个Iterator对象。其效果是将Iterable中的每一个元素都进行函数f的变换，再放到一个Iterator中。

```python
# map实现将一个list中的整形转化为str类型
res = list(map(str, [1, 2, 3, 4]))
print(res) # ['1', '2', '3', '4']
```

注意由于返回值是Iterator，需要用list再进行一下转化

reduce函数同样接收一个函数f和一个Iterable对象，最后返回一个结果。但是函数f必须有两个参数，reduce会把f的结果不断和下一个元素累积。

即：`reduce(f, [x1, x2, x3, x4, x5]) = f(f(f(f(x1, x2), x3), x4), x5)`

```python
# 使用reduce实现将[1, 3, 5, 7]转化为整形1357
from functools import reduce # 使用reduce需要先从functools中引入
def func(a, b):
  return a*10 + b
res = reduce(func, [1, 3, 5, 7])
print(res) # 1357
```

### filter

filter函数接收两个参数，函数f和Iterable对象，返回一个Iterator对象，但和map不同的是，filter中的返回值是一个bool型，根据这个bool值进行筛选，为True最后放到结果中。

```python
# 筛选奇数
def odd(n):
  return n % 2 != 0
res = list(filter(odd, [1, 2, 3, 4, 5]))
print(res) # [1, 3, 5]
```

使用filter可以实现一个无限的素数生成器，基本原理是，先产生一个3开始的奇数生成器（素数不可能是偶数），然后每次取出第一个元素n，对序列中每个元素进行筛选，留下那些不能被n整除的，由于所有步骤使用的都是generator惰性求值，所以可以构造出一个无限的素数序列。

```python
# 打印50以内所有素数
def odd_iter():
  n = 1
  while True:
    n = n + 2
    yield n
# lamda表达式定义了一个匿名函数
def f(n):
  return lambda x : x % n != 0
def primes():
  yield 2
  it = odd_iter()
  while True:
    n = next(it)
    yield n
    it = filter(f(n), it)
for num in primes():
  if (num < 50):
    print(num)
  else:
    break
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
```

### sorted

排序函数，默认从小到大排序，可接收三个参数，第一个是排序的序列（一个Iterable对象），第二个参数（可省）是key = fn，表示每个元素使用fn转化后的key进行排序，第三个参数（可省）是reverse = True/Flase用来指定是否逆序，默认为False，返回一个排序后的Iterable

```python
# 按绝对值倒序排序
res = sorted([-2, 1, 3, -5, 4], key=abs, reverse=True)
print(res)
# [-5, 4, 3, -2, 1]
```

## 2. 闭包

函数A可以作为另一个函数B的返回值，返回后函数A不会立即执行，而是等到调用它的时候才执行，如果函数B中引用了函数A的参数或局部变量，则函数B再返回A之后局部变量不会释放，因为A还在引用，这种程序结构叫做闭包（可类比js的闭包）

```python
# 惰性求和函数
def lazy_sum(*args):
  def sum():
    res = 0
    for i in args:
      res += i
    return res
  return sum
fn = lazy_sum(1, 2, 3, 4)
res = fn()
print(res) # 10 
```

返回的函数A不是立即执行，所以需要注意A中不能引用B中的循环变量可能出现意外的结果，因为这样当A执行的时候B中循环已经结束，B中的循环变量已经是循环结束后的值。

举个例子：

```python
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
```

所以返回闭包时需要注意：返回函数中不要引用循环变量或后续会发生变化的变量

## 3. 匿名函数

匿名函数可以用一个lambda表达式来表示，但缺点是匿名函数只能是一个表达式。

```python
lambda x : x*x
等价于
def f(x)
	return x*x
```

（可类比js中箭头函数）

用法：

```python
res = list(map(lambda x: x*x, [1, 2, 3, 4]))
print(res)
# [1, 4, 9, 16]
```

## 4. 装饰器

当我们要增强一个函数的功能但又不希望改变原有函数的定义，而是在调用它的时候动态的添加某个功能，就可以使用装饰器（decorator）

```python
def log(func):
  def wrapper(*args, **kw):
    print('call', func.__name__)
    return func(*args, **kw)
  return wrapper
@log
def now():
  print('2019-10-15')
now()
# call now
# 2019-10-15
```

此处的`@log`相当于调用了`now = log(now)`

但是这里会出现一个问题，如果此时打印出`now.__name__`，会发现是`wrapper`

```python
import functools
def log(func):
  @functools.wraps(func)
  def wrapper(*args, **kw):
    print('call', func.__name__)
    return func(*args, **kw)
  return wrapper
@log
def now():
  print('2019-10-15')
now()
print(now.__name__)
# call now
# 2019-10-15
# now
```



## 5. 偏函数

偏函数就是将一个函数的某些参数设置一个默认值，然后返回一个新的函数

用法：

`functools.partial(func, *args, **kw)` 前面讲过所有函数的参数都可以写成`(*args, **kw)`的形式，在创建偏函数的时候也是如此。

```python
import functools
# 将max函数传入10再返回一个函数：参数10传入*args中
min10Max = functools.partial(max, 10)
print(min10Max(5, 6, 7)) # 10
# 将int函数固定成按二进制转化:base传入**kw中
int2 = functools.partial(int, base=2)
print(int2('1001')) # 9
```