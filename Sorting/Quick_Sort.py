def partition(arr,l,r):
    pivot=arr[l]
    j=l
    for i in range(l+1,r+1):
        if(arr[i]<=pivot):
            j+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[l],arr[j]=arr[j],arr[l]
    return j

def quick_sort(arr,l,r):
    if(l<r):
        m=partition(arr,l,r)
        quick_sort(arr,l,m-1)
        quick_sort(arr,m+1,r)
    return arr

l=list(map(int,input().strip().split()))
lw=0
hg=len(l)-1

print(quick_sort(l,lw,hg))
