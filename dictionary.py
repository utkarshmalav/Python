# dictionary

d1={1:"Hello", 2:"Hl",'a':"Welcome"}

print("Keys : ",d1.keys())

print("Value : ",d1.values())

print(d1.get('a'))

newd=d1.copy()
print(newd)

print(d1.pop(1))
print(d1)

print(d1.popitem())

d2={4:"Welcome"}

d1.update(d2)
print(d1)

d1.update(5:"Hi")