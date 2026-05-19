max=5
front=rear=-1
L=[0]*5
def Enqueue(ele):
	global front,rear
	if (rear==max-1 and front==0) or front==rear+1:
		print("Overflow!")
		return
	if front==-1:
		front=rear=0
	else:
		if rear==max-1:
			rear=0
		else:
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
	if front==max-1:
		front=0
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
	print("Elements are: ")
	if front<=rear:
		i=front
		while i<=rear:
			print(L[i])
			i=i+1
	else:
		i=front
		while i<=max-1:
			print(L[i])
			i=i+1
		i=0
		while i<=rear:
			print(L[i])
			i=i+1

Enqueue(10)
Enqueue(20)
Enqueue(30)
Enqueue(40)
Enqueue(50)
Disp()
Peek()
Dequeue()
Dequeue()
Disp()
Enqueue(60)
Enqueue(70)
Enqueue(80)
Disp()