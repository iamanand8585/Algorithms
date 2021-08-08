def linear_search_rec(a,low,high,key):
    if(high<low):
        return "Not Found"
    if(a[low]==key):
        return low
    return linear_search_rec(a,low+1,high,key)

arr=list(map(int,input().strip().split()))
l=0
h=len(arr)-1
k=int(input())
print(linear_search_rec(arr,l,h,k))