#list=[24, 19, 36, 27, 29]
#sort=[19, 24, 27, 29, 36]
l=[0]*5
for i in range(len(l)):
	ele=int(input("Enter element : "))
	l[i]=ele
print("Before sorting :\n",l)
for i in range(1,len(l)):
	key=l[i]
	j=i-1
	while j>=0 and l[j]>key:
		l[j+1]=l[j]
		j=j-1
	l[j+1]=key
print("After sorting :\n",l)