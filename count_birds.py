"""
This file includes the main function (start_count) of Birdy for counting birds.

Author: Dominik Imgrüth
"""

#from typing import Dict
import time
import dataframe
from datetime import date, datetime

# a warnings filter is used, because the pandas.DataFrame.append method will be outdated soon;
# it is still running (and concat not yet working)

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# create a catalogue of pre-defined birds
# used the same birds as in the bridlife catalogue:
birds: dict[str, int] = {'AMSEL': 0,
                         'BERGFINK':0,
                         'BLAUMEISE': 0,
                         'BUCHFINK': 0,
                         'BUNTSPECHT': 0,
                         'ERLENZEISIG': 0,
                         'FELDSPERLING': 0,
                         'GIMPEL': 0,
                         'GRÜNFINK': 0,
                         'HAUBENMEISE': 0,
                         'HAUSSPERLING': 0,
                         'KLEIBER': 0,
                         'KOHLMEISE': 0,
                         'ROTKEHLCHEN': 0,
                         'STIEGLITZ': 0,
                         'TANNENMEISE': 0,
                         'TÜRKENTAUBE': 0}
def start_count(birds, standard_db):
    """
    interface for counting birds.
    the user of this function sets a time in which she records the bird she is observing in her garden or balcony
    the observations will be recorded and the user can save them to a database.
    note on counting method:
        - bird species can be observed at different times, but only the highest count is saved.
          example: if at minute 1, you record FIVE Amsel and at minute THREE Amsel,
                   the recorded number will be FIVE
        - if a species isn't in the predefined catalogue, the user is asked if she would like to add the species
    :param birds: dict, a predefined catalogue of birds (keys) and amount (values, typically = 0)
    :param standard_db: the database, where results are saved (if chosen by user)
    :return: None
    """

    # say hello and ask for name
    print('Hello dear bird friend!\nWhat is your name?')
    name = input('NAME: ').capitalize()

    # ask the user how long she would like to count birds
    # (dummy) initial condition for the while loop
    duration = -1
    # while loop is used to check that the user is providing a reasonable input (float > 0)
    while duration < 0:
        input_dur = input(f'How long would you like to count birds, {name}? \n\nAnswer in Minutes: ')
        try:
            duration = float(input_dur)
            # if negative, ask to enter again
            if duration < 0:
                print("The time is negative - this is not a time machine! \nYou can exit with '0'")
        except:
            print('I am sorry, this is not a number!')
            print('\nIf you wish to exit enter 0.\n')

    # counting makes only sense if the duration was > 0
    if duration > 0:

        # now implement the timer: add the duration to the actual time and use it for keep a while loop running
        now_sec = time.time()
        # save the time also for the database in datetime format
        now = datetime.now()

        # add the duration to the current time for the timer (while loop)
        time_quit = now_sec + duration * 60  # in seconds

        print("Time is running, let's watch out for birds!")

        while time_quit > time.time():

            # ask the user which bird she sees. birds will be written in upper case
            # also if the user likes she can abort counting with 'exit' and
            # show all birds in the standard catalogue with 'show'
            bird = input('Which bird do you see?\n (type "exit" for stop counting; "show" for inspect birds)\n').upper()

            # exit (via break) and correct duration
            if bird == 'EXIT':
                print('You stopped counting!')
                # overwrite duration:
                duration = round((time.time() - now_sec)/60,2)
                break

            # show catalogue and continue with counting
            if bird == 'SHOW':
                print(list(birds.keys())[:6])
                print(list(birds.keys())[6:12])
                print(list(birds.keys())[12:])
                continue

            # try if the amount of birds is a (positive) integer:
            try:
                cnt = int(input('How many of them?\n'))
                if cnt < 1:
                    print('Not a positive integer. Nothing added.')
                    continue
            except:
                print('Not an integer. Nothing added.')
                continue

            # if the species is not one in the catalogue (dictionary birds),
            # ask the user if she wants to include a new species
            if bird not in birds.keys():
                print(f'The bird {bird} is not yet in the catalogue. Do you want to add it [y]/n?')
                if input().upper() == 'N':
                    print("Bird not added.")
                else:
                    birds[bird] = cnt
                    print('Bird added to the catalogue.')

            # if the bird exists in the dictionary birds:
            else:
                # if the count is lower or equal to an already existing count, do not replace it
                # (only highest count is of importance)
                if birds[bird] > cnt:
                    print('There is already a higher count - not updated.')
                # finally, if all is OK, the count will be added to the dictionary
                else:
                    birds[bird] = cnt
                    print('Bird added to the catalogue.')

        # while loop finished - time is up
        print('\nYOU ARE FINISHED!')
        artwork = open('bird_ascii.txt', 'r').read()
        print(artwork)

        # show the results of this counting
        print('The result of today\'s count is:\n')

        # create the database entry (using the dataframe module) and show birds with count > 0
        df = dataframe.create_db_entry(date.today(), now.strftime("%H:%M:%S"), duration, name, birds)
        print(df[df['Count'] > 0])

        # ask if results should be added to the database
        print(f'Do you like to save the result to the database [y]/n?')
        if input().upper() != 'N':
            # adding data using the dataframe module
            dataframe.add_to_db(standard_db, df)
            print(f'Thank you - data saved to: {standard_db}')

    else:
        # give short information in case duration = 0
        print('Counting aborted - back to main menu.')