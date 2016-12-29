# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

secret_number = 0     
attempt = 0 	  	  # number of chances to guess
				  	  # range100 default:   7
                  	  # range1000 default: 10
is_range1000 = False  # mark for range                  

def new_game():
    if(is_range1000):
        range1000()
    else:
        range100()

def range100():
    global secret_number, attempt, is_range1000
    
    attempt = 7
    is_range1000 = False
    print "New game. Range is [0,100)"
    print "Number of remaining guesses is " + str(attempt) + "\n" 
    secret_number = random.randint(0, 100)

def range1000():
    global secret_number, attempt, is_range1000
    
    attempt = 10
    is_range1000 = True
    print "New game. Range is [0,1000)"
    print "Number of remaining guesses is " + str(attempt) + "\n"
    secret_number = random.randint(0, 1000)

def input_guess(guess):
    global attempt, secret_number
    
    print "Guess was " + guess
    guess_number = int(guess)
    attempt -= 1
    
    if (guess_number == secret_number):
        print "Number of remaining guesses is " + str(attempt)
        print "Correct!\n"
        new_game()
    elif (guess_number > secret_number and attempt != 0):
        print "Number of remaining guesses is " + str(attempt)
        print "Lower!\n"
    elif (guess_number < secret_number and attempt != 0):
        print "Number of remaining guesses is " + str(attempt)
        print "Higher!\n"
    else:
        print "Number of remaining guesses is " + str(attempt)
        print "You ran out of guesses.  The number was " + str(secret_number) + "\n"
        new_game()

#create frame
frame = simplegui.create_frame("Guess the Number!", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

frame.start()
new_game()                    