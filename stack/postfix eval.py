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
def operator(char):
	if char in "+-*/^":
		return True
	else:
		return False
def result(b,a,i):
	if i=='+':
		return b+a
	elif i=='-':
		return b-a
	elif i=='*':
		return b*a
	elif i=='/':
		return b//a
	elif i=='^':
		return b**a
	else:
		print("Invaid operator")
def posteval(exp):
	x=''
	for i in exp:
		if i.isspace():
			if x!='':
				Push(x)
				x=''
			continue
		elif operator(i):
			a=int(Pop())
			b=int(Pop())
			res=result(b,a,i)
			Push(res)
		else:
			x=x+i
	if x!='':
		Push(x)

print("Enter a postfix expression : ")
inp=input()
p=posteval(inp)
print("Result = ",Pop())