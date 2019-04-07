# 建立表头
print(' |',end='')
for item in range(10):
     # 不自动换行,只留空格符
     print('{0:3d}'.format(item),end='')
print() #换行
print('-'*32)
     #第一重 for/in
for one in range(10):
     print(one,'|',end='')
     for two in range(10):
          print('{0:3d}'.format(one*two),end='')
print()
