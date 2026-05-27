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
	L=[]
	p=""
	s=s+')'
	L.append('(')
	for i in s:
		if operand(i):
			p=p+i
		elif i=='(':
			L.append(i)
		elif operator(i):
			x=L.pop()
			while operator(x) and precedence(x)>=precedence(i):
				p=p+x
				x=L.pop()
			L.append(x)
			L.append(i)
		elif i==')':
			x=L.pop()
			while x!='(':
				p=p+x
				x=L.pop()
	return p

print("Enter an infix expression : ")
i=input()
p=intopost(i)
print("Postfix expression = ",p)