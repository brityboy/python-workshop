# how to solve a problem when starting from scratch
# two ways
# 1) a structure exists and you have to work within it
# 2) you have no structure and you are going to do something form scratch
#
# this tactic is called top down programming
# this effectively boils down to "keeping away from coding as long as i can"
# I will call functions even though they don't exist
# Then i'll work with the output they can't produce yet
# I'll codify these two pieces of my problem
# I'll get to what these functions need to do
#
# we want these functions to be abstractions of problems
#
# when we write code in this way, we'll get better and better at certain things
#
# we'll be able to foresee these circumstances better and better
#
# example - calhousing data
#
# the biggest barrier is the act of starting
#
# the first thing to write is a name block
# write down the general functions that you want to use
# write out the functions that you want to use
# write the docstring associated with each file
# this clarifies the inputs and outpuers you are going to need

# Treat all sprints like mini projects and use the top down approach always


import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    ''' returns data in a dataframe
    '''
    df = pd.read_csv('cal_housing.data')
    return df


def clean_data(df):
    ''' return dataframe with missing values and outliers removed
    '''
    remove_missing(df)
    remove_outliers(df)


def remove_missing(df):
    ''' modify dataframe to remove missing values
    '''
    pass


def remove_outliers(df, sd):
    '''
    INPUT:  df - pandas dataframe
            df - int, # of standard deviations past which we should consider
                the value an outliers
    OUTPUT: none
    '''
    pass


def plot_stuff_about_data(df):
    ''' plots the histograms of all numeric columns
        in the data
    '''
    df.hist()
    plt.show()


if __name__ == '__main__':
    data = load_data()
    print(data)
    clean_data(data)
    plot_stuff_about_data(data)


# Magic methods
