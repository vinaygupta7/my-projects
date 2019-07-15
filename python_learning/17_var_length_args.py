#*args
def print_users(user, *users):
    print ("First user argument is: ", user)

    for user in users:
        print ('user received from variable lengths arguments:', user)

print_users('vinay', 'vijay ', 'sanju', 'raman', 'nishant')
print ('****************************************************************************')
print ('***************************KWARGS EXAMPLE***********************************')
#**kwargs available as dictionary

def print_keyargs(arg1, arg2,*args, **kwargs):
    print ('First normal argument : ' + str(arg1))
    print ('Second normal argument : ' + str(arg2))
    print ('Non Keyworded argument : ' + str(args))
    print ('Keyworded argument : ' + str(kwargs))

print_keyargs(1,2,3,4,name='vinay', age='30', Country='India' )