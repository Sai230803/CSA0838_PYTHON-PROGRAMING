a=input("s1=")
b=input("s2=")
c=0
for i in range (len(a)):
    for j in range (len(b)): 
        if(a[i]==b[j]):
            c+=1
print(c)        
