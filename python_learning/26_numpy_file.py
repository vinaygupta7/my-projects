import numpy

arr = numpy.array([[1,2,3],[4,5]])

print (arr)


numpy.savetxt('save_26np.txt', arr, fmt='%c')

newarr = numpy.loadtxt(('save_26np.txt'))

print (newarr)


##CSV FILES
numpy.savetxt('save_26np.csv',arr,delimiter=',')

newarr1 = numpy.genfromtxt('save_26np.csv')

print (newarr1)