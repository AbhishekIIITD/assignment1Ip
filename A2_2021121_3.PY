


def radixconvertor(fr,to,n):
    dec=0
    multiplier=fr**0
    value={}
    for i in range(0,10):
        value[str(i)]=i
    for i in range(10,36):
        value[chr(i+55)]=i
    
    length=len(n)-1
    while(length>=0):
        dec=dec+value[n[length]]*multiplier
        multiplier*=fr
        length-=1
    x=""
    for i in range(10,36):
        value[str(i)]=chr(i+55)
    while(dec>0):
        x=str(value[str(int(dec)%to)])+x
        dec=dec//to
    return x


    

print("1. Convert decimal to binary and vice-versa\n2. Convert decimal to hexadecimal and vice-versa \n3. Convert decimal to octal and vice-versa. \n4. Convert binary to hexadecimal and vice-versa. \n5. Convert binary to octal and vice-versa. \n6. Convert hexadecimal to octal and vice-versa. \n7. Convert number with radix A to radix B. Here A,B <= 36. ")
choice=int(input('Enter your choice : '))

if(choice==1):
    x=input("Enter the decimal number")
elif(choice==2):
elif(choice==2):
elif(choice==2):
elif(choice==2):
elif(choice==2):
elif(choice==2):