print("enter four roll numbers")

l1=[]
i=1

while i<=4:
    l1.append(int(input()))
    i+=1

print("enter four names")

l2=[]
t=1

while t<=4:
    l2.append(input())
    t+=1

d1={}

for k in l1:
    for v in l2:
        d1[k]=v
        l2.remove(v)
        break
    
print(d1)   
