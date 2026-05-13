class Node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
		self.prev=None
head,cur,ptr,prev=None,None,None,None
c=0
ct=1
while ct==1:
	c=c+1
	print(f"Enter node {c} data: ")
	ele=int(input())
	cur=Node(ele)
	cur.next=None
	cur.prev=None
	if head==None:
		head=cur
	else:
		ptr.next=cur
		cur.prev=ptr
	ptr=cur
	print("Do you want to continue adding data?(press 1 else press any number to exit): ")
	ct=int(input())
print("Elements in froward: ")
ptr=head
while ptr.next!=None:
	print(ptr.data)
	ptr=ptr.next
print(ptr.data)
print("Elements in backward: ")
while ptr!=None:
	print(ptr.data)
	ptr=ptr.prev