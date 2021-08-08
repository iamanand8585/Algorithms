def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)

x,y=map(int,input().split())
print(hcf(x,y))