for num in range(1,1001,1):
	sum=0
	for i in range(1,num//2+1):
		if (num%i==0):
			sum=sum+i
	if (sum==num):
		print(num,"Perfect")