n = int(input("Enter a value:"))  
temp = n  
r = 0  
while(n > 0):  
    d = n % 10  
    r = r * 10 + d  
    n= n // 10  
if(temp == r):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")  
