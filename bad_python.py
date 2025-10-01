# bad_script.py
import numbers
import pandas as pd
import matplotlib.pyplot as plt
import random

def readData(filepath):
    """reads a filepath for a csv

    Args:
        filePath (string): the path to the file to be read into a dataframe

    Returns:
        dataframe: the dataframe that was read from the csv
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        print("Invalid filepath")
        return None


def avg(data, column):
    """gets the average of a column in a dataframe

    Args:
        data (dataframe): a dataframe with a column column
        column (string): the name of the column in the dataframe

    Returns:
        float: the average value of the data in the column
    """
    if data is None or data.empty:
        return None
    if not column in data.columns:
        print("column is not a feature in data")
        raise IndexError
    if isinstance(data[column], numbers.Number):
        print("the values in column are not numerical")
        raise TypeError
    avg = data[column].mean()
    print("average is", avg)
    return avg

def standardDev(data, column):
    """get the standard deviation of a column in a dataframe

    Args:
        data (dataframe): a dataframe with a column column
        column (string): the name of a column in a dataframe

    Returns:
        float: the standard deviation of the column
    """
    if data is None or data.empty:
        return None
    if not column in data.columns:
        print("column is not a feature in data")
        raise IndexError
    if isinstance(data[column], numbers.Number):
        print("the values in" + column + "are not numerical")
        raise TypeError
    stdev = data[column].std()
    print("std dev is", stdev)
    return stdev

def print5Random(data):
    """prints a random row 5 times. The same row may be printed multiple times

    Args:
        data (dataframe): _description_
    """
    print("sample rows:")
    if data is None or data.empty:
        raise ValueError("DataFrame is empty. Expected non-empty input.")
    for i in range(5):
        r = random.randint(0, len(data)-1)
        print(data.iloc[r])

def plotVals(data, value):
    """create and show a graph of a column in a dataframe

    Args:
        data (dataframe): the dataframe with the data
        value (string): the name of a column in data
    """
    if data is None or data.empty:
        raise ValueError("DataFrame is empty. Expected non-empty input.")
    if not value in data.columns:
        print("column is not a feature in data")
        raise IndexError
    plt.plot(data[value])
    plt.title("Values")
    plt.show()
    plt.savefig('./chart.png', dpi=300, bbox_inches='tight')
    plt.close()  
