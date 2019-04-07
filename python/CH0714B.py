def total (num1,num2,num3):
     result=0
     for item in range(num1,num2,num3):
          result+=item
     return result
print('计算数值总和,输入-1停止计算')
key=input('按y开始,按n停止---')
while key=='y':
     start=int(input('输入起始值:'))
     finish=int(input("输入终点值:"))
     step=int(input("输入间距值:"))

     #调用自定义函数total
     print('数值总和:{:,}'.format(
total(start,finish,step)
          ))
     key=input('按y开始,按n结束')
