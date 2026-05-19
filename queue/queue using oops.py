class Queue:
	def __init__(self):
		self.max=5
		self.L=[0]*5
		self.front=self.rear=-1
	def Enqueue(self,ele):
		if self.rear==self.max-1:
			print("Overflow!")
			return
		if self.front==-1:
			self.front=self.front+1
		self.rear=self.rear+1
		self.L[self.rear]=ele
		print(f"Element {ele} inserted!")
	def Dequeue(self):
		if self.front==-1:
			print("Underflow!")
			return
		print(f"Deleted element = {self.L[self.front]}")
		if self.front==self.rear:
			self.front=self.rear=-1
			return
		self.front=self.front+1
	def Peek(self):
		if self.front==-1:
			print("Underflow!")
			return
		print(f"Top element = {self.L[self.front]}")
	def Disp(self):
		if self.front==-1:
			print("Underflow!")
			return
		i=self.front
		print("Elements are: ")
		while i<=self.rear:
			print(self.L[i])
			i=i+1

q=Queue()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Disp()
q.Peek()
q.Dequeue()
q.Disp()