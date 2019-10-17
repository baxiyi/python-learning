# 面向对象编程

## 1. 类和实例

类是抽象的模版，而实例是具体的对象

创建类：

```python
class Student(object):
  pass
```

创建类的实例：

```python
st = Student()
# 可以单独给实例添加属性
st.number = 1
print(st.number) # 1
```

类可以通过定义`__init__`方法（构造函数）给一个类绑定初始的属性，第一个参数必须是self，指向对象本身，但调用的时候不需要传这个参数

```python
class Student(object):

  def __init__(self, name, score):
    self.name = name
    self.score = score

st = Student('mzw', 100)
print(st.name, st.score) # mzw 100
```

也可以在类的内部定义其它内部方法,，第一个参数也必须是self，但调用时不需要传

```python
class Student(object):

  def __init__(self, name, score):
    self.name = name
    self.score = score
  def printGrade(self, text):
    print(text + ':' + self.name + ',' + str(self.score))

st = Student('mzw', 100)
st.printGrade('my name and grade') # my name and grade:mzw,100
```

## 2. 访问限制

可以通过将变量设置为`__name`这样的形式将其变为类内部的私有变量，外部无法通过st._name的方式进行访问，这是因为python解释器将其变成了\_Student__name，实际上通过st.\_Student\_\_name仍然可以访问该变量，python内部并没有绝对的机制防止外部访问私有变量，一切全靠约定和自觉！

如果需要访问私有变量，可以添加相应的get和set方法

```python
class Student():
  
  def __init__(self, name, score):
    self.__name = name
    self.__score = score
  def getName(self):
    return self.__name
  def setName(self, newName):
    self.__name = newName

st = Student('mzw', 100)
print(st.__name) # AttributeError: 'Student' object has no attribute '__name'
print(st._Student__name) # mzw
st.setName('baxiyi')
print(st.getName()) # baxiyi
```

有一种错误写法需要注意：

```python
class Student():
  
  def __init__(self, name, score):
    self.__name = name
    self.__score = score
  def getName(self):
    return self.__name
  def setName(self, newName):
    self.__name = newName

st = Student('mzw', 100)
st.__name = 'zzz'
print(st.__name) # zzz
print(st.getName()) # mzw
```

这种方式实际上是给st实例单独定义了一个__name属性，因此可以通过st.\_\_name可以访问，但访问的并不是内部的\_\_name变量，通过getName方法发现，内部的\_\_name变量仍然是mzw

## 3. 继承和多态

通过`class A(B)`的方式可以让A继承B，A继承B之后也可以有自己的方法，可以重新定义B中重名的方法实现多态。

```python
class Animal:
  def run(self):
    print('Animal runnning')
class Dog(Animal):
  def run(self):
    print('Dog running')
class Cat(Animal):
  def run(self):
    print('Cat running')

animal = Animal()
animal.run() # Animal runnning
dog = Dog()
dog.run() # Dog running
cat = Cat()
cat.run() # Cat running
```

多态的好处在于如果A，C，D都继承B，那么它们都是B类型（可以通过isinstance方法判断），这样就可以用一个B类型代表它们，当B作为函数参数的时候，可以传入B，A，C，D几种类型，而调用共同的方法时则根据每个类具体实现的方法。

```python
# 子类均属于父类类型
print(isinstance(dog, Animal)) # True
print(isinstance(cat, Animal)) # True
# 多态的作用
def animalRun(animal):
  animal.run()
a = Animal()
b = Dog()
c = Cat()
animalRun(a) # Animal runnning
animalRun(b) # Dog running
animalRun(c) # Cat running
```

由于python是动态类型语言，实际上上面的animalRun可以接受任何一种数据类型，只要该类型中有run()方法，那么函数就可以被成功调用，这一点不同于C++或Java这样的静态语言，这一特点叫做动态语言的**鸭子类型**，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

```python
class Person:
  def run(self):
    print('person running')
person = Person()
animalRun(person) # person running
```

## 4. 获取对象信息

### 判断对象类型

- type()方法

  ```python
  # 基本数据类型
  print(type(123) == int) # True
  print(type('123') == str) # True
  # 引入types可判断function，lambda，generator等类型
  import types
  def fn():
    pass
  # 自定义的function
  print(type(fn) == types.FunctionType) # True
  # 内置的function
  print(type(abs) == types.FunctionType) # False
  print(type(abs) == types.BuiltinFunctionType) # True
  
  print(type(lambda  x: x*x) == types.LambdaType) # True
  print(type(x*x for x in range(0, 10)) == types.GeneratorType) # True
  ```

- isinstance方法

  参照上一节，可用来判断是否是某个类或是否继承于某个类，同时type能判断的isinstance都可以。

  isinstance还可以判断是不是多种类型中的一种

  ```python
  import types
  print(isinstance(lambda x: x*x, types.LambdaType))
  print(isinstance([1, 2, 3, 4], (list, tuple))) # True
  ```

### 获取内部属性和方法

##### dir()：获取一个对象所有属性和方法

```python
print(dir('123'))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

这里注意，以len()方法为例，`len('123')`等价于`'123'.__len__()`外部全局可以调用的方法，在内部都有一个对应的内置方法

##### hasattr(), setattr(), getattr()方法：用来判断是否有，设置，获取某个属性或方法

```python
class Test:
  def __init__(self):
    self.a = 1
  def testPrint(self):
    print('test')
test = Test()
print(hasattr(test, 'a')) # True
print(hasattr(test, 'testPrint')) # True
setattr(test, 'b', 2)
print(hasattr(test, 'b')) # True
b = getattr(test, 'b')
print(b)
# getattr的第三个参数可用来设置没有该属性时的返回值
c = getattr(test, 'c', 'no c')
print(c) # no c
```

## 5. 实例属性和类属性

之前我们提到的属性都是实例属性，实例属性可以通过self变量或类的实例直接添加，实例属性是每个实例自己的属性。

还有一种属性叫类属性（也就是其它语言中的静态属性），这种属性为所有实例共享。

```python
class Student:
  type = 'student'
st = Student()
st1 = Student()
print(st.type) # student
print(st1.type) # student
# 可通过类直接访问
print(Student.type) # student
# 如果实例属性和类属性名字相同，会在该实例上覆盖类属性
st.type = 'senior'
print(st.type) # senior
print(Student.type) # student
```

