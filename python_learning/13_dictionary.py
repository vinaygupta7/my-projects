person = {

    'first_name': 'Vinay',
     'last_name': 'Gupta',
     'age': 30,
     'city': "Delhi"
}

print person['first_name']
print person['age']

person ['age']=31

print person
print (len(person))

##Unordered

for item in person:
    print item



del(person['city'])

print person
print (len(person))

print (str(person))
print (type(person))

print person.get('city')


print person.items()

print person.keys()


