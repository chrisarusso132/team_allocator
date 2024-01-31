'''
Program: teamSelectorV3.py
1/15/2024

Side project idea created from the book "Beginner's Step-By-Step Coding Course" (page 120)

This program will simplify the process of picking, or allocating, teams. Afterwords it will offer the user to re-shuffle the teams and captains. Once the user is satisfied, they will have an option to play again.

I began writing the idea from scratch in a notebook to attempt to clarify the steps I needed to do. Eventually I began writing out the code here. I completed a rough draft of the code using the book, online, and chatGPT, as resources but was missing the re-shuffle features, play again feature, and functions for modularity. I went back to the notebook and drew an image of the steps the app should take and where functions should connect and call each other. I created a new file and began with one function at a time and kept testing to make sure it worked. Using chatGPT I was able to solve issues where I was stuck and finally finished the code on 1/18/2024
'''



import random
import time

# Welcome message placed outside of function so it does run again when user decides to replay.
print("Welcome to Team Allocator!")

# Definition of startGame() function to play the game or exit
def startGame():
	# While loop to make sure user inputs only a 1 or 2
	while True:
		play = input("Please enter 1 to START.\nOr enter 2 to QUIT.\nEnter choice here >> ")
		if play == "1":
			print("\nStarting program:")
			time.sleep(1)
			break
		# If player inputs 2, output farewell message and exit() app
		elif play == "2":
			print("Have a good day!")
			time.sleep(2)
			exit()
		# Handles empty input
		elif play == "":
			print("Please enter a valid choice.\n")
		# Handles invalid input
		else:
			print("Please enter a valid choice.\n")

# Definition of inputPlayers() function to create a list of players
def inputPlayers():
	# Empty array that the user will fill
	playerNames = []
	# While loop where the user inputs names of players
	while True:
		name = input("Enter player name. When finished please enter '2' >> ")
		# Input 2 to break the loop and move to the next block of code
		if name == "2":
			print("\nRandomizing teams. One Moment...\n")
			time.sleep(2)
			break
		# Handles empty input
		elif name == "":
			print("Please enter a valid choice.\n")
		else:
			# Add the entered name to the list of player names
			playerNames.append(name)
	# Return the list of player names
	return playerNames
# Definition of randomizer() function to shuffle the playerNames and create two teams and then returns the variavles
def randomizer(playerNames):
	random.shuffle(playerNames)
	''' Creates variable team1
	1. Takes the array playerNames
	2. : Slices the list. Since there is nothing prior :, then it slices from 0 onwards
	3. len(playerNames) takes the variable and returns the length (number of elements) in the list.
	4. //2 Divides the array length by 2 and returns a digit referring to where to stop the slice
	'''
	team1 = playerNames[:len(playerNames)//2]
	''' Similarly, this part of the code extracts elements from the middle index (length divided by 2) up to the end of the list. This creates team2 with the second half of the elements.
	'''
	team2 = playerNames[len(playerNames)//2:]
	return team1, team2

# Definition of randomCaptain() function. Chooses two captains from its appropriate teams and returns the variables
def randomCaptain(team1, team2):
	captain1 = random.choice(team1)
	captain2 = random.choice(team2)
	return captain1, captain2

# Definition of results() functions. Displays the results to the user
def results(team1, team2, captain1, captain2):
	print("Here are your curated teams:\n")
	# Display Team One results
	print("Team One:")
	print("Captain:", captain1)
	for player in team1:
		print(player)
	# Display Team Two results
	print("\nTeam Two:")
	print("Captain:", captain2)
	for player in team2:
		print(player)
	# Add extra line for better readability
	print()

# Definition of teamShuffle() function. Asks if user wants to re-shuffle the current players to create new team1 and team 2 variables
def teamShuffle(playerNames, team1, team2, captain1, captain2):
	while True:
		shuffle = input("Enter 1 to RE-SHUFFLE your current PLAYERS.\nEnter 2 to continue to the next step >> ")
		# If user chooses to shuffle, randomize teams and captains
		if shuffle == "1":
			team1, team2 = randomizer(playerNames)
			captain1, captain2 = randomCaptain(team1, team2)
			# Display the newly shuffled teams and captains
			results(team1, team2, captain1, captain2)
		# If user chooses 2, break out of the loop
		elif shuffle == "2":
			print()
			break
		#Handles empty input
		elif shuffle == "":
			print("Please enter a valid choice.")
		# Handles invalid input
		else:
			print("Please enter a valid choice.")
	# Return the updates teams, captains, and user's choice
	return team1, team2, captain1, captain2, shuffle

# Definition of captainShuffle() function. Asks user if they want to re-shuffle the captains of the current teams
def captainShuffle(team1, team2):
	while True:
		newCaptains = input("Enter 1 to RE-SHUFFLE your CAPTAINS for your current teams?\nEnter 2 to continue to the next step >> ")
		# If user inputs 1, randomly select new captains for appropriate teams
		if newCaptains == "1":
			captain1, captain2 = randomCaptain(team1, team2)
			# Display the new captains
			results(team1, team2, captain1, captain2)
		# If user inputs 2, break out of the loop
		elif newCaptains == "2":
			print()
			break
		# Handles empty input
		elif newCaptains == "":
			print("Please enter a valid option.")
		# Handles invalid inputs
		else:
			print("Please enter a valid option.")
	# Retrun the new captains
	return captain1, captain2

# Definition of newTeam() function to ask user if they want to play again
def newTeam():
	newStart = input("Would you like to play again?\nEnter 1 to play again\nEnter 2 to QUIT. >> ")
	# If user inputs 1, restart the program
	if newStart == "1":
		main()
	# If user inputs 2, exit the program
	elif newStart == "2":
		print("Thank you for using Team Allocator!")
		time.sleep(2)
		exit()
	# Handles empty inputs
	elif newStart == "":
		print("Please enter a valid choice.\n")
	# Handles invalid inputs
	else:
		print("Please enter a valid choice.\n")

# Definition of main() function
def main():
	# Calls the startGame() function
	startGame()
	# Input player names from inputPlayers() function
	playerNames = inputPlayers()
	# Randomize teams and selects captains from appropriate functions
	team1, team2 = randomizer(playerNames)
	captain1, captain2 = randomCaptain(team1, team2)
	# Calls results() function to display teams
	results(team1, team2, captain1, captain2)
	# Reshuffle teams and captains based on user input
	team1, team2, captain1, captain2, shuffle = teamShuffle(playerNames, team1, team2, captain1, captain2)
	# Calls the captainShuffle() function to reshuffle captains
	captainShuffle(team1, team2)
	# Calls newTeam() function to start a new team allocation or exit program
	newTeam()

if __name__ == '__main__':
	main()