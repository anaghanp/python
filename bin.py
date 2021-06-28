binary=input("enter the number")
def BinarytoDecimal(binary):
    decimal=0
    for digit in binary:
        decimal=decimal*2+int(digit)
    print("the decimal value is",decimal)