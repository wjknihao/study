month=int(input('请输入1-12月份'))
if month >=1 and month <=12:
     if month ==4 or month==6 or month==12:
          print('{0}月有30天'.format(month))
     elif month==2:
          print('{0}月有28或29天'.format(month))
     else:
          print('{0}月有31天'.format(month))
else:
     print('输入月份不对,请重新输入')
     
