import random
number = random.randint(1,10)
point = 5
player_name = input("Hello there!\nWelcome to number guessing game.\n"
                    "You lose a point for every incorrect guess you make.\n"
                    "You have 5 tries to correctly guess the number I am thinking about.\n"
                    "Let's Begin!. What should I call you?")
number_of_guesses = 0
print ('okay! '+  player_name+ ' I am thinking about a number between 1 and 10. What is the number:')
while number_of_guesses < 5:
    guess = int (input())
    number_of_guesses +=1
    if guess < number: 
        print('You guessed too low! Guess again:')
    if guess > number: 
        print('You guessed too high! Guess again:')
    if guess == number: 
        break        
