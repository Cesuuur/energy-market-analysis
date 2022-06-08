import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import numpy as np

def plotFunction(dataArray, title, xLabel, yLabel):
    '''
    Plot data array
    '''
    fig, ax = plt.subplots(figsize=(9, 9))
    ax.plot(np.arange(0, len(dataArray), 1)[::-1], dataArray)

    ax.set_title(title)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    plt.show()

def plotFunctionWithDates(dataArray, dates, title, xLabel, yLabel):
    '''
    Plot data array with dates
    '''
    fig, ax = plt.subplots(figsize=(9, 9))

    ax.plot(dates[::-1], dataArray[::-1])
    fig.autofmt_xdate(rotation=45)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    plt.xticks(np.arange(0, len(dataArray), 200))
    plt.show()