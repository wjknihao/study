print("关键字参数：\n"), dict(name="wjk",age=20,sex="male")
print("列表用元组分组:\n",dict([('one',1),('two',2),('three',3)]))
#使用字典对象
print('字典对象:\n',dict({'jane':1,'feb':2,'mar':3}))
weeks=[1,2,3,4,5,6,7]
number=['a','b','c','d','e','f','g']
wkcomb=dict(zip(number,weeks))
for key in wkcomb:
     print('%3s:%9s'%(key,wkcomb[key]))
