#a and p of rectangle
def ap():
    l= float(input("Enter the length: "))
    b= float(input("Enter the breadth: "))
    a= l*b
    p = 2*(l+b)
    if(a >p):
        print("area is greater than perimeter")
    else:
        print("perimeter is greater than area")
ap()