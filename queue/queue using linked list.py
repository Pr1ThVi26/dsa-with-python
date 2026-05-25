class Node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
class myQueue:
	def __init__(self):
		self.front=None
		self.rear=None
	def Enqueue(self,ele):
		cur=Node(ele)
		if self.front==None:
			self.front=cur
		if self.rear==None:
			self.rear=cur
		else:
			self.rear.next=cur
			self.rear=cur
		print(f"Element {ele} inserted!")
	def Dequeue(self):
		if self.front==None:
			print("Underflow!")
			return
		print("Deleted element =",self.front.data)
		if self.front==self.rear:
			self.rear=self.rear=None
			return
		self.front=self.front.next
	def Peek(self):
		if self.front==None:
			print("Underflow!")
			return
		print("Top element =",self.front.data)
	def Disp(self):
		if self.front==None:
			print("Underflow!")
			return
		ptr=self.front
		while ptr!=None:
			print(ptr.data)
			ptr=ptr.next
			
q=myQueue()
c='y'
while c=='y' or c=="Y":
	print("1. Push element\n2. Pop element\n3. Show top element\n4. Display all elements")
	ch=int(input("Enter your choice: "))
	match ch:
	    case 1:
	    	ele=int(input("Enter element: "))
	    	q.Enqueue(ele)
	    case 2:
	        q.Dequeue()
	    case 3:
	        q.Peek()
	    case 4:
	        q.Disp()
	print("Continue doing operation on the queue?(y/n)")
	c=input()