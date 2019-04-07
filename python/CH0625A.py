from collections import OrderedDict
stud={'Mary':99,'wjk':99,'zs':22,'df':33}
name=OrderedDict(sorted(
     stud.items(),key=lambda fd:fd[0]
     ))
print('按名字进行升序排列')
for key in name:
     print('%5s'%key,name[key])
print('--------')
print('按分数进行降序排序')
score=OrderedDict(sorted(stud.items(),key=lambda fd:fd[1],reverse=True))
for key in score:
     print('%5s'%key,score[key])
