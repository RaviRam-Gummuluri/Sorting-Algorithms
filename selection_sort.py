def sel_sort(arr,N,p):
    for i in range(0,N):
        if p==0:
            min=i
            for j in range(i+1,N):
                if arr[min]>arr[j]:
                    min=j
            arr[i],arr[min]=arr[min],arr[i]
        elif p==1:
            max=i
            for j in range(i+1,N):
                if arr[max]<arr[j]:
                    max=j
            arr[i],arr[max]=arr[max],arr[i]
        else:
            print("you must enter only 0 or 1 for ascending and descending respectively.") 

n=int(input("enter number of elements to sort : "))
a=[]
for x in range(0,n):
    a.append(int(input("enter the number : ")))
s=int(input("enter 0 for sorting in ascending and 1 for sorting in descending : "))
sel_sort(a,n,s)
print(a)

