#2.3-2_merge_sort.py

def merge_sort(arr):
	# arr's type is List
	def merge(a,p,q,r):
		L=a[p:q+1]
		R=a[q+1:r+1]
		n1=len(L)
		n2=len(R)
		i=0
		j=0
		for k in range(p,r+1):
			if i==n1:
				a[k:r+1]=R[j:n2]
				break
			elif j==n2:
				a[k:r+1]=L[i:n1]
				break
			elif L[i]<=R[j]:
				a[k]=L[i]
				i=i+1
			else:
				a[k]=R[j]
				j=j+1
		
	def sort(a,p,r):
		if p<r:
			q=(p+r)//2
			sort(a,p,q)
			sort(a,q+1,r)
			merge(a,p,q,r)

	sort(arr,0,len(arr)-1)


arr=[2,1,3,6,4,5,8,7,9]
merge_sort(arr)
print('arr=',arr)