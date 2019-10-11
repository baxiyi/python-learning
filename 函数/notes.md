# 	函数学习笔记

## 1. 类型转化函数

int(), float(), str(), bool()

```python
# 数据类型转化
print(int('abc')) # ValueError: invalid literal for int() with base 10: 'abc'
print(int('1243')) # 1243
print(int(12.43)) # 12
print(float('12.34')) # 12.34
print(str(1234)) # 1234

print(bool('')) # False
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(None)) # False
print(bool([])) # False
print(bool(())) # False
print(bool({})) # False
print(bool(set())) # False
```

## 2. 定义函数

### 定义形式

```python
# 可以传入默认参数b=0,:不能省略
def func(a, b = 0):
  return a + b

print(func(2)) # 2
print(func(2, 3)) # 5
```

此外python的返回值默认是None，不写return语句，等于`return None`或`return`

### pass语句

pass语句可以用来实现一个空函数，也可以用在if语句中

```python
def nop():
  pass
a = 1
if (a < 10):
  pass
```

### 参数检查

python的函数默认只有参数个数检查，没有参数类型检查，可使用内置的isinstance()函数进行类型检查

```python
def add(a, b):
  return a + b
add(1) # TypeError: add() missing 1 required positional argument: 'b'
# 函数参数不会判断类型，也不会做自动的类型转化
print(add('1', 2)) # TypeError: can only concatenate str (not "int") to str
def add2(a, b):
  if (not isinstance(a, (int, float)) or not isinstance(b, (int, float))):
    raise TypeError('bad type')
  return a + b
print(add2('1', 2)) # TypeError: bad type
```

### 返回多个值

python中可以在return语句中用逗号隔开返回多个值，即`return a, b`，实际上这是`return (a, b)`的简写，也就是python会将这些返回值放到一个tuple里面。

```python
def addAndMinus(a, b):
  return (a + b, a - b)
# 直接定义两个变量接收，是(sum, diff) = addAndMinus(4, 2)的简写
sum, diff = addAndMinus(4, 2)
print(sum, diff) # 6 2
print(addAndMinus(4, 2)) # (6, 2)
```

## 3. 函数参数

### 默认参数

⚠️默认参数必须为不可变对象，否则如果函数内部出现改变参数的操作会存储在参数中，使得下次调用函数的默认参数值发生改变

```python
# 默认参数为可变对象时
def func(arr = []):
  arr.append('end')
  return arr
print(func([1, 2, 3])) # [1, 2, 3, 'end']
print(func()) # ['end']
# 第二次调用默认参数已经变为为['end'],所以返回值为['end', 'end']
print(func()) # ['end', 'end']
```

### 可变参数

在传入参数时可以使用`*args`的形式接受不定个数的参数，在函数内部args会以一个tuple进行接收，传递的时候可以直接传入若干个参数，或者也以`*args`的方式传入（个人觉得类似于js中的...扩展运算符），可变参数不能设置默认值！

```python
def sum(*numbers):
  res = 0
  for num in numbers:
    res += num
  return res
res = sum(1, 2, 3, 4)
print(res) # 10
# 可变参数默认是一个空的tuple
res = sum()
print(res) # 0
# arr1和arr2分开传也可以，最后都被*numbers接收
arr1 = [1, 2]
arr2 = [3, 4]
res = sum(*arr1, *arr2)
print(res) # 10
```

### 关键字参数

传入参数时使用**args接收若干个key - value对，在函数内部组装成一个dict进行接收，传递的时候可以直接传入若干个`key = value`，或者也以\*\*args的形式传入

```python
def person(name, age, **others):
  print('name:', name, 'age:', age, 'others:', others)
# 两种传递值的方式
person('mzw', 21, gender = 'Male', major = 'software')
person('mzw', 21, **{'gender': 'Male', 'major': 'software'})
```

### 命名关键字参数

可限制传入关键字参数名字，使用时需用一个`*`参数将其和前面的参数隔开，`*`后面的参数才是命名关键字参数，此外命名关键字参数是可以设置默认值，不传递也不设置默认值会报错（使用`*`隔开指的是没有可变参数的情况下，如果有，直接在`*args`后面跟上命名关键字参数即可）

