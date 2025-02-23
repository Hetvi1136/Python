#check whether triangle
a=int(input("enter angle1: "))
b=int(input("enter angle2: "))
c=int(input("enter angle3: "))
def triangle(): 
    if(a+b+c==180):
        print("it is triangle")
    else:
        print("it is not a triangle")
triangle()        