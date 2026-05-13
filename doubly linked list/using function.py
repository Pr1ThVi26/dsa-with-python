class Node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
		self.prev=None
		
class SL:
	head=None
	@classmethod
	def create(cls):
		ptr,cur,prev=None,None,None
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
				cur.prev=ptr
			ptr=cur
			print("Do you want to continue adding data?(press 1 else press any number to exit): ")
			ct=int(input())

		@classmethod
	def fwd_disp(cls):
		if cls.head==None:
			print("No elements")
			return
		print("Elements are: ")
		ptr=cls.head
		while ptr.next!=None:
			print(ptr.data)
			ptr=ptr.next
		print(ptr.data)

	@classmethod
	def bwd_disp(cls):
		if cls.head==None:
			print("No elements")
			return
		print("Elements are: ")
		ptr=cls.head
		while ptr.next!=None:
			ptr=ptr.next
		while ptr!=None:
			print(ptr.data)
			ptr=ptr.prev


SL.create()
SL.fwd_disp()
SL.bwd_disp()