'''
Author: Kevin Zhu

Basic example of wordle implementing a streak-style game.
'''

from mynyt import Wordle
import time

game = Wordle()

print('Welcome to Survive Wordle!')
time.sleep(2)

ROUNDS = 5
print(f'The aim is to win {ROUNDS} consecutive rounds of Wordle.')
time.sleep(2)

print(
'''Each round, you must guess a 5-letter word within 6 attempts.
When you guess the word, you will be given a color-coded result with the following key:

- Green is the correct letter in the correct spot
- Yellow is the correct letter but it is in a different spot
- Gray/White means that the letter is not in the word.
'''
)
time.sleep(5)

print('Begin!\n')
time.sleep(1)

for i in range(ROUNDS):
    print(f'Round #{i + 1}\n')
    # game.play returns if the player won
    if not game.play():
        break

i += 1

if i == ROUNDS:
    print('Good Job! You Won!')

else:
    print('Oh no, you lost!')