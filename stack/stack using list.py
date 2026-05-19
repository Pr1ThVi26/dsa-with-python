max=5
L=[0]*5
top=-1
def Push(ele):
	global top
	if top==max-1:
		print("Overflow!")
		return
	top=top+1
	L[top]=ele
	print(f"Element {ele} inserted!")
def Pop():
	global top
	if top==-1:
		print("Underflow!")
		return
	print(f"Deleted element = {L[top]}")
	top=top-1
def Peek():
	if top==-1:
		print("Underflow!")
		return
	print(f"Top element = {L[top]}")
def Disp():
	if top==-1:
		print("Underflow!")
		return
	i=top
	print("Elements are: ")
	while i>=0:
		print(L[i])
		i=i-1
Push(1)
Push(2)
Push(3)
Push(4)
Push(5)
Peek()
Disp()
Pop()
Disp()