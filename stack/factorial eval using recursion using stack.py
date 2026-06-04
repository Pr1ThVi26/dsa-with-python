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
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)
num=int(input("Enter a number : "))
max=num
L=[0]*max
top=-1
res=factorial(num)
print(f"Factorial of {num} = {res}")