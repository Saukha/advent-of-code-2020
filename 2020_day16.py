#!/usr/bin/env python
# coding: utf-8

# 2020 day 16 Part 1

# read inputs for valid_values
import pandas as pd
df1 = pd.read_csv('2020_day16_valid_ranges.txt', header = None, sep = ' ',
                 names = ['field', 'range1', 'or', 'range2'])
df1.drop('or', 1, inplace = True)

# reorganize data
n = df1['range1'].str.split('-', n = 1, expand = True)
m = df1['range2'].str.split('-', n = 1, expand = True)
df1['range1-a'] = n[0]
df1['range1-b'] = n[1]
df1['range2-a'] = m[0]
df1['range2-b'] = m[1]
#print(df1.head())

# build valid_value_set
valid_value_set = set() # initialize empty set
for i in range(0, len(df1)):
#    print(i)
#    print(df1.loc[i, :])
    a=int(df1.loc[i,'range1-a'])
    b=int(df1.loc[i,'range1-b'])
    c=int(df1.loc[i,'range2-a'])
    d=int(df1.loc[i,'range2-b'])
#    print(list(range(a, b+1))[0:5])
#    print(list(range(c, d+1))[-5:])
    for j in range(a, b+1):
        valid_value_set.add(j)
    for k in range(c, d+1):
        valid_value_set.add(k)

# print(len(valid_value_set))
# print(valid_value_set)

# read inputs for ticket_value_data
df = pd.read_csv('2020_day16_ticket_values.txt', 
                 header = None, sep = ',')

# check & add up error rate
invalid_tickets = []
error_rate = 0
for i in range(0, len(df)): # change 1 to len(df) for all rows
    # check each value against valid_value_set 
    for v in df.loc[i]:
        if v in valid_value_set:
            pass
        else:
            invalid_tickets.append(i)
            error_rate = error_rate + v
#            print('v:', v, ' | error_rate:', error_rate)

print('error rate:', error_rate)
# print(invalid_tickets)

# part 2


# part 2




