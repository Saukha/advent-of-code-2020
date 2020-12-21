#!/usr/bin/env python
# coding: utf-8

# 2020 day 13 part 1
# Examples
#earliest = 939
#buses = [7,13,59,31,19]

# inputs
earliest = 1006605
buses = [19,37,883,23,13,17,797,41,29]

# calculate min missed bus at earliest available time
miss = []
wait = []
for bus in buses:
    miss.append(earliest % bus)
    wait.append(bus - earliest % bus)
 #   print('bus',bus, 'miss', earliest % bus, 
 #       'wait', bus - earliest % bus)

# answer wait time of the next soonest bus times the bus number
for i in range(0, len(wait)):
    if wait[i] == min(wait):
        print('part 1 answer:', buses[i]*wait[i])

#################################################################
# part 2

import numpy as np
import time

# Examples
# The earliest timestamp that matches the lists:
l1 = '17,x,13,19'      # is 3417.
l2 = '67,7,59,61'      # first occurs at timestamp 754018.
l3 = '67,x,7,59,61'    # first occurs at timestamp 779210.
l4 = '67,7,x,59,61'    # first occurs at timestamp 1261476.
l5 = '1789,37,47,1889' # first occurs at timestamp 1202161486.
L1 = list(l1.split(','))
L2 = list(l2.split(','))
L3 = list(l3.split(','))
L4 = list(l4.split(','))
L5 = list(l5.split(','))
L1_earliest = 3417-100
L2_earliest = 754018-100
L3_earliest = 779210-100
L4_earliest = 1261476-100
L5_earliest = 1202161486-110

# inputs
L_earliest = 100000000000000
l ='19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,883,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,x,x,797,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'
L = list(l.split(','))

# create bus schedules
def buses_offsets(L):
    buses = []
    offsets = []
    j = 0
    for i in L:
        if i !='x':
            buses.append(i)
            offsets.append(j)
        j+=1
    buses = np.array(buses, dtype = int)
    offsets = np.array(offsets, dtype = int)
    return(buses, offsets)

# find_t 
def find_t(t, buses, offsets):
    # initialize
    flag = True 
    while flag:
        print(t)
        # find next departures
        next_depts[0] = t + buses[0] - t%buses[0]
        for i in range(1, len(buses)):  
            next_depts[i] = next_depts[0] + buses[i] - next_depts[0]%buses[i]       
#        print('t:', t, next_depts)

        # check if all buses depart at their required offsets       
        for i in range(1, len(next_depts)):
            # flag to exit while loop when flag = True fo all buses
            flag = flag and next_depts[i] - next_depts[0] == offsets[i]  

        if flag:
            break
        elif flag == False: # not all buses depart at offsets
            # set t for next while loop after dep time of the latest bus
            t = max(next_depts)
#            print('next t:', t)
#            time.sleep(5)
            flag = True # reset
    return(t, next_depts)

# find t for answer, where all buses are departing at the required offset time
# initialize variables
t = 0
buses = []
offsets = []
buses, offsets = buses_offsets(L5)
next_depts = np.zeros(len(buses), dtype = int)

# find_t
t, next_depts = find_t(L5_earliest-100, buses, offsets)

# print results
print('buses:', buses, 'offsets:', offsets)
print('part 2: t with departures at required offsets:', next_depts)

