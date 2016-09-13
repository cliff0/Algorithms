#2.1-2
#insertion-sort

arr=[5,2,4,6,1,3]

def insert_sort(arr):
    length=len(arr)
    if length<2:
        return arr
    else:
        j=length-2
        while(j>=0):
            i=j+1
            key=arr[j]
            while(i<length and key<arr[i]):
                arr[i-1]=arr[i]
                i=i+1
            arr[i-1]=key
            j=j-1
    return arr


print(insert_sort(arr))  # [6,5,4,3,2,1]



