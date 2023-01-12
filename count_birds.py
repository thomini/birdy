# this file represents the interface to the user when counting birds
from typing import Dict
import time
import dataframe
from datetime import date, datetime
import warnings
warnings.filterwarnings("ignore",category=FutureWarning)

# create a catalogue of pre-defined birds
# used the same birds as in the bridlife catalouge:
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
def start_count(birds,standard_db):
    # say hello and ask for name
    print('Hello dear bird friend!\nWhat is your name?')
    name = input('NAME: ').capitalize()

    # ask the user how long she would like to count birds
    # initial condition for the while loop
    duration = -1
    while duration < 0:
        input_dur = input(f'How long would you like to count birds, {name}? \n\nAnswer in Minutes: ')
        try:
            duration = float(input_dur)
            if duration < 0:
                print("The time is negative - this is not a time machine! \nYou can exit with '0' \n Try again:")
        except:
            print('I am sorry, this is not a number!')
            exit()

    # now implement the timer: add the duration to the actual time and use it for keep a while loop running
    now_sec = time.time()
    now = datetime.now() # for the database in datetime format

    # add the duration to the current time for the timer (while loop)
    time_quit = now_sec + duration * 60  # in seconds
    print("Time is running, let's watch out for birds!")
    while time_quit > time.time():

        bird = input('Which bird do you see?\n (type "exit" for stop counting; "show" for inspect birds)\n').upper()
        # check if (positive) integer:
        if bird == 'EXIT':
            print('You stopped counting!')
            # overwrite duration:
            duration = round((time.time() - now_sec)/60,2)
            break
        if bird == 'SHOW':
            print(list(birds.keys()))
            continue
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
            if birds[bird] > cnt:
                print('There is already a higher count - not updated.')
            else:
                birds[bird] = cnt
                print('Bird added to the catalogue.')

    print('\nYOU ARE FINISHED!')
    artwork = open('bird_ascii.txt', 'r').read()
    #file_contents = f.read()
    print(artwork)

    print('The result of today\'s count is:\n')

    # create the database entry (pandas dataframe) and show birds with count > 0
    df = dataframe.create_db_entry(date.today(), now.strftime("%H:%M:%S"), duration, name, birds)
    print(df[df['Count'] > 0])

    # ask if results should be added to the database
    # if date exists, ask to overwrite
    print(f'Do you like to save the result to the database [y]/n?')
    if input().upper() != 'N':
        print('To which database would you like to save it?\n (leave blank if you would like to save it to the standard db)')
        db_name = input("database name:")
        if db_name == "":
            dataframe.add_to_db(standard_db, df)
        else:
            dataframe.add_to_db(db_name, df)