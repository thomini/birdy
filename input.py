# this file represents the interface to the user when counting birds
from typing import Dict

# ask the user how long she would like to count birds

input_dur = input('Hello dear bird friend! \nHow long would you like to count birds? \n\nAnswer in Minutes: ')
try:
    duration = float(input_dur)
except:
    print('I am sorry, this is not a number!')
    exit()

print("Time is running, let's watch out for birds!")

birds = {'AMSEL': 0, 'KOHLMEISE': 0}

bird = input('Which bird do you see?').upper()
cnt = input('How many of them?')

print("You saw ", cnt, bird)

