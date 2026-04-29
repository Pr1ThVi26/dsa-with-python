import sys
for num in range(1,101):
	c=0
	if num==0 or num==1:
		continue
	for i in range(2,num//2+1):
		if (num%i==0):
			c=c+1
	if (c==0):
		print(num,"Prime")