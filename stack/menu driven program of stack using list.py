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

c=1
while c==1:
	print("1. Push element\n2. Pop element\n3. Show top element\n4. Display all elements")
	ch=int(input("Enter your choice: "))
	match ch:
	    case 1:
	    	ele=int(input("Enter element: "))
	    	Push(ele)
	    case 2:
	        Pop()
	    case 3:
	        Peek()
	    case 4:
	        Disp()
	print("Continue doing operation on the stack?(press 1 to continue)")
	c=int(input())