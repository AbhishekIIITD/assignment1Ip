def getReverse(n):
    res=0
    while(n>0):
        res=res*10+n%10
        n=n//10


    
    return res

def checkPalindrome(n):
    n=str(n)
    i=0
    j=len(n)-1
    while(i<j):
        if(n[i]!=n[j]):
            return False
        i+=1
        j-=1
    return True
def getDigitSquareSum(n,i=2):
    res=0
    while(n>0):
        res=res+(n%10)**i
        n=n//10
    return res



def checkNarcissitic(n):
    if(getDigitSquareSum(n,3)==n):
        return True
    return False

def findDigitSum(n):
    res=getDigitSquareSum(n,i=1)
    while(res//10!=0):
        res=getDigitSquareSum(res,i=1)

    return res


print('''Hello User, Welcome to the Application. Please select one of the following operations. \n1. Find reverse of a number 
2. Check whether a number is a palindrome or not. 
3. Check whether a number is a Narcissistic number or not. 
4. Find the sum of digits of a number 
5. Find the sum of squares of digits of a number. 
6. Select 6 to exit the application. 
''')


while(True):
    x=int(input("Select the operation :"))
    if(x==1):
        n=int(input("Enter the Number : "))
        print(getReverse(n))
    elif(x==2):
        n=int(input("Enter the Number : "))
        print(checkPalindrome(n))
    elif(x==3):
        n=int(input("Enter the Number : "))
        print(checkNarcissitic(n))
    elif(x==4):
        n=int(input("Enter the Number : "))
        print(findDigitSum(n))
    elif(x==5):
        n=int(input("Enter the Number : "))
        print(getDigitSquareSum(n))
    elif(x==6):
        print("Exit")
        break
    else:
        print("Wrong input , please try again")
