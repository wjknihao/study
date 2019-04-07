ambit=5
student=[]
print('请输入5个数值:')
for item in range(ambit):
     line=input()
     student.append(int(line))
else:
     print("输入完毕")
for item in student:
     print("输入过{0}".format(item))
     
print(sum([1,2,3]))
