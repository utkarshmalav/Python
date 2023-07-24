#use of continue in python

l=[2,3,4,5,6,7,8,9,10,11,12,13]

for i in l:
    if(i%3==0):
        continue
    elif(i%2==0):
        print(i," is Even")
    else:
        print("NONE",i)
print("Done")
