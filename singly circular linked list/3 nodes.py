class node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
f=node(10)
s=node(20)
t=node(30)
f.next=s
s.next=t
t.next=f
ptr=f
while (ptr.next!=f):
	print(ptr.data)
	ptr=ptr.next
print(ptr.data)