score=[(22,33,44,93),(22,44,52,345),(244,55,32,33)]
avg=[ sum(item)/len(item )  for item in score  ]
print('平均分{0[0]},{0[1]},{0[2]}'.format(avg))
