# 输入输出
# a = input('please input your name: ')
# print('hello', a)

# 基本数据类型
# 字符串
# print('\\\\n\\')
# print(r'\\\\\n') # r''表示''内的字符不进行转义
# 布尔型
# a = True
# b = False
# print(a and b)
# print(a or b)
# print(not a)
# print(not None)
# 除法运算
# print(5 // 3)
# print(4.5 // 3)
# print(4.5 / 3)
# 字符串编码
# print('你好啊')
# a = '好'
# b = u'好'
# print(type(a))
# print(type(b))
# print('\u4e2d\u6587')
# print('ABC'.encode('utf-8'))
# print('中国'.encode('utf-8'))
# print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('utf-8'))
# print(len('中文'))
# print(len(b'\xe4\xb8\xad\xe5\x9b\xbd'))
# 字符串格式化
# print('%2d - %02d' % (2, 6))
# print('%10.2f' % 3.144444)
# list类型
# arr = [1, 2, 'abc', [4, 5]]
# # 使用len()方法获取list长度
# print(len(arr)) # 4

# # 可直接访问数组下标和修改，如果list为嵌套关系也可以用二维数组的方式访问元素
# print(arr[0]) # 1
# arr[0] = 2
# print(arr) # [2, 2, 'abc', [4, 5]]
# arr[0] = 1
# print(arr[3][1]) # 5

# # 下标为负数的时候表示访问数组的倒数第几个元素,即len(arr) - n个元素
# print(arr[-1]) # [4, 5]

# # append()方法用来向list结尾添加元素，insert()用来在某个下标处插入元素
# arr.append(6)
# print(arr) # [1, 2, 'abc', [4, 5], 6]
# arr.insert(2, 'efg') 
# print(arr) # [1, 2, 'efg', 'abc', [4, 5], 6]

# # pop()方法用来从list结尾移出元素，相当于栈的pop()，如果加参数，表示移除该下标处的元素
# arr.pop()
# print(arr) # [1, 2, 'efg', 'abc', [4, 5]]
# arr.pop(1)
# print(arr) # [1, 'efg', 'abc', [4, 5]]

# tuple类型
# arr = (1, 2, 'abc', [4, 5])
# print(arr) # (1, 2, 'abc', [4, 5])
# # 使用len()方法获取长度
# print(len(arr)) # 4
# # 元素只读，不能修改，且没有append(), insert(), pop()这些方法
# print(arr[2]) # abc
# # arr[2] = 1 # TypeError: 'tuple' object does not support item assignment

# # 但需要注意，tuple中元素不可变，指的是指向关系不变，如果其内部还有list类型，list的元素是可以改变的
# arr[3][0] = 5
# print(arr) # (1, 2, 'abc', [5, 5])

# # 当tuple中只有一个元素的时候，需要在后面加一个, ，否则就赋值成了一个单独元素
# arr1 = (1)
# print(arr1) # 1
# arr2 = (1,)
# print(arr2) # (1,)
# print(arr2[0]) # 1

# if语句
# 注意if，else语句后面都必须加:，elif是else if的简写，if内的语句只需要缩进不需要加{}
# age = 20
# if age > 10:
#   print('a')
#   print('b')
# elif age > 12:
#   print('c')
# else:
#   print('d')

# 循环和if语句一样需要加:，不需要{}
# arr = [1, 2, 'abc']
# for i in arr:
#   print(i) # 1 2 abc
# sum = 0
# i = 0
# while i < 10:
#   sum += i
#   i += 1 # python没有++运算符
# print(sum) # 45

# # 可以使用range函数得到某个范围内的连续整数列表，如range(10)产生0 - 9的list，range(2, 10)产生2 - 9的list
# sum = 0
# for i in range(10):
#   sum += i
# print(sum) # 45

# sum = 0
# for i in range(2, 10):
#   sum += i
# print(sum) # 44

# # 想在循环中访问list的下标，可以使用enumerate函数对list进行处理
# for index, value in enumerate(arr):
#   print(index * 2) # 0 2 4

# dict类型
# # 声明空dict
# d1 = {}
# print(type(d1), d1) # <class 'dict'> {}
# d = {'a': 1, 'b': 2, 'c': 3}
# # 直接通过[]访问value或者通过get()方法，访问的key不存在会报错
# print(d['a']) # 1
# print(d.get('a')) # 1
# print(d['d']) # KeyError: 'd'
# # 通过赋值对value进行添加和修改
# d['b'] = 4
# d['d'] = 5
# print(d) # {'a': 1, 'b': 4, 'c': 3}
# # 通过in操作符判断key是否存在
# print('a' in d) # True
# print('e' in d) # False
# # 通过pop(key)方法移除一个key,通过clear()清空一个dict
# d.pop('b')
# print(d) # {'a': 1, 'c': 3}
# d.clear()
# print(d) # {}

# set类型
# #声明空set的正确姿势
# s1 = set()
# print(type(s1), s1) # <class 'set'> set()
# # s = set([1, 2, 'abc'])
# s = {1, 2, 'abc'}
# # 通过add()方法添加元素，如果已经有了就不再添加
# s.add(1)
# print(s) # {1, 2, 'abc'}
# s.add(3)
# print(s) # {3, 1, 2, 'abc'}
# # 通过in判断set内是否有某个key
# print(1 in s) # True
# print(4 in s) # False
# # 通过remove(key)函数移除元素，通过clear()方法清空set
# s.remove(2)
# print(s) # {1, 3, 'abc'}
# s.clear()
# print(s) # set()
# 无论是set类型还是dict类型，其中作为key的元素都必须是不可变对象，在python中整数，浮点数，字符串都不可变，list可变，
# tuple虽然不可变但如果其中嵌套了可变对象，也不能作为key
# s = set([1, 'abc', (2, 3, 4)])
# print(s) # {'abc', 1, (2, 3, 4)}
# s = set([1, 'abc', [1, 2, 3]]) # TypeError: unhashable type: 'list'
# s = set([1, 'abc', (1, 2, [3, 4])]) # TypeError: unhashable type: 'list'
