# 错误处理
# try:
#   print('try')
#   r = 10 / int('a')
#   print('result:', r)
# except ZeroDivisionError as e:
#   print('zero division error:',e)
# except ValueError as e:
#   print('value error:', e)
# else:
#   print('no error')
# finally:
#   print('finally')
# print('end')
# # try
# # value error: invalid literal for int() with base 10: 'a'
# # finally
# # end
# 根据调用栈捕获
# def foo(s):
#   return 10 / int(s)
# def bar(s):
#   return foo(s)*2
# def main():
#   try:
#     bar('0')
#   except Exception as e:
#     print('Error', e)
#   finally:
#     print('finally')
# main()
# # Error division by zero
# # finally

# 调用栈
# def foo(s):
#     return 10 / int(s)
# def bar(s):
#     return foo(s) * 2
# def main():
#     bar('0')
# main()
# # Traceback (most recent call last):
# #   File "test.py", line 26, in <module>
# #     main()
# #   File "test.py", line 25, in main
# #     bar('0')
# #   File "test.py", line 23, in bar
# #     return foo(s)*2
# #   File "test.py", line 21, in foo
# #     return 10 / int(s)
# # ZeroDivisionError: division by zero
# logging记录错误
# import logging
# def foo(s):
#   return 10 / int(s)
# def bar(s):
#   return foo(s)*2
# def main():
#   try:
#     bar('0')
#   except Exception as e:
#     logging.exception(e)
#   finally:
#     print('finally')
# main()
# # ERROR:root:division by zero
# # Traceback (most recent call last):
# #   File "test.py", line 61, in main
# #     bar('0')
# #   File "test.py", line 58, in bar
# #     return foo(s)*2
# #   File "test.py", line 56, in foo
# #     return 10 / int(s)
# # ZeroDivisionError: division by zero
# # finally

# 抛出错误  
# def foo(s):
#   n = int(s)
#   if n == 0:
#     raise ZeroDivisionError('invalid value %s' % s)
#   return 10 / n
# def main():
#   try:
#     foo('0')
#   except Exception as e:
#     print('except', e)
# main()
# # except invalid value 0

# def foo(s):
#   n = int(s)
#   if n == 0:
#     raise ZeroDivisionError('invalid value %s' % s)
#   return 10 / n
# def bar(s):
#   try:
#     foo(s)
#   except Exception as e:
#     print('bar except', e)
#     raise
# def main():
#   try:
#     bar('0')
#   except Exception as e:
#     print('main except', e)
# main()
# # bar except invalid value 0
# # main except invalid value 0

# import logging, os
# logging.basicConfig(level=logging.INFO, 
#   filename=os.path.dirname(__file__)+'/logs/test.log',format='[%(asctime)s-%(filename)s:-%(levelname)s:%(message)s]',
#   filemode='a'
# )
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

import pdb
s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)
