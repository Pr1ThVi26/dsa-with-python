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
	def delend(cls):
		if cls.head==None:
			print("No elements")
			return
		if cls.head.next==None:
			print("Deleted element =",cls.head.data)
			cls.head=None
			return
		ptr=cls.head
		while (ptr.next.next!=None):
			ptr=ptr.next
		print("Deleted element =",ptr.next.data)
		ptr.next=None

SL.create()
SL.disp()
SL.delend()
SL.disp()