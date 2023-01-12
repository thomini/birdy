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
      '\n- create plot: \'P\''
      '\n- exit: \'E\'')
action = input('Your choice: ')[0].upper()
if action not in ['C','R','P','E']:
    print('Sorry - action unknown.')
    action = input('Last chance - your choice: ')[0].upper()

if action == 'C':
    count_birds.start_count(count_birds.birds,dbname)

if action == 'R':
    df = dataframe.open_db(dbname)
    df_show = df[df['Count']>0]
    print(df_show)


