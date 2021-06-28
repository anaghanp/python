n=int(input("enter the number of elements"))
arr=[]
def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
             arr[j],arr[j+1]=arr[j+1],arr[j]
for i in range(0,n):
    arr.append(int(input("enter the elements:")))
print("array is:")
for i in range(0,n):
    print(arr[i])

bubblesort(arr)
print("soerted array is:")
for i in range(len(arr)):
        print(arr[i])
