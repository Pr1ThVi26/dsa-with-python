def quicksort(l,left,right):
	if left<right:
		pivot=l[left]
		i=left+1
		j=right
		while i<j:
			while i<=right and l[i]<=pivot:
				i=i+1
			while l[j]>pivot:
				j=j-1
			if i<j:
				temp=l[i]
				l[i]=l[j]
				l[j]=temp
		temp=l[left]
		l[left]=l[j]
		l[j]=temp
		quicksort(l,left,j-1)
		quicksort(l,j+1,right)
l=[0]*5
for i in range(len(l)):
	ele=int(input("Enter element : "))
	l[i]=ele
print("Before sorting :",l)
quicksort(l,0,len(l)-1)
print("After sorting :",l)