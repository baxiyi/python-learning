import torch

# # 赋值
# x = torch.ones(3, 5)
# print(x)
# y = torch.empty(3, 5)
# print(y)
# z = torch.tensor([1, 2])
# print(z)
# m = torch.rand(3, 5)
# print(m)
# n = m.new_ones(2, 3) # 默认使用m的dtype
# print(n)

# # 操作
# x = torch.ones(3, 5)
# print(x.size())
# y = torch.rand(3, 5)
# print(y)
# # 三种计算和的方法
# print(x + y)
# print(torch.add(x, y))
# # 改变自身的函数后面都需要加_
# print(x.add_(y)) 
# # reshape
# x_shape = x.view(15)
# print(x_shape)
# y_shape = y.view(5, -1)
# print(y.size())
# # 单个元素的tensor
# z = torch.tensor([1.0])
# print(z.item())

# # 与numpy数组互相转化
# import numpy as np 
# x = torch.tensor([1, 2])
# a = x.numpy()
# print(x)
# print(a)

# b = np.array([1, 2, 3])
# y = torch.from_numpy(b)
# print(b)
# print(y)


# # Autograd
# x = torch.ones(3, 5)
# print(x.requires_grad)
# x.requires_grad_(True)
# #也可以直接初始化设置requires_grad
# x = torch.ones(3, 5, requires_grad=True)
# print(x.requires_grad)
# y = x + 1
# # 此时y就有了grad_fn
# print(y.grad_fn)
# z = x * y + x
# # 注意必须是标量才能进行backward
# out = z.mean()
# out.backward()
# print(x.grad)
# # 如果不需要grad
# with torch.no_grad():
#     print((x ** 2).requires_grad) # False
# # 用detach()可以复制得到一个不带grad的张量
# z = x.detach()
# print(z.requires_grad)

