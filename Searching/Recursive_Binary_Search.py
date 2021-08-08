def binary_search(a,low,high,key):
    if(high<low):
        return low-1
    mid=low+(high-low)//2
    if(key==a[mid]):
        return mid
    elif(k<a[mid]):
        return binary_search(a,low,mid-1,key)
    else:
        return binary_search(a,mid+1,high,key)

#binary search requires sorted array
arr=list(map(int,input().strip().split()))
l=0
h=len(arr)-1
k=int(input())
print(binary_search(arr,l,h,k))

