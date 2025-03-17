import math
import cmath
def log():
    x=int(input("Enter the number:-"))
    ans=round(math.log10(x),3)
    print(ans)
def ln():
    x=int(input("Enter the number:-"))
    ans=round(math.log10(x)*2.3026,3)
    print(ans)
def sqrt():
    x=int(input("Enter the number:-"))
    if x<0:
        ans=cmath.sqrt(x)
    else:
        ans=math.sqrt(x)
    print(ans)
def pow():
    a=int(input("Enter the number:-"))
    b=int(input("Enter the power:-"))
    print(math.pow(a,b))
def add():
    a=int(input("Enter the first number:-"))
    b=int(input("Enter the second number:-"))
    print( a + b)

def subtract():
    a=int(input("Enter the first number:-"))
    b=int(input("Enter the second number:-"))
    print( a - b)

def multiply():
    a=int(input("Enter the first number:-"))
    b=int(input("Enter the second number:-"))
    print( a * b)

def divide():
    a=int(input("Enter the first number:-"))
    b=int(input("Enter the second number:-"))
    if b != 0:
        print( a / b)
    else:
        return "Cannot divide by zero!"
    
def add_complex():
    real1=int(input("Enter the real part of number 1:-"))
    img1=int(input("Enter the imaginary part of number 1:-"))
    real2=int(input("Enter the real part of number 2:-"))
    img2=int(input("Enter the imaginary part of number 2:-"))
    c1=complex(real1,img1)
    c2=complex(real2,img2)
    c=( c1 + c2)
    print(c)
    print("Modulas is ",modulus(c))
    print("Argument is ",argument(c))

def subtract_complex():
    real1=int(input("Enter the real part of number 1:-"))
    img1=int(input("Enter the imaginary part of number 1:-"))
    real2=int(input("Enter the real part of number 2:-"))
    img2=int(input("Enter the imaginary part of number 2:-"))
    c1=complex(real1,img1)
    c2=complex(real2,img2)
    c=c1-c2
    print(c)
    print("Modulas is ",modulus(c))
    print("Argument is ",argument(c))

def multiply_complex():
    real1=int(input("Enter the real part of number 1:-"))
    img1=int(input("Enter the imaginary part of number 1:-"))
    real2=int(input("Enter the real part of number 2:-"))
    img2=int(input("Enter the imaginary part of number 2:-"))
    c1=complex(real1,img1)
    c2=complex(real2,img2)
    c=(c1 * c2)
    print(c)
    print("Modulas is ",modulus(c))
    print("Argument is ",argument(c))
def divide_complex(c1, c2):
    real1=int(input("Enter the real part of number 1:-"))
    img1=int(input("Enter the imaginary part of number 1:-"))
    real2=int(input("Enter the real part of number 2:-"))
    img2=int(input("Enter the imaginary part of number 2:-"))
    c1=complex(real1,img1)
    c2=complex(real2,img2)

    if c2 != 0:
        c=(c1 / c2)
        print(c)
        print("Modulas is ",modulus(c))
        print("Argument is ",argument(c))
    else:
        return "Not possible devive by Zero"

def modulus(c):
    return(abs(c))

def argument(c):
    return(cmath.phase(c))

do_operation=True
while do_operation:
    print("what operation do you want ?")
    op=int(input("press 1 for finding logarithm\npress 2 for power calculate\npress 3 or 4 for complex addition or substraction\npress 5 or 6 for complex multiplication or division\npress 7/8/9/0 for mormal addition/subtraction/multiplication/division:-"))
    if op==1:
        log()
    elif op==2:
        pow()
    elif op==3:
        add_complex()
    elif op==4:
        subtract_complex()
    elif op==5:
        multiply_complex()
    elif op==6:
        divide_complex()
    elif op==7:
        add()
    elif op==8:
        subtract()
    elif op==9:
        multiply()
    elif op==0:
        divide()
    

    should_continue = input("Are you want any or operation? Type 'Yes' or 'No': ").lower()
    if should_continue=='no':
        do_operation=False
        print("Thank You")