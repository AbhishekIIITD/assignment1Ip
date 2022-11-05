
from re import S


n=int(input("Enter the number of students : "))
for i in range(0,n):
    shape=int(input(
        '''
1. Square
2. Rectangle
3. Rhombus
4. Parallelogram
5. Circle
6. Cube
7. Cuboid
8. Right circular cone
9. Hemisphere input
10. Sphere
11. Solid cylinder 
12. Hollow cylinder
13. Exit from the menu\nChoose a shape : ''',
))
    if(shape<=5):
        perimeter=0
        area=0
        if(shape==1):
            side=int(input("Enter the side : "))
            perimeter=4*side
            area=side*side
        elif(shape==2):
            length=int(input("Enter the length : "))
            breadth=int(input("Enter the breadth : "))
            perimeter=2*(length+breadth)
            area=length*breadth
        elif(shape==3):
            side=int(input("Enter the side : "))
            d1=int(input("Enter the diagnol d1 : "))
            d2=int(input("Enter the diagnol d2 : "))
            perimeter=4*side
            area=(d1*d2)/2
        elif(shape==4):
            length=int(input("Enter the length : "))
            breadth=int(input("Enter the breadth : "))
            height=int(input("Enter the hieght : "))
            perimeter=2*(length+breadth)
            area=length*height
        elif(shape==5):
            radius=int(input("Enter the radius : "))
            perimeter=2*3.14*radius
            area=3.14*(radius**2)
        print(end="\n")
        print("The Perimeter of your shape is : ",perimeter)
        print("The area of your shape is : ",area)
    else:
        csa=0
        tsa=0
        volume=0

        if(shape==6):
            side=int(input("Enter the side : "))
            csa=4*side*side
            tsa=6*side*side
            volume=side*side*side
        elif(shape==7):
            length=int(input("Enter the length : "))
            breadth=int(input("Enter the breadth : "))
            height=int(input("Enter the hieght : "))
            csa=2*(length*breadth +height*length)
            tsa=2*(length*breadth +height*length +breadth*height)
            volume=length*breadth*height
        elif shape==8:
            l=int(input("Enter the slant height : "))
            r=int(input("Enter the radius : "))
            h=int(input("Enter the height : "))
            csa=3.14*r*l
            tsa=csa+ (3.14*r**2)
            volume=(1/3)*(3.14*(r**2)*h)
        elif shape==9:
            r=int(input("Enter the radius : "))
            csa=2*3.14*(r**2)
            tsa=3*3.14*(r**2)
            volume=(2/3)*(3.14*r**3)
        elif shape==10:
            r=int(input("Enter the radius : "))
            csa=4*3.14*(r**2)
            tsa=4*3.14*(r**2)
            volume=(4/3)*(3.14*r**3)
        elif shape==11:
            r=int(input("Enter the radius : "))
            h=int(input("Enter the height : "))
            csa=3.14*r*h
            tsa=csa+ 2*(3.14*r**2)
            volume=(3.14*(r**2)*h)
        elif shape==12:
            r1=int(input("Enter the inner radius : "))
            r2=int(input("Enter the outer radius : "))
            h=int(input("Enter the height : "))
            csa=2*3.14*h(r1+r2)
            tsa=csa + 2*3.14*(r2-r1)
            volume=3.14*(r2-r1)*h
        elif shape==13:
            break
        else:
            print("wrong input chosen")
            break
        print("The csa of your shape is : ",csa)
        print("The tsa of your shape is : ",tsa)
        print("The volume of your shape is : ",volume)
            

            

        



    
   