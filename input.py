# this file represents the interface to the user when counting birds
from typing import Dict

# ask the user how long she would like to count birds

input_dur = input('Hello dear bird friend! \nHow long would you like to count birds? \n\nAnswer in Minutes: ')
try:
    duration = float(input_dur)
    #TODO: check for negative numbers!
except:
    print('I am sorry, this is not a number!')
    exit()

#TODO: implement timer
print("Time is running, let's watch out for birds!")

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

bird = input('Which bird do you see?\n').upper()
#TODO: check if positive integer:
cnt = int(input('How many of them?\n'))

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


#print("You saw ", cnt, bird)
print('The result of today\'s count is:\n', birds)

#TODO: add result to database including a date
# if date exists, ask to overwrite