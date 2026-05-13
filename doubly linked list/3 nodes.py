class node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
		self.prev=None
f=node(10)
s=node(20)
t=node(30)
f.prev=None
f.next=s
s.prev=f
s.next=t
t.prev=s
t.next=None
print("Display elements in forward: ")
ptr=f         
while (ptr.next!=None):
	print(ptr.data)
	ptr=ptr.next
print(ptr.data)
print("Display elements in backward: ")
while ptr!=None:
	print(ptr.data)
	ptr=ptr.prev