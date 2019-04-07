sum =score=0
count=-1
while score!=-1:
	score=int(input('请输入分数'))
	sum+=score
	count+=1
average=sum/count
print('共',count,'科','总分',sum,'平均',average)
