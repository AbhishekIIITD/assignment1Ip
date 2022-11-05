
def diffrentiate(listofexpo,value):
    res=0
    for i in listofexpo:
        res=res+i*(value**(i-1))
    return res

def fx(listofexpo,value):
    res=0
    for i in listofexpo:
        res=res+(value**i)
    return res

def newton_rapthen(listofexpo,x0):
    threshold=0.0001
    if diffrentiate(listofexpo,x0)==0:
        return 0
    x=(1-fx(listofexpo,x0)/diffrentiate(listofexpo,x0))
    while(x-x0>threshold):
        x0=x
        x=(1-fx(listofexpo,x0)/diffrentiate(listofexpo,x0))
    return x


listofexpo=[]
no_of_terms=int(input("Enter the number of terms : "))
for i in range(0,no_of_terms):
    a=float(input("Enter the exponent value : "))
    listofexpo.append(a)
print(newton_rapthen(listofexpo,1))