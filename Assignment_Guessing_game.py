#ass 2- guessing game

import random
guessnum=random.randint(1,9)
num= int(input('Guess a number between 1 and 9: '))

while guessnum!='num':
  
   
    if num<guessnum:
             print('Guess is too low,Try again')
             num= int(input('Guess a number between 1 and 9: '))
             
    elif num>guessnum:
        print('Guess is too high,Try again')
        num= int(input('Guess a number between 1 and 9: '))
    else:
        print('****Congratulations!!Well Guessed****!!!!!!!!!!')
        break
