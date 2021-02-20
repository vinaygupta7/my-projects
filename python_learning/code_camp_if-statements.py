is_Male = False
is_Tall = True 

if is_Male:
    print("You are a male")
else:
    print("You are not a male")

if is_Male and is_Tall:
   print("You are a tall male." )
elif is_Male and not(is_Tall):
   print("You are a short  male.")
elif not(is_Male) and is_Tall:
   print("You are not a male but you are tall")
else:
   print("You are neither male nor tall")  
