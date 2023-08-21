#file handling using write fumction (w)

file=open("helllo.txt","w")
w="hello uttu\n"

l=["This is 1st line\n",
   "This is 2nd line\n",
   "This is 3rd line"]

file.write(w)
file.writelines(l)
file.close()
