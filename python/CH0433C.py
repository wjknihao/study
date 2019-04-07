wd=input("输入栏款值")
width=int(wd)
print("="*width)
score_width=21 #分数的栏宽
name_width=width-score_width #名字的栏款
data='{0:11s} {1:.2f}'
print("{0:11s} {1}".format("名字","分数"))
print("-"*width)
print(data.format("mary",68.22))
print(data.format("wjk",1000))
print(data.format("zqq",111))
