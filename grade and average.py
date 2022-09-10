s1=int(input("enter s1 marks="))
s2=int(input("enter s2 marks="))
s3=int(input("enter s3 marks="))
s4=int(input("enter s4 marks="))
t=s1+s2+s3++s4
print("total=",t)
if(t>=350):
    print("S grade")
    if(t>=300 and t<350):
        print("A grade")
        if(t>=250 and t<300):
            print("B grade")
            if(t<250):
                print("fail")
average=t/4
print("average=",average)
                

