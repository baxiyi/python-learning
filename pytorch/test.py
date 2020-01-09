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

# network
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 3)
        self.conv2 = nn.Conv2d(6, 16, 3)
        self.fc1 = nn.Linear(16 * 6 * 6, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # print(x.size())
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        # print(x.size())
        batch_size = x.size()[0]
        # print(x.size())
        x = x.view(batch_size, -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    def train(self, x, y):
        optimizer = optim.SGD(self.parameters(), lr=0.01)
        for i in range(100):
            optimizer.zero_grad()
            output = self.forward(x)
            lossfunc = nn.MSELoss()
            loss = lossfunc(output, y)
            print(loss)
            loss.backward()
            optimizer.step()


net = Net()
# print(net)

# params = list(net.parameters())
# print(len(params))
# print(params[0].size())

input = torch.randn(1, 1, 32, 32)
# out = net(input)
# print(out)

target = torch.randn(1, 10)
net.train(input, target)