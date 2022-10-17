a=("name",input("name:"))
b=("age",input("age:"))
c=("gender",input("gender:"))

d1={}
for k,v in a,b,c:
    d1[k]=v

D = {}
t=1
for e in d1:
    i = {e:d1[e]}
    D[t]=i
    t+=1

print(D)    
       