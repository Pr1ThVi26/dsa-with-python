class Rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b
	def show(self):
		print("Length :",self.l)
		print("Breadth :",self.b)
	def area(self):
		return self.l*self.b
	def perimeter(self):
		return 2*(self.l+self.b)
print("Enter length and breadth")
length=int(input())
breadth=int(input())
r=Rectangle(length,breadth)
r.show()
print("Area = ",r.area())
print("Perimeter = ",r.perimeter())