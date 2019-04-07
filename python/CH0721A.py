def passFun(name,score):
     print("自定义函数的形式参数")
     print('name',id(name))
     print('score',id(score))
na='Mary';sc=[75,68]
passFun(na,sc)
print('na',id(na))
print('sc',id(sc))
