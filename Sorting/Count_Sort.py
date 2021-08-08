def count_sort(arr):
    mn=min(arr)
    mx=max(arr)
    rg=mx-mn+1
    cnt=[0]*rg
    for i in range(len(arr)):
        cnt[arr[i]-mn]+=1
    for i in range(1,len(cnt)):
        cnt[i]+=cnt[i-1]
    arr1=[0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        arr1[cnt[arr[i]-mn]-1]=arr[i]
        cnt[arr[i]-mn]-=1
    return arr1

l=list(map(int,input().strip().split()))
print(count_sort(l))
