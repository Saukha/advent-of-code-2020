#!/usr/bin/env python
# coding: utf-8

# Dec 2020 Day 1 part 1
from numpy import genfromtxt
arr = genfromtxt('2020_day01.txt', delimiter='', dtype = 'int')

product = 0
for i in range(len(arr)):
    #print('i', df.loc[i][0])
    for j in range(i+1, len(arr)):
        #print(df.loc[j][0])
            if arr[i]+ arr[j] == 2020:
                if arr[i] * arr[j] > product:
                    yi=arr[i]
                    yj=arr[j]
                    product = yi * yj

print(yi, '+', yj, '= 2020')
print('part 1:', product)

# Dec 2020 Day 1 part 2

product = 0
for i in range(len(arr)):
    #print('i', df.loc[i][0])
    for j in range(i+1, len(arr)):
        #print(df.loc[j][0])
            for k in range(j+1, len(arr)):
                if arr[i]+ arr[j] + arr[k] == 2020:
                    if arr[i] * arr[j] * arr[k] > product:
                        yi=arr[i]
                        yj=arr[j]
                        yk=arr[k]
                        product = yi * yj * yk
                        
print(yi, '+', yj, '+', yk,'= 2020')
print('part 2:', product)


