import os

newfile=open("new_file.txt","w")
for i in range(1,11):
 newfile.write("\n Hello!")
print (newfile.mode)
newfile.close()
