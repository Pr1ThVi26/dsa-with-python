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
Enqueue(10)
Enqueue(20)
Enqueue(30)
Disp()
Peek()
Dequeue()
Disp()