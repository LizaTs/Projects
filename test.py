import random

# Initializing data
tools = ["rock", "paper", "scissors"]
user = input("Please insert a tool: Rock, Paper or Scissors\t ").lower()
computer = random.choice(tools)

def play(user,computer): # Defining rules
	if user == computer:
		return "You chose {}, opponent chose {}. \nIt's a tie!".format(user, computer)
	elif (user == tools[0] and computer == tools[2]) or (user == tools[1] and computer == tools[0]) or (user == tools[2] and computer == tools[1]):
		return "You chose {}, opponent chose {}. \nYou win!".format(user, computer)
	else:
		return "You chose {}, opponent chose {}. \nYou lose!".format(user, computer)

while True:
	if user in tools:
		print(play(user, computer)),"\n"
		answer = input("Do you wanna play again? yes/no\n")
		if answer == "yes":
			user = input("Please insert a tool: Rock, Paper or Scissors\t ").lower()
			computer = random.choice(tools)
			play(user,computer)
		elif answer == "no":
			print("Game over")
			break
	else:
		print("Input incorrect")
		user = input("Please insert a tool: Rock, Paper or Scissors\t ").lower()
		computer = random.choice(tools)
		play(user, computer)