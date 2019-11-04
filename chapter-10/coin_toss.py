"""A program that was to be debugged using the tools supplied in chapter 10.
"""

import random
import time
random.seed(time.time)
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = ['tails', 'heads'][random.randint(0, 1)]  # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
