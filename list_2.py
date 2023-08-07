# list functions

#repitation
l1=[1,10.0]
l2=l1*3
print(l2)

#concatination
l3=l1+l2
print(l3)

#iterating
for l4 in l1:
    print(l4)

#membership
print(1 in l2)

#adding element in list
l4=[]
n=int(input("Enter no of elements : "))

for i in range(0,n):
    l4.append(input("Enter number : "))
for i in l4:
    print(i,end=" ")
print("\n")
l4.remove('1')
print(l4)
print(min(l4))
print(max(l4))