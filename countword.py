l=[]
w=input("enter the sentence:")
str=w.split(" ")
print(str)
for i in str:
    if i not in l:
        l.append(i)
for i in range(0,len(l)):
    print("the word",l[i],"occurs",str.count(l[i]),"times")