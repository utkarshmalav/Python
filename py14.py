#append use in python to take input from user and store in list

l=list()
a=int(input("Enter list size : "))
print("Enter the elements : ")
for i in range (0,a):
    l.append(int(input()))
print(l)
