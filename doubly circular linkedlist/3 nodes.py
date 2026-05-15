class node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
		self.prev=None
f=node(10)
s=node(20)
t=node(30)
f.prev=t
f.next=s
s.next=t
s.prev=f
t.next=f
t.prev=s
ptr=f
while (ptr.next!=f):
	print(ptr.data)
	ptr=ptr.next
print(ptr.data)
while (ptr.prev!=t):
	print(ptr.data)
	ptr=ptr.prev
print(ptr.data)