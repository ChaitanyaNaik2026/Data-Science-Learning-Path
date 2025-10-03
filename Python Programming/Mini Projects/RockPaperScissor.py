#Rock Paper Scissor Game


import random #choosing random out of a list
#Function Creation
def get_choice():     #semi colon at the end of function

    player_choice = input("Enter a choice(rock,paper,scissors): ") #Input Function
    computer_option = ["rock","paper","scissor"] #list Creation
    computer_choice = random.choice(computer_option)
    choices = {"player": player_choice, "computer":computer_choice} #Dictionary with key value pair
    return choices


def cheak_win(player, computer):
    print("You chose " + player, "computer chose " + computer)  # print choices
    
    # conditional                    #else if or elif  for if else statements
    if player == computer:
        return "Its a tie"
    elif player == "rock":
      if computer == "scissors":
        return "you win"
      else:
        return "you lose"
    
    elif player == "scissor":
      if computer == "paper":
        return "you win"
      else:
        return "you lose"
      
    elif player == "paper":
      if computer == "rock":
        return "you win"
      else:
        return "you lose"
      
    
    

choices = get_choice()
result = cheak_win(choices["player"],choices["computer"])

print(result)

    
    