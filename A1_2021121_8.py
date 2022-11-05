cost=int(input("Enter the inital cost : "))
initialcost=cost
year=0
moneyperkm=50
value=6000*moneyperkm
depreciationrate=int(input("Enter the depreciation rate : "))
depreciation=cost*(depreciationrate/100)
maintainance=cost*(1/100)

while(value<cost and year<15):
    cost=cost-(maintainance + depreciation)
    moneyperkm=moneyperkm + moneyperkm*(10/100)
    value=moneyperkm*6000





    if(year>5):
        maintainance=maintainance + maintainance*(50/100)
    else:
        maintainance=maintainance + initialcost*(1/100)
    
    year+=1

print("Sell the car after" ,year,"years")

