import sys
import random

#Check for command line arguments
if len(sys.argv) < 2 :
    print ("Please supply a flashcard file.")
    exit(1)

# Input Flashcard file
flashcard_filename = sys.argv[1]
f = open(flashcard_filename, "r")

# Setup Empty Dictionary
question_dict = {}

for line in f:
    entry = line.strip().split(",")
    question = entry[0]
    answer = entry[1]
    question_dict[question] = answer

f.close()


print ("FlashCard Quizzer !!!")
print ("At any time, type 'quit' to QUIT")
print ("")

questions = list(question_dict.keys())

while True:
    question = random.choice(questions)
    answer = question_dict[question]

    print ("Question: " + question)
    user_input = str(raw_input("Your guess: "))

    if user_input == 'quit':
        print ("Thanks for playing!")
        break
    elif user_input == answer:
        print ("Correct.")

    else:
        print ("Sorry the answer was : " + answer)
