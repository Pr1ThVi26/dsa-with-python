def merge(l,left,mid,right):
	n1=mid-left+1
	n2=right-mid
	L=[0]*n1
	R=[0]*n2
	for i in range(n1):
		L[i]=l[left+i]
	for j in range(n2):
		R[j]=l[mid+1+j]
	i=0
	j=0
	k=left
	while i<n1 and j<n2:
		if L[i]<=R[j]:
			l[k]=L[i]
			i=i+1
		else:
			l[k]=R[j]
			j=j+1
		k=k+1
	while i<n1:
		l[k]=L[i]
		i=i+1
		k=k+1
	while j<n2:
		l[k]=R[j]
		j=j+1
		k=k+1
def mergesort(l,left,right):
	if left<right:

		mid=(left+right)//2

		mergesort(l,left,mid)

		mergesort(l,mid+1,right)

		merge(l,left,mid,right)
l=[0]*5
for i in range(len(l)):
	ele=int(input("Enter element : "))
	l[i]=ele
print("Before sorting :",l)
mergesort(l,0,len(l)-1)
print("After sorting :",l)