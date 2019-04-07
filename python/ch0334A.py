import random
number =random.randint(1,100)
print(type(number))
guess=-1;
while guess !=number :
     guess=int(input('请输入1~100之间的随机数字,猜一猜-->'))
     
     if guess==number:
          print('你猜对了数字是',number)
     elif guess>number:
          print('数字大了')
     else :
          print('数字小了')
