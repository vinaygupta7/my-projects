i = 1 
while i <= 10:
      print(i)
      i += 1

print ("Done with loop") 

secret= "HELP"
guess= ""
count = 0
limit = 3
limit_reached = False

while guess != secret and not (limit_reached):
      if count < limit:
        guess = input("Guess the word: ")
        count += 1
      else:
         limit_reached = True


if limit_reached:
      print ("You loose! out of limit")    
else:
      print("you win")
