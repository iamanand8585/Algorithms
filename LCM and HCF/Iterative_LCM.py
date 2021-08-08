#lcm is lowest number that is divisible by all the numbers.
def lcm(a,b):
    greatest=max(a,b)
    while(True):
        if(greatest%a==0 and greatest%b==0):
            lcm=greatest
            break
        greatest+=1
    return lcm


x,y=map(int,input().split())
print(lcm(x,y))