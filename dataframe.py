"""
This script is used to create the database (basically a pandas.DataFrame)
and define functions for
* handling the database
* analyse data
* create plots

Author: Dominik Imgrüth
"""

import pandas as pd
import matplotlib.pyplot as plt
from itertools import repeat

# define the columns of interest
cols = ['Date', 'Time', 'Duration(min)', 'Observer', 'Bird', 'Count']

# create empty dataframe
bird_count_df = pd.DataFrame(columns=cols)


def create_db_entry(date, time, dur: float, observer: str, data_dict: dict):
    """
    creates a database entry for observations made during one bird count period
    :param date: date on which the counting was conducted
    :param time: starting time of the counting period
    :param dur: float, duration of the counting period
    :param observer: str, name of the observer
    :param data_dict: dict, this is the bird counting data
        keys: str, bird species
        values: int, amount of birds
    :return: pandas.DataFrame
    """

    keys = data_dict.keys()
    values = data_dict.values()
    n = len(keys)

    # create lists of length n with the same entry
    date_list = list(repeat(date, n))
    time_list = list(repeat(time, n))
    dur_list = list(repeat(dur, n))
    obs_list = list(repeat(observer, n))

    # using zip, prepare data for creating a pandas.DataFrame with it
    data = list(zip(date_list, time_list, dur_list, obs_list, keys, values))

    return pd.DataFrame(data, columns=cols)


def open_db(path):
    """
    a function to open an existing database; if it not exists, it will be created
    :param path: must be in pickle format (.pkl)
    :return: pandas.DataFrame
    """
    if type(path) != str:
        print("path must be string")
        exit()
    try:
        df = pd.read_pickle(path)
    except:
        # create new dataframe
        df = bird_count_df
        df.to_pickle(path)

    return df


def add_to_db(db, df):
    """
    function for adding new observations to an existing database
    :param db: database (pandas.Dataframe) to which the observations should be added
    :param df: observations (pandas.Dataframe) to be added to db
    :return: None
    """

    active_db = open_db(db)
    new_db = active_db.append(df, ignore_index=True)
    new_db.to_pickle(db)


def save_report(df, name):
    """
    saves the report as .csv file
    :param df: data (pandas.Dataframe) to be saved
    :param name: file name
    :return: None
    """
    path = 'reports/' + name + '.csv'
    df.to_csv(path)


def plot_df(df):
    """
    wrapper function for matplotlib pyplot.bar plotting function
    :param df: birdy dataframe (pandas.Dataframe) holding data to be plotted
    :return: None, opens a matplotlib window
    """
    # colors = ['green', 'blue', 'purple', 'brown', 'teal']
    # create bar plot with bird species and amount
    plt.bar(df['Bird'], df['Count'])  # , color=colors)
    # include title and axes labels
    plt.title('Total bird counts', fontsize=14)
    plt.xlabel('Species', fontsize=14)
    plt.ylabel('Amount of sightings', fontsize=14)
    # include a grid
    plt.grid(True)
    # show the plot
    plt.show()


def plot_df_year(df, year: int = 2023):
    """
    wrapper function for plot_df: plots only a specified year
    :param df: birdy dataframe (pandas.Dataframe) holding data to be plotted
    :param year: int, year to be plotted
    :return: None, opens a matplotlib window
    """
    # translate 'Date' (str) to datetime and the extract the year
    df_year = df[pd.to_datetime(df['Date']).dt.year == year]
    # call plot_df on new selected year
    plot_df(df_year)
