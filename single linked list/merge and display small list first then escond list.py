class Node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
class SL:
	@classmethod
	def create(cls):
		cur=None
		c=0
		ct=1
		head=None
		while ct==1:
			c=c+1
			print(f"Enter node {c} data: ")
			ele=int(input())
			cur=Node(ele)
			cur.next=None
			if head==None:
				head=cur
			else:
				ptr.next=cur
			ptr=cur
			print("Do you want to continue adding data?(press 1 else press any number to exit): ")
			ct=int(input())
		return head
	@classmethod
	def disp(cls,head):
		print("Elements are: ")
		ptr=head
		while ptr!=None:
			print(ptr.data)
			ptr=ptr.next
	@classmethod
	def merge(cls,L1,L2):
		L3=None
		ptr1=L1
		ptr2=L2
		while ptr1!=None and ptr2!=None:
			if ptr1.data<ptr2.data:
				L3=cls.insertend(L3,ptr1.data)
				ptr1=ptr1.next
			else:
				L3=cls.insertend(L3,ptr2.data)
				ptr2=ptr2.next
		while ptr1!=None:
			L3=cls.insertend(L3,ptr1.data)
			ptr1=ptr1.next
		while ptr2!=None:
			L3=cls.insertend(L3,ptr2.data)
			ptr2=ptr2.next
		SL.disp(L3)

	@classmethod
	def insertend(cls,L3,ele):
		cur=Node(ele)
		cur.next=None
		if L3==None:
			L3=cur
			return L3
		ptr=L3
		while (ptr.next!=None):
			ptr=ptr.next
		ptr.next=cur
		return L3

L1=SL.create()
L2=SL.create()
SL.disp(L1)
SL.disp(L2)
print("After merge")
SL.merge(L1,L2)