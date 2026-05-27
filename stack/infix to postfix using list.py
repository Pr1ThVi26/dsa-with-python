class myStack:
	def __init__(self):
		self.max=100
		self.L=[0]*self.max
		self.top=-1
	def Push(self,ele):
		if self.top==self.max-1:
			print("Overflow!")
			return
		self.top=self.top+1
		self.L[self.top]=ele
	def Pop(self):
		if self.top==-1:
			print("Underflow!")
			return
		ele=self.L[self.top]
		self.top=self.top-1
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
def intopost(s,L):
	p=""
	s=s+')'
	L.Push('(')
	for i in s:
		if operand(i):
			p=p+i
		elif i=='(':
			L.Push(i)
		elif operator(i):
			x=L.Pop()
			while operator(x) and precedence(x)>=precedence(i):
				p=p+x
				x=L.Pop()
			L.Push(x)
			L.Push(i)
		elif i==')':
			x=L.Pop()
			while x!='(':
				p=p+x
				x=L.Pop()
	return p

print("Enter an infix expression : ")
s=myStack()
i=input()
p=intopost(i,s)
print("Postfix expression = ",p)