number={'grace':68,'tom':76}
number['wjk']=88
print('成绩',number)
number.update({'cjd':99,'zs':44})
print('按名字降序排序')
for value in sorted(number,reverse=True):
     print("%-10s %d"%(value,number[value]))
print('清空字典--',number.clear()) #清空字典
score={'Judy':64,'sunny':60}
number.update(score)
number.update(Steven=99,ivy=74)
print(number)
