def binary_search(a,low,high,key):
    while(low<=high):
        mid=low+(high-low)//2
        if(key==a[mid]):
            return mid
        elif(key<a[mid]):
            high=mid-1
        else:
            low=mid+1
    return low-1

arr=list(map(int,input().strip().split()))
l=0
h=len(arr)-1
k=int(input())
print(binary_search(arr,l,h,k))
