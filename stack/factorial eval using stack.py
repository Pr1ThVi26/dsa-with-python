def Push(ele):
	global top
	if top==max-1:
		print("Overflow!")
		return
	top=top+1
	L[top]=ele
def Pop():
	global top
	if top==-1:
		print("Underflow!")
		return
	ele=L[top]
	top=top-1
	return ele
def factorial(num):
	temp=num
	while num<=temp and num>0:
		Push(num)
		num=num-1
	m=1
	for i in range(1,temp+1):
		m=m*Pop()
	return m
num=int(input("Enter a number : "))
max=num
L=[0]*max
top=-1
res=factorial(num)
print(f"Factorial of {num} = {res}")