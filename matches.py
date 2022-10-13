a=input("s1=")
b=input("s2=")
d=0
for i in range (len(a)):
    for j in range (len(b)): 
        if(a[i]==b[j]):
            d+=1
print(d)        
