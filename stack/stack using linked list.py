class Node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
class myStack:
	def __init__(self):
		self.top=None
	def Push(self,ele):
		cur=Node(ele)
		cur.next=self.top
		self.top=cur
		print(f"Element {ele} inserted!")
	def Pop(self):
		if self.top==None:
			print("Underflow!")
			return
		print("Deleted element =",self.top.data)
		self.top=self.top.next
	def Peek(self):
		if self.top==None:
			print("Underflow!")
			return
		print("Top element =",self.top.data)
	def Disp(self):
		if self.top==None:
			print("Underflow!")
			return
		ptr=self.top
		while ptr!=None:
			print(ptr.data)
			ptr=ptr.next

s=myStack()
c='y'
while c=='y':
	print("1. Push element\n2. Pop element\n3. Show top element\n4. Display all elements")
	ch=int(input("Enter your choice: "))
	match ch:
	    case 1:
	    	ele=int(input("Enter element: "))
	    	s.Push(ele)
	    case 2:
	        s.Pop()
	    case 3:
	        s.Peek()
	    case 4:
	        s.Disp()
	print("Continue doing operation on the stack?(y/n)")
	c=input()
