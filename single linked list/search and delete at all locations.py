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
	def searchndel_allLOC(cls,num):
		if cls.head == None:
				print("No element")
				return
		while cls.head!=None and cls.head.data==num:
				cls.head=cls.head.next
		if cls.head == None:
				print("No elements!")
				return
		ptr=cls.head
		temp=None

		while ptr!=None:
			if ptr.data==num:
				temp.next=ptr.next
				ptr=temp.next
				continue
			temp=ptr
			ptr=ptr.next
SL.create()
SL.disp()
num=int(input("Enter element to be deleted :"))
SL.searchndel_allLOC(num)
SL.disp()