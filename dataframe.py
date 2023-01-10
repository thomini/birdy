# this script is used to create the database (a pandas dataframe)
# and define functions for analysis data
import numpy as np
import pandas as pd

# define the columns of interest
cols = ['Date', 'Time', 'Duration', 'Observer', 'Bird', 'Count']

# create empty dataframe
bird_count_df = pd.DataFrame(columns=cols)
print(bird_count_df)