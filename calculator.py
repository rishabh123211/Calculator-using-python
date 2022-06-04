def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def mod(x,y):
    return x%y

def pow(x,y):
    return x**y

def sqr(x):
    return x**2

def sqrt(x):
    return x**(1/2)

def cube(x):
    return x**3

def cubeRoot(x):
    return x**(1/3)

while(True):

    print("\n\n                           WELCOME IN MY CALCULATOR                       \n")

    print("                                1.  Addition                               ")
    print("                                2.  Substration                               ")
    print("                                3.  Multiplication                               ")
    print("                                4.  Division                               ")
    print("                                5.  Divisor                               ")
    print("                                6.  Power                               ")
    print("                                7.  Square                               ")
    print("                                8.  Square Root                               ")
    print("                                9.  Cube                               ")
    print("                                10. Cube Root                               ")
    print("                                11. Exit                               \n\n")


    ch = int(input("Enter Your Choice - "))
    
    if ch == 1 :
        x = int(input("Enter First Number : "))
        y = int(input("Enter Second Number : "))
        print(x," + ",y," = ",add(x,y))

    elif ch == 2 :
        x = int(input("Enter First Number : "))
        y = int(input("Enter Second Number : "))
        print(x," - ",y," = ",sub(x,y))

    elif ch == 3 :
        x = int(input("Enter First Number : "))
        y = int(input("Enter Second Number : "))
        print(x," * ",y," = ",mul(x,y))

    elif ch == 4 :
        x = int(input("Enter First Number : "))
        y = int(input("Enter Second Number : "))
        print(x," / ",y," = ",div(x,y))

    elif ch == 5 :
        x = int(input("Enter First Number : "))
        y = int(input("Enter Second Number : "))
        print(x," % ",y," = ",mod(x,y))

    elif ch == 6 :
        x = int(input("Enter First Number : "))
        y = int(input("TO the power : "))
        print(x," ^ ",y," = ",pow(x,y))

    elif ch == 7 :
        x = int(input("Enter Number : "))
        print(x," ^ 2  = ",sqr(x))

    elif ch == 8 :
        x = int(input("Enter Number : "))
        print(x," ^ 1/2  = ",sqrt(x))

    elif ch == 9 :
        x = int(input("Enter Number : "))
        print(x," ^ 3  = ",cube(x))

    elif ch == 10 :
        x = int(input("Enter Number : "))
        print(x," ^ 1/3  = ",cubeRoot(x))

    elif ch == 11 :
        exit()

    else :
        print("Enter a valid number ")