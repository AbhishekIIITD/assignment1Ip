def discounted_price(price1=0,price2=0,price3=0,discount=0):
    total_price=price1+price2+price3
    discountprice=total_price*(discount/100)
    return total_price-discountprice
    
name=input("Enter your name : ")
print("----------WELCOME TO OUR SHOP----------")
price1=float(input("Enter the price of ITEM_1 : "))
price2=float(input("Enter the price of ITEM_2 : "))
price3=float(input("Enter the price of ITEM_3 : "))
print("--------------Please provide the discounts of saver packs---------------")
superdiscount1=float(input("Enter the discount for saver pack 1 : "))
superdiscount2=float(input("Enter the discount for saver pack 2 : "))
superdiscount3=float(input("Enter the discount for saver pack 3 : "))
print("Hello ",name," sir !")
print("Your Catalog is : ")
print("Item             ","Discount              ","price   ")
print("Item1            ","0                     ",price1)
print("Item2            ","0                     ",price2)
print("Item3            ","0                     ",price3)
print("Saver-1          ",superdiscount1,"                 "  ,discounted_price(price1,price2,discount=superdiscount1))
print("Saver-2          ",superdiscount2,"                 "  ,discounted_price(price1,price3,discount=superdiscount2))
print("Saver-3          ",superdiscount3,"                 "  ,discounted_price(price2,price3,discount=superdiscount3))
print("Saver-3          ","28%              ","    "  ,discounted_price(price1,price2,price3,discount=28))
print()
print()
print("-----------------ThankYou for shopping with us ---------------------")











