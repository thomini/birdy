# this script is used to create the database (a pandas dataframe)
# and define functions for analysis data
import pandas as pd
from itertools import repeat

# define the columns of interest
cols = ['Date', 'Time', 'Duration', 'Observer', 'Bird', 'Count']

# create empty dataframe
bird_count_df = pd.DataFrame(columns=cols)
#print(bird_count_df)

def create_db_entry2(date: str, time, dur: float, obs:int, data_dict:dict): #date,time,dur,obs,
    # data_dict will be the measurement
    keys = data_dict.keys()
    values = data_dict.values()
    n = len(keys)

    date_list = list(repeat(date, n))
    time_list = list(repeat(time, n))
    dur_list = list(repeat(dur, n))
    obs_list = list(repeat(obs, n))
    data = list(zip(date_list, time_list, dur_list, obs_list, keys, values))

    return pd.DataFrame(data, columns = cols)