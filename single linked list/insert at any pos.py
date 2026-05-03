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
	def count(cls):
		c=0
		ptr=cls.head
		while (ptr!=None):
			c=c+1
			ptr=ptr.next
		#print(f"Number of nodes = {c}")
		return c
	@classmethod
	def insertanypos(cls):
		pos=int(input("Enter the position you want to enter data: "))
		ele=int(input("Enter the data: "))
		cur=Node(ele)
		if pos == 1:
			cur.next=cls.head
			cls.head=cur
			return
		c=cls.count()
		if pos>c or pos<1:
			print("Invalid postion")
			return
		ptr=cls.head
		i=1
		while i<pos-1:
			i=i+1
			ptr=ptr.next
		cur.next=ptr.next
		ptr.next=cur
SL.create()
SL.disp()
SL.insertanypos()
SL.disp()