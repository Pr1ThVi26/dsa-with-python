import sys
num=int(input("Enter a num :"))
c=0
if num==0 or num==1:
	print("Exit")
	sys.exit(0)
for i in range(2,num//2+1):
	if (num%i==0):
		c=c+1
if (c==0):
	print(num,"Prime")