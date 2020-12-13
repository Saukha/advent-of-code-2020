#!/usr/bin/env python
# coding: utf-8

import pandas as pd
df = pd.read_csv("2020_day2.txt", header = None, names = ['const', 'char', 'pwd'], sep = ' ')

# part 1
df.char = df.char.map(lambda x: x.rstrip(':'))
new = df.const.str.split("-", n = 1, expand = True)
df['min'] = new[0]
df['max'] = new[1]
df['count']=''
df['false_valid']=''

l=[]
count = 0
for i in range(0, len(df)):
    count = 0 # reset
    l = [char for char in df.pwd[i]]
    m = int(df['min'][i])
    n = int(df['max'][i])
    for j in l:
        if j == df.char[i]:
            count += 1
    df.loc[i, 'count'] = count
    if ((count > m - 1) and (count < n + 1)):  
        df.loc[i, 'false_valid'] = 'y'
    else:
        df.loc[i, 'false_valid'] = 'n'

print('false_valid:', len(df[df['false_valid']=='y']))

# part 2
df['true_valid']=''

count = 0
for i in range(0, len(df)):
    count = 0 # reset
    l = [char for char in df.pwd[i]]
    m = int(df['min'][i])
    n = int(df['max'][i])
    char = df.loc[i, 'char']
    if ((l[m-1] == char) and (l[n-1] == char)):
        df.loc[i, 'true_valid'] = 'n'
    elif ((l[m-1] == char) or (l[n-1] == char)):
        df.loc[i, 'true_valid'] = 'y'
    else:
        df.loc[i, 'true_valid'] = 'n'

print('true_valid:', len(df[df['true_valid']=='y']))

