class Node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
class SL:
	head=None
	@classmethod
	def create(cls):
		ptr,cur=None,None
		c=0
		ct=1
		while ct==1:
			c=c+1
			print(f"Enter node {c} data: ")
			ele=int(input())
			cur=Node(ele)
			cur.next=None
			if cls.head==None:
				cls.head=cur
			else:
				ptr.next=cur
			ptr=cur
			print("Do you want to continue adding data?(press 1 else press any number to exit): ")
			ct=int(input())
	@classmethod
	def disp(cls):
		print("Elements are: ")
		ptr=cls.head
		while ptr!=None:
			print(ptr.data)
			ptr=ptr.next
	@classmethod
	def countoddeven(cls):
		o,e=0,0
		ptr=cls.head
		while (ptr!=None):
			if ptr.data%2==0:
				e=e+1
			else:
				o=o+1
			ptr=ptr.next
		print(f"Odd= {o}\nEven= {e}")
SL.create()
SL.disp()
SL.countoddeven()