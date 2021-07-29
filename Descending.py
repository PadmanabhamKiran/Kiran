n=int(input("Enter the number of elements"))
i=1
list1=list()
while(i<=n):
    element=int(input("Enter the element of the list"))
    list1.append(element)
    print(list1)
    i+=1
list1.sort(reverse=True)
print(list1)
