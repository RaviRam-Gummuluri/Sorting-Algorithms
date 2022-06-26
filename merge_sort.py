from audioop import reverse


def merge_sort(arr):
    if(len(arr)<=1):
        return
    mid=len(arr)//2
    l_arr=arr[:mid]
    r_arr=arr[mid:]
    merge_sort(l_arr)
    merge_sort(r_arr)
    i=0
    j=0
    k=0
    while i<len(l_arr) and j<len(r_arr):
        if l_arr[i]<r_arr[j]:
            arr[k]=l_arr[i]
            i+=1
        else:
            arr[k]=r_arr[j]
            j+=1
        k+=1
    while(i<len(l_arr)):
        arr[k]=l_arr[i]
        i+=1
        k+=1
    while(j<len(r_arr)):
        arr[k]=r_arr[j]
        j+=1
        k+=1
    return arr

n=int(input("enter number of elements to sort : "))
a=[]
for x in range(0,n):
    a.append(int(input("enter the number : ")))
s=int(input("enter 0 for sorting in ascending and 1 for sorting in descending : "))
if s==0:
    merge_sort(a)
elif s==1:
    merge_sort(a).reverse()
else:
    print("you must enter only 0 or 1 for ascending and descending respectively.")
print(a)