n=int(input("Enter the number of elements:"))
i=1
list1=list()
list2=list()
while(i<=n):
    element=int(input("enter an element of list:"))
    list1.append(element)
    i=i+1
print(list1)
for i in list1:
    if i not in list2:
        list2.append(i)
        print(list2)
