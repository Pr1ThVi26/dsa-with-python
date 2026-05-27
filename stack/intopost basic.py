def operand(char):
	if (char>='a' and char<='z') or (char>='A' and char<='Z'):
		print("Operand")
	else:
		print("Not operand")
def operator(char):
	if char in "+-*/":
		print("Operator")
	else:
		print("Not operator")
def digit(char):
	if char in "0123456789":
		print("Digit")
	else:
		print("Not digit")
def precedence(char):
	if char=="^":
		print("Highest precedence")
	elif char in "*/":
		print("Lesser precedence")
	elif char in "+-":
		print("Low precedence")
	else:
		print("Lowest precedence")
str=''
def string(char):
	global str
	str=str+char
	return str

char=input("Enter character: ")
while True:
	print("1. Check Operand")
	print("2. Check Operator")
	print("3. Check Digit")
	print("4. Check Precedence")
	print("5. Add Character To String")
	print("6. Exit")
	ch=int(input("Enter choice: "))
	match ch:
		case 1:
			operand(char)
		case 2:
			operator(char)
		case 3:
			digit(char)
		case 4:
			precedence(char)
		case 5:
			print("String =",string(char))
		case 6:
			print("Program ended")
			exit(0)
		case _:
			print("Invalid choice")
			exit(0)