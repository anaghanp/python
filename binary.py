def binary_search(list1,n):
    low=0
    high=len(list1)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if list1[mid]<elem:
            low=mid+1
        elif list1[mid]>elem:
            high=mid-1
        else:
            return mid+1
        return -1
n=int(input("enter the number of elements:"))
list1=[]
for i in range(0,n):
    list1.append(int(input("enter the elements:")))
print("array is:")
for i in range(0,n):
    print(list1[i])
elem=int(input("enter the element to be searched:"))
result=binary_search(list1,elem)
if result!=-1:
    print("element present at index:",str(result))
else:
    print("element is not present in list1")

