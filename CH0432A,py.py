price=135554;
rate=0.08 #税率
print("%4s:"%"定价",format(price,">8d"))
tax=price*rate
print('%4s:'%'税率',format(tax,'011.2f'))
total=price+tax
print('含税价:',format(total,'011.2f'))
