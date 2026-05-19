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
			cur.prev=cur
			cur.next=cur
			if cls.head==None:
				cls.head=cur
			else:
				ptr.next=cur
				cur.prev=ptr
				cur.next=cls.head
				cls.head.prev=cur
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
		while ptr.next!=cls.head:
			print(ptr.data)
			ptr=ptr.next
		print(ptr.data)

	@classmethod
	def bwd_disp(cls):
		if cls.head==None:
			print("No elements")
			return
		print("Elements are: ")
		ptr=cls.head.prev
		while ptr!=cls.head:
			print(ptr.data)
			ptr=ptr.prev
		print(ptr.data)

	@classmethod
	def delbegn(cls):
		if cls.head==None:
			print("No elements!")
			return 
		print("Deleted element: ",cls.head.data)
		if cls.head.next==cls.head:
			cls.head=None
			return
		temp=cls.head.prev
		cls.head=cls.head.next
		temp.next=cls.head	
		cls.head.prev=temp
		
SL.create()
SL.fwd_disp()
SL.bwd_disp()
SL.delbegn()
SL.fwd_disp()
SL.bwd_disp()