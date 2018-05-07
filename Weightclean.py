# -*- coding: utf-8 -*-
"""
Created on Fri May  4 14:03:48 2018

@author: peter
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:26:14 2018

@author: peter
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:44:11 2018

@author: peter
"""

# libraries
import time
import datetime
import numpy as np
import openpyxl
import csv
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


# start time is 4am Sun, Apr 29 2018
time.ctime(1524988800.0398614)
tstart = 1524988800.0398614

# number of weeks elapsed; also equal to current week number
tcurrent = time.time()
weekscurrent = round((tcurrent - tstart)/604800) # round for whole number

# Today's weigh in
wcurrent = float(input("Enter today's weight in pounds: "))

# Get the csv file contents as a list, then change the current
# week's value to the current weight as input above.

f1 = open("weightcomma.csv", "r")
csvfile = csv.reader(f1)
lines = list(csvfile)
# alternate: with loop. Like this:
# with open("weightcomma.csv", "r") as f1:
#    csvfile = csvreader(f1)
#    lines = list(csvfile)

# You are getting the csv file here as a list of lists: a big list, made up of
# smaller lists (one for each week). Updating the csv with the new weight
# measurement will require two modifications: an update to the small list
# corresponding to the current week, and then an update of the big list with
# the newly modified small list from the current week.
# For both updates, we need to delete the old entry entirely and insert a
# new one.
# Then we can write the updated big list to the csv file.
lines2=lines[weekscurrent].copy() # separate copy of list for only current week
lines2.pop(2) # remove third entry in current week list
lines2.insert(2, wcurrent) # insert updated weight in third position
lines.pop(weekscurrent) # remove the old list for current week from big list
lines.insert(weekscurrent,lines2) # Insert updated current week into big list.

# Close the original file, we're done with it
f1.close()

# Write big list back into the csv.
# "with" loop automatically closes file when finished
with open("weightcomma.csv", "w") as f:
    writer = csv.writer(f, lineterminator = '\n')
    writer.writerows(lines)

# If you need to open the csv with a "with" loop again:
# with open("weightcomma.csv", "r") as f1:
#    csvfile = csvreader(f1)
#    lines = list(csvfile) # (gives contents as list)

# Build chart

# pandas might work better? e.g.:
df = pd.read_csv('weightcomma.csv')
# df['Date'] = df['Date'].map(lambda x: datetime.strptime(str(x), '))
print(df.head(6))
#df1 = pd.DataFrame(np.random.randn(1000, 2), columns = ['Date', 'Weight']).cumsum()
df.plot.scatter(x='Week', y='Weight', color='k')
# df1['Week'] = pd.Series(list(range(len(df))))
# df1.plot(x='Week', y='Weight')

#data = np.genfromtxt('weightcomma.csv', delimiter=',', names=[True])
#x, y, z = np.loadtxt('weightcomma.csv', delimiter=',', skiprows=1)
#plt.plot('x','z', label='Weekly updated weight')


plt.axhline(y=160, color='r', linestyle='-') # red line at starting weight
plt.axhline(y=145, color='b', linestyle='-') # blue line at goal weight
plt.axis([0, weekscurrent+1, 135, 170])
plt.xticks(np.arange(0, weekscurrent+1, step=1))

plt.show()
