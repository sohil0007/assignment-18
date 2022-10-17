a=("name",input("name:"))
b=("age",input("age:"))
c=("gender",input("gender:"))

d1={}
for k,v in a,b,c:
    d1[k]=v

print(d1)