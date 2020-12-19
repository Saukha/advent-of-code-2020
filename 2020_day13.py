#!/usr/bin/env python
# coding: utf-8

# 2020 day 13 part 1
# Examples
#earliest = 939
#buses = [7,13,59,31,19]

# inputs
earliest = 1006605
l = '19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,883,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,x,x,797,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'
l = list(l.split(','))
buses = [int(x) for x in l if x !='x']

# calculate min missed bus at earliest available time
miss = []
wait = []
for bus in buses:
    miss.append(earliest % bus)
    wait.append(bus - earliest % bus)
    print('bus',bus, 'miss', earliest % bus, 'wait', bus - earliest % bus)

# answer wait time of the next soonest bus times the bus number
for i in range(0, len(wait)):
    if wait[i] == min(wait):
        print('answer:', buses[i]*wait[i])

# part 2

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
L5 = list(l4.split(','))

# inputs
earliest = 100000000000000
l='19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,883,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,x,x,797,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'
buses = l.split(',')

# create bus schedules
def schedule(l):
    buses = []
    plus_t = []
    j = 0
    for i in l:
        if i !='x':
            buses.append(i)
            plus_t.append(j)
        j+=1
    return(buses, plus_t)

buses, plus_t = schedule(L)
print(L)
print(buses)
print(plus_t)

