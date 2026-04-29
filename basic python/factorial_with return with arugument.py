def fact(n):
	f=1
	for i in range(1,num+1):
		f=f*i
	return f
num=int(input("Enter a number :"))
res=fact(num)
print("Factorial =",res)