#Comparison operators

import operator as op
a=10
b=15
print(a,"is Greater then ",b,":",end=" ")
print(op.gt(a,b))

print(a,"is Less then ",b,":",end=" ")
print(op.lt(a,b))

print(a,"is Greater & Equal to ",b,":",end=" ")
print(op.ge(a,b))

print(a,"is Less & Equal to ",b,":",end=" ")
print(op.le(a,b))

print(a,"is Equal to ",b,":",end=" ")
print(op.eq(a,b))

print(a,"is Not-Equal to ",b,":",end=" ")
print(op.ne(a,b))

print(a,"is ",b,":",end=" ")
print(a is b)
    
print(a,"is not ",b,":",end=" ")
print(a is not b)

