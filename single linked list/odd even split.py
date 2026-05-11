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
	def insertend(cls,L1,ele):
		cur=Node(ele)
		cur.next=None
		if L1==None:
			L1=cur
			return L1
		ptr=L1
		while (ptr.next!=None):
			ptr=ptr.next
		ptr.next=cur
		return L1

	@classmethod
	def evenoddsplit(cls,L1):
		ptr=L1
		odd=None
		even=None
		while ptr!=None:
			if ptr.data%2==0:
				even=cls.insertend(even,ptr.data)
			else:
				odd=cls.insertend(odd,ptr.data)
			ptr=ptr.next
		print("Even")
		SL.disp(even)
		print("Odd")
		SL.disp(odd)
L1=SL.create()
SL.disp(L1)
SL.evenoddsplit(L1)