# python基础学习笔记

## 1. 数据类型及变量

### 数据类型

- 整数：没有大小限制 ？
- 浮点数：没有大小限制，但超过一定范围表示为inf
- 字符串：' '或者""扩起来的内容
- 布尔值：有True和Flase两种取值，有and（与），or（或），not（非）三种运算
- 空值：用None表示
### 变量
python是动态语言，同一个变量可以赋值成不同的数据类型，python中没有常量？
### python的除法运算符
python中有两种除法，第一种是 /，运算结果为浮点数

```python
>>> 10 / 3
3.3333333333333335
```

第二种是// ，称为地板除，也就是取整除法

```python
>>> 10 // 3
3
```

需要注意的是使用 // 的时候，如果出现浮点数，也会对浮点数进行取整

```python
>>> 4.5 // 3
1.0
```

## 2. 字符串和编码

### 编码方式

- ASCII：使用一个字节（8位）编码，ASCII码表只有127个字符（只用了7位，最高位都是0），只能用来编码英文字符，中文或其他国家语言就会出现乱码。

- Unicode：将所有的语言统一到了一套编码，一般都使用2个字节进行编码，一些偏僻的字符可能会用4个字符。但这种编码方式的缺陷在于 1. 无论是英文字符还是中文字符都使用2个字节进行编码，但实际上英文字符只需要一个字节（ASCII），前面的8位都只能置0，这就造成了存储和传输时候空间的浪费。2. 无法区分一个字节编码和两个字节编码，计算机识别时不知道这是一个两字节编码的字符还是两个一字节编码的字符。因此产生了UTF-8。

