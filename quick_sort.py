n=int(input("enter number of elements to sort : "))
a=[]
for x in range(0,n):
    a.append(int(input("enter the number : ")))
s=int(input("enter 0 for sorting in ascending and 1 for sorting in descending : "))
sel_sort(a,n,s)
print(a)