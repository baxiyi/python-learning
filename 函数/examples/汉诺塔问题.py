# a表示要移动圆盘的柱子，b表示中间借助的柱子，c表示目标柱子
def move(n, a, b, c):
  if n == 1:
    print(a, '-->', c)
    return
  move(n - 1, a, c, b)
  print(a, '-->', c)
  move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')