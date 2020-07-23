#!/usr/bin/env python3
# library(reticulate)
# use_virtualenv(r-reticulate)

import pandas as pd
ps3 = pd.read_csv('pandas/ps3.csv')

ps3.shape
ps3.shape[0]
ps3.shape[1]
ps3.columns
len(ps3.columns)
ps3.dtypes
print(ps3.head(5))
ps3.dtypes
ps3.describe()

ps3['Year'].head()
ps3.iloc[0]
ps3.iloc[0,0]
ps3.iloc[0,1]
ps3.iloc[0,2]

ps3.iloc[26]
ps3.iloc[27]

ps3.loc[[0,1,2,26,27],['Name','Year']]
ps3.index

ps3['Year']
ps3.Year

dir(ps3)

# How many years are there?
AllYears = ps3['Year']
# There is a method called unique that can be used to determine the number of 
# unique entries in the variable
AllYears.unique()
# and we can find the length of this
len(AllYears.unique())

print('Number of unique years', len(AllYears.unique()))

# An alternative is drop_duplicates
# You would use this in a data frame
AllYears.drop_duplicates()

# what was the biggest global seller in 2006?
# first we have to select 2006
# let's start with the Years and make a variable that is True if the 
# the year is 2006 and False otherwise
ps3_TF = ps3['Year'] == 2006
# note that can use more complicated comparisons like >, <=, <, <=, and !=
# for example
ps3_TF2 = ps3['Year'] >= 2007
ps3_2006 = ps3.loc[ps3_TF]

# the maximum is easy to find
maxIn2006 = ps3_2006['Global_Sales'].max()
# the index where this is also easy to find
maxIndexIn2006 = ps3_2006['Global_Sales'].idxmax()

# we can combine to make a variable containing details of the maximum
# and we can print it out
ps3_maxIn2006 = ps3_2006.loc[maxIndexIn2006]
print('Max', ps3_maxIn2006['Name'], ps3_maxIn2006['Global_Sales'])

# We can now repeat this for different years 
# I've combined them into a single row
# You will find that experienced programmers do this
# While you are learning you don't have to
ps3.loc[ps3.loc[ps3['Year'] == 2011]['EU_Sales'].idxmax()]

# Pandas lets you make new columns
# Let's work out what percentage is EU sales
# This is 100*EU_Sales/Global_Sales
ps3['EU_Percentage'] = 100 * ps3['EU_Sales']/ps3['Global_Sales']
# Notice how the calculation applies to all the rows 
# This is a big strength of data frames
# Notice how the new column is added to the data frame
# For loops are not required.

