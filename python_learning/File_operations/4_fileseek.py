newfile=open('new_file.txt','r')
newfile.seek(3)
print (newfile.read())
print (newfile.tell())