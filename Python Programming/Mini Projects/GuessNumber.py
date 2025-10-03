import random

target= random.randint(1,100)

while True:
    userChoice = input("Guess the number or Quit(Q) :")
    if(userChoice == "Q"):
      break

    userChoice= int(userChoice)
    if(userChoice == target) :
       print("Success")
       break
    elif(userChoice<target):
        print("Number less then target")
    else:
        print("Number greater than target")

print("End of Guess")

