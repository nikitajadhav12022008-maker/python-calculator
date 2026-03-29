#python based calculator:
#using functions:
def calculator():
    op = input("enter a operation(+,-,*,/):")
    a = int(input("enter 1st number:"))
    b = int(input("enter 2nd number:"))
    #checks operation by using conditional statements:
    if(op == "+"):
        print(a+b)
    elif(op == "-"):
        print(a-b)
    elif(op == "*"):
        print(a*b)
    elif(op == "/"):
        if(b != 0):
            print(a/b)
        else:
            print("error:division by zero")
    else:
        print("invalid operation please try again !!!!")
#function calling:
calculator()
