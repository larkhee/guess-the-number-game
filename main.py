#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
print(logo)

print('''Welcome to the number guessing game.
I'm thinking of a number between 1 and 100.''')

def diffSet():
  difficulty = input(f"Choose difficulty. Type \'easy' or \'hard'\n")
  if difficulty == 'easy':
    return 10
  elif difficulty == 'hard':
    return 5
  else:
    print(f'That is an invalid option.')
    return diffSet()

lives = diffSet()  
print(lives)
  
#Generate a random number
import random
number = random.randint(1,101)


#Answer displayed for debugging. comment it out for the actual game!
print(f'for debugging purpose, here is the correct answer: {number}')


#While loop for the game.
game_finished = False

while game_finished == False:
  print(f'You have {lives} attempts left.')
  guess = int(input(f'Make a guess \n'))
  if guess > number:
    print('Too high. Guess again')
    lives -= 1
    if lives == 0:
      game_finished = True
      print('You have expired number of attempts. You lose')
  elif guess < number:
    print('Too low. Guess again')
    lives -=1
    if lives == 0:
      game_finished = True  
      print('You have expired the number of attempts. You lose')
  else:
    print('You guessed correctly! You win')
    game_finished = True



