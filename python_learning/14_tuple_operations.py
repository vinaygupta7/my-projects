tup=("Hadoop","Python","Android","Data Science",200000)

print(len(tup))
print (max(tup))
print (min(tup))

print (sorted(tup))
print (tup)
print (tup[::-1])

#Mutable  List Immutable tuple
tup1 = ([0,1,2],[2,3,4],[6,7,8])
tup1[0][1] = "updated"

print (tup1)
print (list(tup1))

for item in tup1:
    print ("\n")
    print tuple(item)
    print item