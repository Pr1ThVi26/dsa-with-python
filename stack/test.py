str="32 323 "
L=[]
x=''
for i in str:
	if i.isspace():
		L.append(x)
		x=''
		continue
	else:
		x=x+i
print(L)