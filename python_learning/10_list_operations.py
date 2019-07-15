list=['Hadoop','python','Android','Java']
print (list[1])
print (list[0:2])
print(list[-1])

#CONCAT
print (list+['REACT','Angular','JS'])

#REPT
print (list*3)

#Membership
print ('Hadoop' in list, 'JS' in list)

#Update
list[3]="C++"
print (list)

#DELETE
del(list[2])
print (list)

#pop
print (list.pop(2))
print (type(list))

#List_Comprhension
print ([x**2 for x in [1,2,3,4,5]])

#iNSERTION
list.insert(1,"Scripting")
list.insert(4,'Android')
print(list)

print(sorted(list))

#print Reverse
for course in list[::-1]:
    print course

#print length

print(len(list))