import random
def gameplay() :
  player_choice = input("Enter your choice(rock, paper, scissors) : ")
  option = ["rock","paper","scissors"]
  computer_choice = random.choice(option)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def checkwin(player,computer):
  print(f"Player: {player},Computer: {computer}")
  if player == computer : 
    return "You tie!!"
  elif player == "rock":
    if computer == "scissors":
      return "You win!!"
    else:
      return "You lose."
  elif player == "paper":
    if computer == "rock":
      return "You win!!"
    else:
      return "You lose."
  elif player == "scissors":
    if computer == "paper":
      return "You win!!"
    else:
      return "You lose."

choices = gameplay()
result = checkwin(choices["player"],choices["computer"])
print(result)
