def add(x , y):
    return x+y
def sub(x , y):

    return x-y
def mul(x , y):

    return x*y
def div(x , y):

    return x/y
print("calculator")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
ch=int(input("enter your choice"))
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if ch==1:
    print(num1 ,"+", num2, "=", add(num1,num2))
elif ch==2:
    print(num1 ,"-", num2, "=" ,sub(num1,num2))
elif ch==3:
    print(num1 ,"*", num2 ,"=", mul(num1,num2))
elif ch==4:
    print(num1 ,"/", num2 ,"=", div(num1,num2))


