class DEqueue:
	def __init__(self):
		self.max=5
		self.L=[0]*5
		self.front=self.rear=-1
	def rearEnqueue(self,ele):
		if self.rear==self.max-1:
			print("Overflow!")
			return
		if self.front==-1:
			self.front=self.front+1
		self.rear=self.rear+1
		self.L[self.rear]=ele
		print(f"Element {ele} inserted!")
	def frontEnqueue(self,ele):
		if (self.front==0 and self.rear==self.max-1) or self.front==self.rear+1:
			print("Overflow!")
			return
		if self.front==-1:
			self.front=self.rear=0
		else:
			if self.front==0:
				self.front=self.max-1
			else:
				self.front=self.front-1
		self.L[self.front]=ele
		print(f"Element {ele} inserted!")
	def frontDequeue(self):
		if self.front==-1:
			print("Underflow!")
			return
		print(f"Deleted element = {self.L[self.front]}")
		if self.front==self.rear:
			self.front=self.rear=-1
			return
		if self.front==self.max-1:
			self.front=0
		else:
			self.front=self.front+1
	def rearDequeue(self):
		if self.front==-1:
			print("Underflow!")
			return
		print(f"Deleted element = {self.L[self.rear]}")
		if self.front==self.rear:
			self.front=self.rear=-1
			return
		if self.rear==0:
			self.rear=self.max-1
		else:
			self.rear=self.rear-1
	def Peekfront(self):
		if self.front==-1:
			print("Underflow!")
			return
		print(f"Top front element = {self.L[self.front]}")
	def Peekrear(self):
		if self.front==-1:
			print("Underflow!")
			return
		print(f"Top rear element = {self.L[self.rear]}")
	def Disp(self):
		if self.front==-1:
			print("Underflow!")
			return
		print("Elements are: ")
		i=self.front
		while True:
			print(self.L[i])
			if i==self.rear:
				break
			if i==self.max-1:
				i=0
			else:
				i=i+1

d=DEqueue()
c='y'
print("1. Input restricted DEqueue")
print("2. Output restricted DEqueue")
print("3. Invalid choice!")
ch1=int(input("Enter your choice: "))
match ch1:
	case 1:
		while c=='y' or c=='Y':
			print("INPUT RESTRICTED DEQUEUE")
			print("1. Push element at rear")
			print("2. Delete front element")
			print("3. Delete rear element")
			print("4. Show top front element")
			print("5. Show top rear element")
			print("6. Display all elements")
			print("7. Exit")
			ch2=int(input("Enter your choice: "))
			match ch2:
				case 1:
					ele=int(input("Enter element: "))
					d.rearEnqueue(ele)
				case 2:
					d.frontDequeue()
				case 3:
					d.rearDequeue()
				case 4:
					d.Peekfront()
				case 5:
					d.Peekrear()
				case 6:
					d.Disp()
				case _:
					print("Invalid choice!")
					exit(0)
			print("Cntinue doing operation on the queue?(y/n)")
			c=input()
	case 2:
		while c=='y' or c=='Y':
			print("OUTPUT RESTRICTED DEQUEUE")
			print("1. Push element at front")
			print("2. Push element at rear")
			print("3. Delete front element")
			print("4. Show top front element")
			print("5. Show top rear element")
			print("6. Display all elements")
			print("7. Exit")
			ch2=int(input("Enter your choice: "))
			match ch2:
				case 1:
					ele=int(input("Enter element: "))
					d.frontEnqueue(ele)
				case 2:
					ele=int(input("Enter element: "))
					d.rearEnqueue(ele)
				case 3:
					d.frontDequeue()
				case 4:
					d.Peekfront()
				case 5:
					d.Peekrear()
				case 6:
					d.Disp()
				case _:
					print("Invalid choice!")
					exit(0)
			print("Cntinue doing operation on the queue?(y/n)")
			c=input()
	case _:
		print("Invalid choice!")
		exit(0)