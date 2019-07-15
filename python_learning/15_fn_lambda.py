value= (lambda x: x*4)

print value(4)
print ('*******************************************')

#MAP
items=[1,2,3,4,5]
sqrd = list(map(lambda x: x**2, items))
print items
print ('squared value is:' )
print sqrd
print ('*******************************************')
#FILTER
num_list= range(-10 , 5)
less_zero = list(filter(lambda x: x<0, num_list ))
print num_list
print ('Filtered value is:')
print less_zero

print ('*******************************************')

#REDUCE
from functools import reduce
product = reduce((lambda x,y: x*y), [1,2,3,4])
product1 = reduce((lambda x,y: (x*2)*y), [1,2,3,4])
print product
print product1


