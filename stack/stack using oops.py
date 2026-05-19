class Stack:
	def __init__(self):
		self.max=5
		self.L=[0]*5
		self.top=-1
	def Push(self,ele):
		if self.top==self.max-1:
			print("Overflow!")
			return
		self.top=self.top+1
		self.L[self.top]=ele
		print(f"Element {ele} inserted!")
	def Pop(self):
		if self.top==-1:
			print("Underflow!")
			return
		print(f"Deleted element = {self.L[self.top]}")
		self.top=self.top-1
	def Peek(self):
		if self.top==-1:
			print("Underflow!")
			return
		print(f"Top element = {self.L[self.top]}")
	def Disp(self):
		if self.top==-1:
			print("Underflow!")
			return
		i=self.top
		print("Elements are: ")
		while i>=0:
			print(self.L[i])
			i=i-1

s=Stack()
s.Push(10)
s.Push(20)
s.Push(30)
s.Disp()
s.Peek()
s.Pop()
s.Disp()