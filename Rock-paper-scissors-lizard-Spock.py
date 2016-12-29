import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number(name):
    # assign number to corresponding string
    if (name == "rock"):
        name = 0
    elif (name == "Spock"):
        name = 1
    elif (name == "paper"):
        name = 2
    elif (name == "lizard"):
        name = 3
    elif (name == "scissors"):
        name = 4
    else:
        name = -1 # invalid name
    return name

def number_to_name(number):
    # convert the number to corresponding string 
    if (number == 0):
        result = "rock"
    elif (number == 1):
        result = "Spock"
    elif (number == 2):
        result = "paper"
    elif (number == 3):
        result = "lizard"
    elif (number == 4):
        result = "scissors"
    else:
        print "Invalid number"
    return result

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player chooses " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_number = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses " + comp_number
    # compute difference of comp_number and player_number modulo five
    difference = (name_to_number(comp_number) - name_to_number(player_number)) % 5
    # use if/elif/else to determine winner, print winner message
    if (difference == 0):
        print "Player and computer tie!"
    elif (difference <= 2):
        print "Computer wins!"
    else:
        print "Player wins!"  

# test code
rpsls("rock")  
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")        