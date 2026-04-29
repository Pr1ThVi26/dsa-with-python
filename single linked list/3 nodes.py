class node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
f=node(10)
s=node(20)
t=node(30)
f.next=s
s.next=t
ptr=f
while (ptr!=None):
	print(ptr.data)
	ptr=ptr.next