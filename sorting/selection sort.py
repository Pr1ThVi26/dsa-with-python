l=[0]*5
for i in range(len(l)):
	ele=int(input("Enter element : "))
	l[i]=ele
print("Before sorting :\n",l)
for i in range(len(l)-1):
	for j in range(i+1,len(l)):
		if l[i]>l[j]:
			temp=l[i]
			l[i]=l[j]
			l[j]=temp
print("After sorting :\n",l)