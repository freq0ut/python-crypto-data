# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:22:28 2021

@author: zackg
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import numpy as np
import pandas as pd
import seaborn as sns

numMovingAvgs = 30

# define function for reversing lists
def Reverse(lst): 
    new_lst = lst[::-1] 
    return new_lst 

# create dataframes for closing price and dates from .csv for BTC
btc_df = pd.read_csv('aave-btc-max.csv', usecols=[0, 1])
btc_date_df = pd.read_csv('aave-btc-max.csv', usecols=[0])
btc_closePrice_df = pd.read_csv('aave-btc-max.csv', usecols=[1])

# convert BTC date/time dataframe to list
btcDateList = btc_date_df.values.tolist()
delistBtcDateList = []

# remove time from date list
for i in range (0, len(btcDateList)):
    delistBtcDateList.append(btcDateList[i][0].split(' ')[0])

# reverse both lits to get chronological ordering
formatBtcDateList = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in delistBtcDateList]
btcClosePriceList = btc_closePrice_df.values.astype(float).tolist()

# moving average risk color map list
aaveMovingAvg = []

# buffer first numMovingAvgs values with 0
for i in range (0, numMovingAvgs):
    aaveMovingAvg.append(i)

# calculate moving average for previous numMovingAvgs days for each location
for i in range (numMovingAvgs, len(btcClosePriceList)):
    movingAvgBtc_sum = 0
    for j in range (0, numMovingAvgs):
        movingAvgBtc_sum = movingAvgBtc_sum + float(btcClosePriceList[i-j][0])

    movingAvgBtc = movingAvgBtc_sum/numMovingAvgs
    aaveMovingAvg.append(movingAvgBtc)

# remove the first numMovingAvgs values
for i in range (0,numMovingAvgs):
    formatBtcDateList.pop(0)
    btcClosePriceList.pop(0)
    aaveMovingAvg.pop(0)

# set background color
plt.style.use('dark_background')

# scatter plot with color map
plt.scatter(formatBtcDateList, btcClosePriceList, c = aaveMovingAvg, s = 100, cmap = 'cool')
    
# naming the x axis  
plt.xlabel('Date', fontsize = 18) 

# naming the y axis  
plt.ylabel('Price (BTC)', fontsize = 18)

# giving a title to my graph  
plt.title('Aave (AAVE) Price History', fontsize = 28)  

# change size/color of ticks on x and y
plt.tick_params(direction='out', length=6, width=2, colors='white', grid_color='gray', grid_alpha=0.9, labelsize = 15, pad = 6)

# remove every nth tick label for date to improve readability
ax = plt.gca()
for index, label in enumerate(ax.xaxis.get_ticklabels()):
    if index % 1 != 0:
        label.set_visible(False)

# function to show the plot
cbar = plt.colorbar()
cbar.ax.set_yticklabels(['Low Risk','','','Med Risk','','','High Risk'], fontsize = 16)
cbar.ax.tick_params(length = 0)
plt.show()
plt.savefig('aave.png', dpi=600)