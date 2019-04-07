import math
print('PI={0.pi}'.format(math))
print('PI=%10.4f'%math.pi) #输出四位小数
radius=math.pi*26**2
print('PI={0:.4f}\n'#圆面积加千位逗号
     '圆面积={1:,.3f}'.format(math.pi,radius))
area=int(radius) #转为整数
print("圆面积={0:d},{0:#x},{0:#b}".format(area))
print("靠右={0:*>10d}".format(area))
print("居中={0:*^10d}".format(area))
