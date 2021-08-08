def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
    return arr

l=list(map(int,input().strip().split()))

print(selection_sort(l))
