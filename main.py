# this is the main file. all actions can be called from here.
# actions include
# * do a bird counting
# * check the databse
# * create reports
import count_birds
import dataframe

dbname = 'db/2023_birds.pkl' # could be asked from the user

print('Hello to BIRDY! \n  ... your minion for counting birds in your garden!')
print('\nPlease choose an action:'
      '\n- start a new counting: \'C\''
      '\n- print a report: \'R\''
      '\n- save a report (csv): \'S\''
      '\n- create plot: \'P\''
      '\n- exit: \'E\'')
action = input('Your choice: ')[0].upper()
if action not in ['C', 'R', 'S', 'P', 'E']:
    print('Sorry - action unknown.')
    action = input('Last chance - your choice: ')[0].upper()

if action == 'C':
    count_birds.start_count(count_birds.birds,dbname)

if action == 'R':
    df = dataframe.open_db(dbname)
    df_show = df[df['Count']>0]
    print(df_show)

if action == 'S':
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


