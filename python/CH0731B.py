def calcu(*value):
     result=1
     for item in value:
          result+=item;
     return result;
print('1个参数',calcu(9))
print('2个参数',calcu(9,2))
