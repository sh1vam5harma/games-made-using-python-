# Date- 8/27/2022
# Coder- Shivam S.
# Stack- Python v3
# Project Name- Number Guessing Game

import random 

n = random.randint(1,10)

guess = int(input("Enter an integer ranging from 1 to 10: "))

while n != "guess":
  print

  if guess < n:
    print("Guess is low.")
    guess = int(input("Enter an integer from 1 to 10: "))

  elif guess > n:
      print("Guess is high.")
      guess = int(input("Enter an integer from 1 to 10: "))

  else: 
      print("You guessed it!")
      break
      print
    
