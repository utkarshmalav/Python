# Program using file handling read only (r)


#Using read():

file= open ("read.txt","r")
text=file.read()
print(text)


#using for loop:

f=open("for_loop.txt","r")
for i in f:
    print(i)


#using with statement:

with open("with.txt") as file:
    data=file.read()
print(data)


#To read ceratin no of characters...

file=open("cerain_char.txt","r")
print(file.readline(6))


#Readline()

file=open("readline.txt","r")
print(file.readline(2))
file.seek(0)                    # used to take cursor at starting
print(file.readlines())
file.close()

# split function
file=open("split.txt","r")
data=file.readline()
for line in data:
    word=line.split()
    print(word)

 
