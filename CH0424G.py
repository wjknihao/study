print("---split()函数分割字符串")
wordA='one two three four'
print('原来的字符串:',wordA)
print(wordA.split())
print(wordA.split(maxsplit=2))
opr='--'
opr*=20
print(opr)
wordB='one,two,three,four'
print('字符串二:',wordB)

print(wordB.split(','))
