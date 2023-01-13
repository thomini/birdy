# this is the main file. all actions can be called from here.
# actions include
# * do a bird counting
# * check the databse
# * create reports
import count_birds
import dataframe

# define standard database name - results will be saved there, unless specified otherwise by user
dbname = 'db/birds.pkl'

print('Hello to BIRDY! \n  ... your minion for counting birds in your garden!')

# start a while loop to keep the program running
QUIT = True
while QUIT:

    print('\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+'
          '\nPlease choose an action:'
          '\n- start a new counting: \'C\''
          '\n- print a report: \'R\''
          '\n- save a report (csv): \'S\''
          '\n- create plot: \'P\''
          '\n- exit: \'E\'')

    action = input('Your choice: ')[0].upper()
    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n')

    if action == 'C':
        count_birds.start_count(count_birds.birds, dbname)

    elif action == 'R':
        df = dataframe.open_db(dbname)
        df_show = df[df['Count']>0]
        print(df_show)

    elif action == 'S':
        rep_name = input('Please give a name for the report:\n')
        df = dataframe.open_db(dbname)
        #rep_year = input('Please choose a year for the report (choose "a" for all years):\n')[0].upper()
        #if rep_year != 'a':
        #    try:
        #        rep_year = int(rep_year)
        print('[l]ong or [s]hort version?\nshort version includes only sightings (no "zeros")')
        action2 = input('Your choice: ')[0].upper()
        if action2 == 'S':
            df = df[df['Count']>0]
        dataframe.save_report(df, rep_name)

    elif action == 'P':
        df = dataframe.open_db(dbname)
        df = df[df['Count'] > 0]
        y = input('For which year you would like to get a plot?')
        try:
            dataframe.plot_df_year(df, int(y))
        except:
            print('year not known or no data available. Printing all years...')
            dataframe.plot_df(df)

    elif action == 'E':
        print('Thank you for visiting Bird - See you soon! Chirp chirp.')
        QUIT = False

    else:
        print('Sorry - action unknown.')

