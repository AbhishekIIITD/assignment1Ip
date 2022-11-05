def functionvalforx(listofcoeff,x):
    length=len(listofcoeff)-1
    res=0
    i=0
    while(length>=0):
        res=res + listofcoeff[length]*(x**(i))
        length-=1
        i+=1
    return res

def printstars(n):
    for i in range(0,n):
        print("*",end='')
    print(end='\n')


def polynomial(listofcoeff,lowerb,upperb,incrementor):
    for i in range(lowerb,upperb+1,incrementor):
        printstars(functionvalforx(listofcoeff,i))


listofcoeff=[]
print("Please provide the necessary function details : ")
degree=int(input("Enter the degree of the polynomial : "))

for i in range(0,degree+1):
    x=int(input(f"Enter the coeff{1+i} : "))
    listofcoeff.append(x)
lowerb=int(input("Enter the value of lower bound : "))
upperb=int(input("Enter the value of upper bound : "))
incrementor=int(input("Enter the steps of incrementation : "))
polynomial(listofcoeff,lowerb,upperb,incrementor)



