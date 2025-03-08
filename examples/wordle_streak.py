'''
Author: Kevin Zhu

Basic example of wordle implementing a streak-style game.
'''

from mynyt import Wordle

game = Wordle()

streak = 0

# game.play returns if the player won
while game.play():
    streak += 1

print(f'Good Job! You had a streak of {streak} wins!')