#check divisible by 10
a=int(input("enter a number: "))
def dby10(): 
    if(a%10==0):
        print(a,"is divisible by 10")
    else:
        print(a,"is not divisible by 10")
dby10()        