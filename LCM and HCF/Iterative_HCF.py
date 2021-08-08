a,b=map(int,input().split())

#hcf is highest number that divides all numbers.

for i in range(1,min(a,b)+1):
    if(a%i==0 and b%i==0):
        hcf=i

print(hcf)