```python
def person(name, age, *, gender, address = 'Beijing'):
  print('name: ', name, 'age:', age, 'gender:', gender, 'address:', address)
person('mzw', 21, gender = 'Male') # name:  mzw age: 21 gender: Male address: Beijing
person('mzw', 21, **{'gender': 'Male', 'address': 'Dalian'}) # name:  mzw age: 21 gender: Male address: Dalian
```

### 组合使用

以上几种参数可以组合使用，在组合使用时，需要注意顺序必须是必选参数，默认参数，可变参数，命名关键字参数，（其它）关键字命名参数。需要注意这些参数尽量不要过多的组合，否则接口的理解性可能很差

```python
def person(name, age = 21, *address, gender, **others):
  print('name:', name, 'age:', age, 'address', address, 'gender:', gender, 'others', others)
person('mzw', *['Beijing', 'Dalian'], **{'gender': 'Male', 'job': 'software'})
# name: mzw age: Beijing address ('Dalian',) gender: Male others {'job': 'software'}
```

上面这个例子可以看到'Beijing'这个字符串被传到了age参数中，而没有使用默认值，这是因为实际上关键字参数之前的参数都是以一个tuple传入的，所以接收的时候前三个参数都在一个tuple里面，也就相当于下面这样：

```python
person(*['mzw', 'Beijing', 'Dalian'], **{'gender': 'Male', 'job': 'software'})
```

所以默认参数和可变参数是无法区分的，这种情况下必须给默认参数传值，才能保证后面传值正常

从这个例子也可以看出，实际任何一个函数的所有参数都可以用`func(*args1, **args2)`的形式传递参数

### 通过**args方式传值和直接传入一个dict对象的区别

通过**传值相当于将一个dict对象拆开，然后在函数内部再组成一个新的dict，也就是说相当于做了一个浅复制，如果在函数中对传入的dict参数做了修改，那么不会改变原本的dict对象，下面的例子说明了这一点：

```python
def func1(args):
  args['end'] = True
d1 = {'a': 1, 'b': 2}
func1(d1)
print(d1) # {'a': 1, 'b': 2, 'end': True}
def func2(**args):
  args['end'] = True
d2 = {'a': 1, 'b': 2}
func2(**d2)
print(d2) # {'a': 1, 'b': 2}
```

可以看见d1发生了改变，d2没有，但是如果对深层的数据进行修改，**args也顶不住！

```python
def func1(args):
  args['b']['c'] = 4
d1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
func1(d1)
print(d1) # {'a': 1, 'b': {'c': 4, 'd': 3}}
def func2(**args):
  args['b']['c'] = 4
d2 = {'a': 1, 'b': {'c': 2, 'd': 3}}
func2(**d2)
print(d2) # {'a': 1, 'b': {'c': 4, 'd': 3}}
```

可以看见d1,d2都发生了改变，所以做的只是一个浅复制

其实类比通过*args方式传值和直接传入一个tuple/list对象也是一样的，只是由于tuple是不可变对象，所以不存在在函数内部对其进行浅层修改的情况，也就没有讨论的意义了

### 4. 递归函数

Python没有尾递归优化

汉诺塔问题递归解决：

问题：大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着64片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。请编写`move(n, a, b, c)`函数，它接收参数`n`，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法。

示例：

```python
move(3, 'A', 'B', 'C')
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
```

解法：

**将n个盘子从A移动到C（借助B）**的问题，可以分成下面三个步骤：

1. 先把前n-1个盘子从A移动到B
2. 把第n个盘子从A移动到C
3. 把剩下的n-1个盘子从B移动到C

步骤一又可以看成是将n-1个盘子**从A移动到B（借助C）**的问题，同理步骤三可以看成是**将n-1个盘子从B移动到C（借助A）**的问题，这样就形成了递归

注意：在每个状态，都有一个需要源柱子，即需要移动盘子的柱子(参数a)，一个目标柱子（参数c），一个中间借助的柱子（参数b），所以这里的参数a，b，c不是固定的柱子，而是一直在变的，取决于需要处理的子问题是什么

每个函数的出口在最后源柱子只剩一个盘子的时候（盘子n），此时只需要直接将其移动到目标柱子上即可

代码如下：

```python
def move(n, a, b, c):
  if n == 1:
    print(a, '-->', c)
    return
  move(n - 1, a, c, b)
  print(a, '-->', c)
  move(n - 1, b, a, c)
```

