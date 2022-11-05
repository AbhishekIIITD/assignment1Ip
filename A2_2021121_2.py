def matrixmul(a,b):
    res=[]
    for i in range(0,len(a)):
        res.append([])
    for i in range(0,len(a)):
        for j in range(0,len(b[i])):
            element=0
            row=i
            col=j
            while(row<len(a))



vertices=int(input("Enter the no. of vertices : "))
x=[int(i) for i in input().split()]
y=[int(i) for i in input().split()]
z=[int(i) for i in input().split()]
q=int(input("Enter the no. of transformations : "))
for i in range(0,q):
    query=input()
