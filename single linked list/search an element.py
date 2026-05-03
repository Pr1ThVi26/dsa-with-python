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
	def search(cls,num):
		c=0
		ptr=cls.head
		while ptr!=None:
			c=c+1
			if ptr.data==num:
				print(f"Element found at {c} position")
				break
			ptr=ptr.next
		if ptr==None:
			print("Element not found!")

SL.create()
SL.disp()
num=int(input("Enter element to search :"))
SL.search(num)