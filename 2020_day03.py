#!/usr/bin/env python
# coding: utf-8

# day 3
import pandas as pd
df = pd.read_csv('2020_day03.txt', header = None, names = ['grid'])

# part 1

i = 0
j = 3
total = 0
line = df.loc[0, 'grid']
l = len(line)
        
for i in range(1, len(df)):
    line = df.loc[i, 'grid']  
    if j < l:
        if line[j] == '#':
            total += 1
#        print(line, '    i:',i,'  j:', j,'  total:', total)
        j += 3
        if j == 33:
            j = 2
        elif j == 32:
            j = 1
        elif j == 31:
            j = 0
print('part 1:', total)

# part 2
'''
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
'''
R = [1,3,5,7,1]
D = [1,1,1,1,2]

product = 1

for k in range(0,5):
#    print('k = ',k, '  #################################################################')
    i = 0
    j = 0
    total = 0
#    print(i,j,k, 'R=',R[k], 'D=', D[k])
    while i < len(df):
        line = df.loc[i, 'grid'] 
        if j < l:
            if line[j] == '#':
                total += 1
#            print(line, '   ', line[j], '    i:',i,'  j:', j,'  total:', total)
        i += D[k]
        j += R[k]
        if j == 37:
            j = 6
        elif j == 36:
            j = 5
        elif j == 35:
            j = 4
        elif j == 34:
            j = 3
        elif j == 33:
            j = 2
        elif j == 32:
            j = 1
        elif j == 31:
            j = 0
    product = product * total
            
print('part 2:', product)