- UTF-8：确切地说，是Unicode的一种实现方式，它根据一个Unicode字符的数字大小的不同编码成1 - 6个字节，一般英文字符会编码成一个字节，汉字会编码成3个字符，Unicode和UTF-8的具体转化规则如下：

  ![preview](https://pic3.zhimg.com/cd6c79db0291464c193de1b532ae890c_r.jpg)

  可以看到UTF-8也通过前几位的区别（0，110，1110，11110）告诉计算机该字符采用的是几个字节编码的形式，也就解决了Unicode上面的两个问题。

一般来讲，在计算机内存中统一使用Unicode编码，当需要保存到硬盘或传输时，就转化成UTF-8编码

### Python的字符串编码

Python3统一使用Unicode编码，并提供了编码和解码的相应函数

对于单个字符的编码，Python提供了`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符：

```python
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
>>> '\u4e2d\u6587' #直接通过Unicdoe形式也可以写str
'中文'
```

当存储和传输时，需要进行编码和解码，即encode()和decode()两个函数，这两个函数都是将str转化成bytes，Python中使用b' '的形式表示字节类型。

```python
#编码
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
# str如果超过ascii的范围，仍然转为ascii会报错
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
# 解码
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```

len()函数用来获取字符串长度，如果是bytes类型，得到的是字节数

```python
>>> len(b'ABC')
3
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
6
>>> len('中文'.encode('utf-8')) # 一个中文使用3个字节编码，所以是6个字节
6
```

#### 字符串格式化

和C语言一样使用%进行占位，%d表示整数，%f表示浮点数，%s表示字符串，%x表示16进制整数

还可以指定是否补0和整数和小数的位数

```python
# 以%区分，前面是一个包含占位符的字符串，后面是对应的变量，如果多个用()括起来
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
# 补0，两位则是%02d
>>> '%2d-%02d' % (3, 1) 
 3-01
# 浮点数保留小数点后两位
>>> '%.2f' % 3.1415926
3.14
```

参考：https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896

## 3. list和tuple

- list：列表，是一种有序集合，元素可变，使用[ ]赋值，一个list中的元素数据类型可以不同

  ```python
  arr = [1, 2, 'abc', [4, 5]]
  # 使用len()方法获取list长度
  print(len(arr)) # 4
  
  # 可直接访问数组下标和修改，如果list为嵌套关系也可以用二维数组的方式访问元素
  print(arr[0]) # 1
  arr[0] = 2
  print(arr) # [2, 2, 'abc', [4, 5]]
  arr[0] = 1
  print(arr[3][1]) # 5
  
  # 下标为负数的时候表示访问数组的倒数第几个元素,即len(arr) - n个元素
  print(arr[-1]) # [4, 5]
  
  # append()方法用来向list结尾添加元素，insert()用来在某个下标处插入元素
  arr.append(6)
  print(arr) # [1, 2, 'abc', [4, 5], 6]
  arr.insert(2, 'efg') 
  print(arr) # [1, 2, 'efg', 'abc', [4, 5], 6]
  
  # pop()方法用来从list结尾移出元素，相当于栈的pop()，如果加参数，表示移除该下标处的元素
  arr.pop()
  print(arr) # [1, 2, 'efg', 'abc', [4, 5]]
  arr.pop(1)
  print(arr) # [1, 'efg', 'abc', [4, 5]]
  ```

- tuple：元组，是一种有序集合，但初始化后不能修改，使用( )赋值

  ```python
  arr = (1, 2, 'abc', [4, 5])
  print(arr) # (1, 2, 'abc', [4, 5])
  # 使用len()方法获取长度
  print(len(arr)) # 4
  # 元素只读，不能修改，且没有append(), insert(), pop()这些方法
  print(arr[2]) # abc
  arr[2] = 1 # TypeError: 'tuple' object does not support item assignment
  
  # 但需要注意，tuple中元素不可变，指的是指向关系不变，如果其内部还有list类型，list的元素是可以改变的
  arr[3][0] = 5
  print(arr) # (1, 2, 'abc', [5, 5])
  
  # 当tuple中只有一个元素的时候，需要在后面加一个, ，否则就赋值成了一个单独元素
  arr1 = (1)
  print(arr1) # 1
  arr2 = (1,)
  print(arr2) # (1,)
  print(arr2[0]) # 1
  ```

## 4. 条件语句和循环语句

### 条件语句

```python
# if语句
# 注意if，else语句后面都必须加:，elif是else if的简写，if内的语句只需要缩进不需要加{}
age = 20
if age > 10:
  print('a')
  print('b')
elif age > 12:
  print('c')
else:
  print('d')
```

### 循环语句

有for x in ...和while两种语句，break可以提前退出循环，continue可以结束本次循环

```python
# 循环和if语句一样需要加:，不需要{}
arr = [1, 2, 'abc']
for i in arr:
  print(i) # 1 2 abc
sum = 0
i = 0
while i < 10:
  sum += i
  i += 1 # python没有++运算符
print(sum) # 45

# 可以使用range函数得到某个范围内的连续整数列表，如range(10)产生0 - 9的list，range(2, 10)产生2 - 9的list
sum = 0
for i in range(10):
  sum += i
print(sum) # 45

sum = 0
for i in range(2, 10):
  sum += i
print(sum) # 44

# 想在循环中访问list的下标，可以使用enumerate函数对list进行处理
for index, value in enumerate(arr):
  print(index * 2) # 0 2 4
```

## 5. dict和set

- dict：字典(也就是map)，采用key - value形式，key必须唯一，通过{ key1: value1, key2: value2 .... }形式进行赋值

  ```python
  # 声明空dict
  d1 = {}
  print(type(d1), d1) # <class 'dict'> {}
  d = {'a': 1, 'b': 2, 'c': 3}
  # 直接通过[]访问value或者通过get()方法，访问的key不存在会报错
  print(d['a']) # 1
  print(d.get('a')) # 1
  print(d['d']) # KeyError: 'd'
  # 通过赋值对value进行添加和修改
  d['b'] = 4
  d['d'] = 5
  print(d) # {'a': 1, 'b': 4, 'c': 3}
  # 通过in操作符判断key是否存在
  print('a' in d) # True
  print('e' in d) # False
  # 通过pop(key)方法移除一个key,通过clear()清空一个dict
  d.pop('b')
  print(d) # {'a': 1, 'c': 3}
  d.clear()
  print(d) # {}
  ```

- set：存储一组key，key必须是唯一的，不能重复，内部元素无序，通过set([key1, key2, key3 ...])形式或{key1, key2, key3 ...}赋值（注意不能使用s = {}的方式声明一个空set，{}默认是一个dict类型）。

  ```python
  #声明空set的正确姿势
  s1 = set()
  print(type(s1), s1) # <class 'set'> set()
  # s = set([1, 2, 'abc'])
  s = {1, 2, 'abc'}
  # 通过add()方法添加元素，如果已经有了就不再添加
  s.add(1)
  print(s) # {1, 2, 'abc'}
  s.add(3)
  print(s) # {3, 1, 2, 'abc'}
  # 通过in判断set内是否有某个key
  print(1 in s) # True
  print(4 in s) # False
  # 通过remove(key)函数移除元素，通过clear()方法清空set
  s.remove(2)
  print(s) # {1, 3, 'abc'}
  s.clear()
  print(s) # set()
  ```

**注意**：无论是set类型还是dict类型，其中作为key的元素都必须是不可变对象，在python中整数，浮点数，字符串都不可变，list可变，tuple虽然不可变但如果其中嵌套了可变对象，也不能作为key

```python
s = set([1, 'abc', (2, 3, 4)])
print(s) # {'abc', 1, (2, 3, 4)}
s = set([1, 'abc', [1, 2, 3]]) # TypeError: unhashable type: 'list'
s = set([1, 'abc', (1, 2, [3, 4])]) # TypeError: unhashable type: 'list'
```

