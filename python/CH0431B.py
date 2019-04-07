import math
print ("%.3f:输出含有三个小数为啥的PI值")
fmt="含有四位小数:%.4f"
print("PI",fmt%(math.pi))
radius=(math.pi)*5**2
print('含有四位小数','%.4f'%radius)
print('按四位整数输出','%04d'%radius)
