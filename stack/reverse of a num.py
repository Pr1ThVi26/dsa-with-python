max=100
L=[0]*max
top=-1
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
def reverse(num):
	c=0
	while num>0:
		rem=num%10
		Push(rem)
		num=num//10
		c=c+1
	res=0
	s=''
	for i in range(c):
		temp=str(Pop())
		s=s+temp
		#res=res*10+temp
	return s[::-1]
num=int(input("Enter a number : "))
res=reverse(num)
print(L)
print(f"Reverse of {num} = {res}")