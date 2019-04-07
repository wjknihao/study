bb=[[1,2,3],[2,5,6],[3,3,3]]
for i,item in enumerate(bb):
           print("第{}行".format(i),end=" ")
           for two in item:
                print(two, end="  ")
else :
     print("数据读取完毕")

wjk=[ [bb for bb in range(1,item+1) ]  for item in range(5)]
print(wjk)
