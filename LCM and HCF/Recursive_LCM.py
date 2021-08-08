def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)

#since, hcf*lcm=x*y
#therefore, lcm=(x*y)/hcf
x,y=map(int,input().split())
print((x*y)//hcf(x,y))