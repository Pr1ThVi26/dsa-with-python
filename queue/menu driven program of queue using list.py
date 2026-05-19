max=5
front=rear=-1
L=[0]*5
def Enqueue(ele):
	global front,rear
	if rear==max-1:
		print("Overflow!")
		return
	if front==-1:
		front=front+1
	rear=rear+1
	L[rear]=ele
	print(f"Element {ele} inserted!")
def Dequeue():
	global front,rear
	if front==-1:
		print("Underflow!")
		return
	print(f"Deleted element = {L[front]}")
	if front==rear:
		front=rear=-1
		return
	front=front+1
def Peek():
	if front==-1:
		print("Underflow!")
		return
	print(f"Top element = {L[front]}")
def Disp():
	if front==-1:
		print("Underflow!")
		return
	i=front
	print("Elements are: ")
	while i<=rear:
		print(L[i])
		i=i+1

c=1
while c==1:
	print("1. Push element\n2. Pop element\n3. Show top element\n4. Display all elements")
	ch=int(input("Enter your choice: "))
	match ch:
	    case 1:
	    	ele=int(input("Enter element: "))
	    	Enqueue(ele)
	    case 2:
	        Dequeue()
	    case 3:
	        Peek()
	    case 4:
	        Disp()
	print("Continue doing operation on the stack?(press 1 to continue)")
	c=int(input())