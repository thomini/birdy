# this script is used to create the database (a pandas dataframe)
# and define functions for analysis data
import pandas as pd
from itertools import repeat

# define the columns of interest
cols = ['Date', 'Time', 'Duration(s)', 'Observer', 'Bird', 'Count']

# create empty dataframe
bird_count_df = pd.DataFrame(columns=cols)

def create_db_entry2(date, time, dur: float, observer: str, data_dict:dict):
    # data_dict will be the measurement
    keys = data_dict.keys()
    values = data_dict.values()
    n = len(keys)

    date_list = list(repeat(date, n))
    time_list = list(repeat(time, n))
    dur_list = list(repeat(dur, n))
    obs_list = list(repeat(observer, n))
    data = list(zip(date_list, time_list, dur_list, obs_list, keys, values))

    return pd.DataFrame(data, columns = cols)

#TODO: function "create report" for given date
#TODO: save dataframe to database
#TODO: create plot

def save_df(df,save_as):
    df.to_pickle(save_as)

# a function to open an existing database; if it not exists it will be created
# path must be in pickle format (.pkl)
def open_db(path):
    if type(path) != str:
        print("path must be string")
        exit()
    try:
        df = pd.read_pickle(path)
    except:
        # create new dataframe
        df = pd.DataFrame(columns=cols)
        df.to_pickle(path)

    return df

#open_db('db/2023_birds.pkl')


def add_to_db(db, df):
    active_db = open_db(db)
    new_db = active_db.append(df,ignore_index = True)
    new_db.to_pickle(db)