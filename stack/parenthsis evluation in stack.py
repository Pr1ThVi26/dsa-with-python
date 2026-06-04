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
		return

	ele=L[top]
	top=top-1
	return ele

def parenteval(str):

	for i in str:

		if i in "({[":
			Push(i)

		elif i==')':

			if top==-1:
				print("Invalid expression")
				return

			ch=Pop()

			if ch!='(':
				print("Invalid expression")
				return

		elif i==']':

			if top==-1:
				print("Invalid expression")
				return

			ch=Pop()

			if ch!='[':
				print("Invalid expression")
				return

		elif i=='}':

			if top==-1:
				print("Invalid expression")
				return

			ch=Pop()

			if ch!='{':
				print("Invalid expression")
				return

	if top==-1:
		print("Valid expression")
	else:
		print("Invalid expression")

print("Enter an expression : ")
inp=input()

parenteval(inp) 