def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if list1[mid] < ele:
            low = mid + 1
        elif list1[mid] > ele:
            high = mid - 1
        else:
            return mid+1
    return -1
n=int(input("enter the number of elemets : "))
list1=[]
for i in range(0,n):
    list1.append(int(input("enter the elements : ")))
print("the array is :")
for i in range(0,n):
    print(list1[i])
ele=int(input("enter the elemet to be searched : "))
result = binary_search(list1, ele)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")
