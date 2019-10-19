# 面向对象高级编程

## 1. \_\_slot\_\_

一般情况下一个实例是可以随意添加实例属性的，如果想设置一个类只能添加某些实例属性，可以使用\_\_slot\_\_变量。给它赋值一个tuple，如果添加的属性不在tuple内会报错

```python
class Student:
  __slots__ = ('name', 'age')
st = Student()
st.name = 'mzw'
print(st.name) # mzw
st.age = 21
print(st.age) # 21
st.score = 100 # 'Student' object has no attribute 'score'
print(st.score)
```

## 2. @property

@property可以用来将一个方法变成属性，这个方法就成为了属性的get函数，同时也可以定义一个对应的setter方法，如果不定义setter方法那么属性就是只读的。

这种方式相比于直接设置属性的优势在于，可以在setter函数中对属性进行类型检查，同时也可以设置只读属性。

```python
class Student:
  def __init__(self):
    self._name = 'no name'
  @property
  def name(self):
    return self._name
  @name.setter
  def name(self, val):
    if not isinstance(val, str):
      print('name must be str type')
      return
    self._name = val
st = Student()
st.name = 1 # name must be str type
st.name = 'mzw'
print(st.name) # mzw
```

@property将函数name变成了name属性的get函数，同时也可通过@name.setter的方法设置它的set函数，并在里面进行了类型检查，这里注意get,set函数内部使用的是_name的定义，这种前面带\_的属性在python中是一种约定的写法，表示不能在外部直接访问的变量（但实际上并没有机制进行约束）。

如果不设置setter则为只读属性：

```python
class Student:
  def __init__(self):
    self._name = 'no name'
  @property
  def name(self):
    return self._name
st = Student()
st.name = 'mzw' # AttributeError: can't set attribute
```

## 3. 多重继承

python中允许多重继承（一个子类可以继承多个父类），因此允许mixIn的设计模式：即一个子类继承一个主要的父类，再通过继承其它类实现一些需要的功能。

比如Tigger主要继承Animal类，但它应该具有跑的能力，因此继承RunnaleMixIn类，它是食肉动物，因此继承CarnivorousMixIn类

```python
class Animal:
  pass
class RunnaleMixIn:
  pass
class CarnivorousMixIn:
  pass
class Tigger(Animal, RunnaleMixIn, CarnivorousMixIn):
  pass
```

## 4. 定制类

可以通过重写类内部形如\_\_xxx\_\_的方法来实现定制功能，下面是一些常见的

### \_\_str\_\_和\_\_repr\_\_

当通过print方法打印一个对象的时候，默认会调用\_\_str\_\_方法，所以可以通过重写它来改变输出内容。\_\_repr\_\_则是调试过程中显示该对象时调用的函数。

```python
class Student:
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return 'Student object (name: %s)' % self.name
  __repr__ = __str__
print(Student('mzw')) # Student object (name: mzw)
```

### \_\_iter\_\_和_\_next\_\_

可以通过重写\_\_iter\_\_和\_\_next\_\_将一个类变为迭代对象，并通过for...in...遍历

下面通过这种方法实现一个小于10000的斐波那契数列（打印小于100的）

```python
class Fib:
  def __init__(self):
    self.a, self.b = 0, 1
  def __iter__(self):
    return self
  def __next__(self):
    self.a, self.b = self.b, self.a + self.b
    if self.a > 10000:
      raise StopIteration()
    return self.a 

for n in Fib():
  if (n > 100):
    break
  print(n)
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
```

### \_\_getitem\_\_

上面的Fib类可以进行for...in...循环，但不能通过下标访问元素，如果要实现这种效果，可以重写\_\_getitem\_\_，在list中通过下标访问元素的时候就是默认调用这个方法。

```python
class FibList():
  def __getitem__(self, n):
    a, b = 1, 1
    for x in range(n):
      a, b = b, a + b
    return a
fib = FibList()
print(fib[0]) # 0
print(fib[5]) # 8
```

### \_\_getattr\_\_

可以改写\_\_getattr\_\_方法对不存在的属性进行出错处理，返回一个值

```python
class Student:
  def __getattr__(self, attr):
    if attr == 'score':
      return 0
st = Student()
print(st.score) # 0
st.score = 100
print(st.score) # 100
```

当score未设置的时候，会调用写好的\_\_getattr\_\_函数，返回0，但设置之后就不会再调用这个方法了

### \_\_call\_\_

写了这个方法之后，就可以将实例作为一个函数一样调用，比如：

```python
class Student:
  def __init__(self, name):
    self.name = name
  def __call__(self):
    print('My name is %s' % self.name)
st = Student('mzw')
st() # My name is mzw
```

从上面可以看出python中对象和函数实际上没有太大区别，区别只是能否调用，能否调用可以通过callable方法进行判断

```python
class Student:
  def __init__(self, name):
    self.name = name
  def __call__(self):
    print('My name is %s' % self.name)
class Test:
  pass
st = Student('mzw')
st() # My name is mzw
test = Test()
# 类的内部重写了__call__方法，所以可调用
print(callable(st)) # True
# 正常的类，未重写__call__，不可调用
print(callable(test)) # False
print(callable(abs)) # True
print(callable(int)) # True
print(callable(123)) # False
print(callable('123')) # False
print(callable([1, 2, 3])) # False
```

## 5. 枚举类

可以通过Enum类型定义枚举类，枚举类的每个成员都有一个value属性，根据定义时候的顺序从1开始递增。

```python
from enum import Enum

Day = Enum('Day', ('Mon', 'Tue', 'Wes', 'Thu', 'Fri', 'Sat', 'Sun'))
print(Day.Mon) # Day.Mon
print(Day.Tue.value) # 2
print(Day(2)) # Day.Tue
# 通过for循环列举所有值
for name, member in Day.__members__.items():
  print('name:', name, 'member:', member, 'value:', member.value)

# name: Mon member: Day.Mon value: 1
# name: Tue member: Day.Tue value: 2
# name: Wes member: Day.Wes value: 3
# name: Thu member: Day.Thu value: 4
# name: Fri member: Day.Fri value: 5
# name: Sat member: Day.Sat value: 6
# name: Sun member: Day.Sun value: 7
```

另外，还可以使用unique装饰器自定义不含重复值的枚举类

```python
from enum import Enum, unique
@unique
class WeekDay(Enum):
  # 可以自定义value
  Mon = 11
  Tue = 2
  Tue = 3
  Wes = 3
  Thu = 4
print(WeekDay.Mon) # TypeError: Attempted to reuse key: 'Tue'
```

如果键重复会报错，如果值重复也会报错

自定义的类型，也同样可以通过上面Enum类型的几种方式访问

```python
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
```

## 6. 元类（metclass）

metclass可以控制创建类的行为（如何创建一个类），可以理解为类为metclass创建出来的‘实例’，而真正的实例是类创建出来的实例。

一般用不到，等需要的时候再进行总结吧

