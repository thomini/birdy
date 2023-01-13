"""
this is the main birdy 'interface' file, from here all actions can be called.

Actions include
* do a bird counting
* check and delete the database
* create and save reports
* create plots

Author: Dominik Imgrüth
"""


import count_birds
import dataframe

# define standard database name - results will be saved there, unless specified otherwise by user
dbname = 'db/birds.pkl'

print('Hello to BIRDY! \n  ... your minion for counting birds in your garden!')

# start a while loop to keep the program running
QUIT = True
while QUIT:

    # print user options:
    print('\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+'
          '\nPlease choose an action:'
          '\n- start a new counting: [C]'
          '\n- print a report: [R]'
          '\n- save a report (csv): [S]'
          '\n- create plot: [P]'
          '\n- delete database: [D]'
          '\n- exit: [Q]')

    # use only first char of user input and capitalize it
    action = input('Your choice: ')[0].upper()
    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n')

    # depending on the user input one of the following ifs is executed
    if action == 'C':
        # use the count_birds.py code here
        # first create a copy of the species dictionary
        # (if the = would be used, only a reference would be created!)
        birds_count = count_birds.species.copy()
        count_birds.start_count(birds_count, dbname)

    elif action == 'R':
        # reporting: open database, select only counts > 0, and print the dataframe
        df = dataframe.open_db(dbname)
        df_show = df[df['Count']>0]
        print(df_show)

    elif action == 'S':
        # saving report:
        # first ask for name of the file
        rep_name = input('Please give a name for the report:\n')
        # open dataframe and save it as db
        df = dataframe.open_db(dbname)
        # ask the user if she would like to include also 'zeros' in the report
        print('[l]ong or [s]hort version?\nshort version includes only sightings (no "zeros")')
        action2 = input('Your choice: ')[0].upper()
        # if the user chooses a report without zeros (i.e. short report), filter on Count > 0
        if action2 == 'S':
            df = df[df['Count']>0]
        # finally use the .save_report function to save the dataframe as .csv file in the reports folder
        dataframe.save_report(df, rep_name)

    elif action == 'P':
        # plotting: open database
        df = dataframe.open_db(dbname)
        # for better visual representation choose only birds with a count > 0
        df = df[df['Count'] > 0]
        # the user can choose the year of the observation data used for the plot
        y = input('For which year you would like to get a plot?')
        try:
            dataframe.plot_df_year(df, int(y))
        # if no year is chosen or no data is available for the chosen date, plot all years
        except:
            print('year not known or no data available. Printing all years...')
            dataframe.plot_df(df)

    elif action == 'D':
        # delete the database. better to ask again, to avoid unintended loss of data
        print('Are you sure to delete the database? Data can not be recovered once deleted!')
        delete = input('[y]es / [n]o:')[0].upper()
        # only if the user confirms (by 'y' of 'Y'), data will be deleted
        if delete == 'Y':
            # create empty birdy dataframe
            df = dataframe.bird_count_df
            # and overwrite the database
            df.to_pickle(dbname)
            print(f'{dbname} deleted!')
        else:
            print('Database not deleted.')

    elif action == 'Q':
        # exit the program: say goodbye and set while condition to False
        print('Thank you for visiting Birdy - See you soon! Chirp chirp.')
        artwork = open('bird_ascii.txt', 'r').read()
        print(artwork)
        QUIT = False

    else:
        # if the input is not any of the above, ask again
        print('Sorry - action unknown.')

