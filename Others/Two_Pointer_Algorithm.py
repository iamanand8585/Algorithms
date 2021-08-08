arr=list(map(int,input().strip().split()))
arr.sort()
key=int(input())
i=0
j=len(arr)-1
while(i<j):
    if(arr[i]+arr[j]<key):
        i+=1
    elif(arr[i]+arr[j]>key):
        j-=1
    else:
        print(arr[i],arr[j])
        break
else:
    print("Not Found")