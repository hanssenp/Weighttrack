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
import matplotlib.pyplot as plt


# start time is 4am Sun, Apr 29 2018
time.ctime(1524988800.0398614)
tstart = 1524988800.0398614

# number of weeks elapsed; also equal to current week number
tcurrent = time.time()
weekscurrent = round((tcurrent - tstart)/604800)

# Today's weigh in
wcurrent = float(input("Enter today's weight in pounds: "))

# Functional! This section will get the csv as a list, then change the current
# week's value to the current weight as input above.
f1 = open("weightcomma.csv", "r")
csvfile = csv.reader(f1)
lines = list(csvfile)

# You are getting the csv file here as a list of lists. So:
# Select the row you want -- current week -- as a list, taken from the larger
# list of all the rows in the csv. Delete the third entry on that small list,
# then add a new third entry with current weigh -- effectively, replacing the
# third (empty) cell with the correct value for current weight. Then
# replace (delete and insert) the appropriate row in the big list with your new, modified
# small list. Then write the updated list to the csv.
lines2=lines[weekscurrent].copy()
lines2.pop(2)
lines2.insert(2, wcurrent)
lines.pop(weekscurrent)
lines.insert(weekscurrent,lines2)

# Close the original file, we're done with it
f1.close()

# Attempt to write this list back into the csv.
# Currently writing to a seperate csv, "weightcomma2.csv," for test purposes
# So that you don't have to manually remake "weightcomma" every time.
# writer = csv.writer(open("weightcomma2.csv", mode='w'))
# writer.writerows(lines)

# Some online have suggested a "with" loop:
with open("weightcomma2.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(lines)
