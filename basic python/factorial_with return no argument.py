def fact():
	num=int(input("Enter a number :"))
	f=1
	for i in range(1,num+1):
		f=f*i
	return f
res=fact()
print("Factorial =",res)