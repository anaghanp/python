binary=int(input("enter the number"))
length=len(str(binary))
number=-1
for i in range(0,length):
    number=(number)+2**i
print(number)