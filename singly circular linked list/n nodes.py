class Node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
head,cur,ptr=None,None,None
c=0
ct=1
while ct==1:
	c=c+1
	print(f"Enter node {c} data: ")
	ele=int(input())
	cur=Node(ele)
	cur.next=cur
	if head==None:
		head=cur
	else:
		ptr.next=cur
		cur.next=head
	ptr=cur
	print("Do you want to continue adding data?(press 1 else press any number to exit): ")
	ct=int(input())
print("Elements are: ")
ptr=head
while ptr.next!=head:
	print(ptr.data)
	ptr=ptr.next
print(ptr.data)