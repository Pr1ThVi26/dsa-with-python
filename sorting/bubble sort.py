l=[0]*5
for i in range(len(l)):
	ele=int(input("Enter element : "))
	l[i]=ele
print("Before sorting :\n",l)
for i in range(len(l)-1):
	for j in range(len(l)-1-i):
		if l[j]>l[j+1]:
			temp=l[j]
			l[j]=l[j+1]
			l[j+1]=temp
print("After sorting :\n",l)