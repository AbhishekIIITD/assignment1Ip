def Right_angled_triangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()



def Isosceles_triangle(n):
    for i in range(1,n+1):
        for j in range(0,n-i):
            print(end=" ")
        count =1
        for j in range(1,i+1):
            print(j,end="")
            count+=1
        for j in range(1,i):
            print(count,end="")
            count=count+1
        print()



def Kite(n):
    for i in range(1,2*n):
        if(i<n+1):
            for j in range(0,n-i):
                print(end=" ")
            count =1
            for j in range(1,i+1):
                print(j,end="")
                count+=1
            for j in range(1,i):
                print(count,end="")
                count=count+1
        else:
            for j in range(0,i-n):
                print(end=" ")
            count=1
            for j in range(1,2*n-i+1):
                print(j,end="")
                count+=1
            for j in range(1,2*n-i):
                print(count,end="")
                count+=1
        print()
            


def half_kite(n):
    for i in range(1,2*n):
        if(i<n+1):
            for j in range(1,i+1):
                print(j,end="")
            
        else:
            for j in range(1,2*n-i+1):
                print(j,end="")
                
        print()

        
        
        

def X(n):
    for i in range(1,n):
        for j in range(1,i):
            print(end=" ")
        count=1
        for j in range(1,n-i+2):
            print(j,end="")
            count+=1
        for j in range(0,n-i):
            print(count,end="")
            count+=1
        print()  
    Isosceles_triangle(n)        

x=input()
n=int(input())
if(x=="Right-angled triangle"):
    Right_angled_triangle(n)
elif x=="Isosceles triangle" :
    Isosceles_triangle(n)
elif(x=="Kite"):
    Kite(n)
elif(x=="Half Kite"):
    half_kite(n)
elif(x=="X"):
    X(n)
else:
    print("wrong input")
