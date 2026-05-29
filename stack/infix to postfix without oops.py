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
def operand(char):
	if (char>='a' and char<='z') or (char>='A' and char<='Z') or char in "0123456789":
		return True
	else:
		return False
def operator(char):
	if char in "+-*/^":
		return True
	else:
		return False
def precedence(char):
	if char=="^":
		return 3
	elif char in "*/":
		return 2
	elif char in "+-":
		return 1
	else:
		return 0
def intopost(s):
	p=""
	s=s+')'
	Push('(')
	for i in s:
		if operand(i):
			p=p+i
		elif i=='(':
			Push(i)
		elif operator(i):
			x=Pop()
			while operator(x) and precedence(x)>=precedence(i):
				p=p+x
				x=Pop()
			Push(x)
			Push(i)
		elif i==')':
			x=Pop()
			while x!='(':
				p=p+x
				x=Pop()
	return p
print("Enter an infix expression : ")
i=input()
p=intopost(i)
print("Postfix expression = ",p)