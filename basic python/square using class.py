class Square:
	def __init__(data,a):
		data.a=a
	def show(data):
		print("Side = ",data.a)
	def area(d):
		return d.a*d.a
	def perimeter(d):
		return 2*d.a
print("Enter side of square : ")
side=int(input())
s=Square(side)
s.show()
print("Area = ",s.area())
print("Perimeter = ",s.perimeter())