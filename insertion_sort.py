def ins_sort(arr,N,p):
    if p==0:
        for i in range(1,N):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j=j-1
            arr[j+1]=key
    elif p==1:
        for i in range(1,N):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]<key:
                arr[j+1]=arr[j]
                j=j-1
            arr[j+1]=key
    else:
        print("you must enter only 0 or 1 for ascending and descending respectively.")

n=int(input("enter number of elements to sort : "))
a=[]
for x in range(0,n):
    a.append(int(input("enter the number : ")))
s=int(input("enter 0 for sorting in ascending and 1 for sorting in descending : "))
ins_sort(a,n,s)
print(a)