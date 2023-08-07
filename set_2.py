# set function

s1={1,2,3}
s2={5,2,0}

print(s1.intersection(s2))

print(s1.union(s2))

print(s1.symmetric_difference(s2))

s1.update(s2)
print(s1," & ",s2)

l1=[10,20]
s1=set(l1)
print(s1)