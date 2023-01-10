# this file represents the interface to the user when counting birds
from typing import Dict
import time
import datetime

# ask the user how long she would like to count birds

input_dur = input('Hello dear bird friend! \nHow long would you like to count birds? \n\nAnswer in Minutes: ')
try:
    duration = float(input_dur)
    #TODO: check for negative numbers!
except:
    print('I am sorry, this is not a number!')
    exit()

#TODO: complete list with birdlife catalogue
birds: dict[str, int] = {'AMSEL': 0,
                         'KOHLMEISE': 0,
                         'TANNENMEISE': 0,
                         'BLAUMEISE': 0,
                         'TAUBE': 0,
                         'SPERLING': 0,
                         'BUNTSPECHT': 0,
                         'GRUENFINK': 0,
                         'DROSSEL': 0,
                         'UHU': 0,
                         'STIEGLITZ': 0}

# now implement the timer: add the duration to the time now and use it for an while loop
time_quit = time.time() + duration * 60 # in seconds
print("Time is running, let's watch out for birds!")
while time_quit > time.time():

    bird = input('Which bird do you see?\n').upper()
    #TODO: check if positive integer:
    try:
        cnt = int(input('How many of them?\n'))
        if cnt < 1:
            print('Not a positive integer. Nothing added.')
            continue
    except:
        print('Not an integer. Nothing added.')
        continue

    if bird not in birds.keys():
        print(f'The bird {bird} is not yet in the catalogue. Do you want to add it [y]/n?')
        if input().upper() == 'N':
            print("Bird not added.")
        else:
            birds[bird] = cnt
            print('Bird added to the catalogue.')
    else:
        birds[bird] = cnt
        print('Bird added to the catalogue.')


print('Time is up! \nThe result of today\'s count is:\n')
for k in birds:
    if birds[k]>0: print(k, birds[k])


#TODO: add result to database including a date
# if date exists, ask to overwrite