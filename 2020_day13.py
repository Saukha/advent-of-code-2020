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
L1_start = 3417-1000
L2_start = 754018-1000
L3_start = 779210-1000
L4_start = 1261476-1000
L5_start = 1202161486-100000

# inputs
L_start = 100000000000000
l='19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,883,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,x,x,797,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'
L = list(l.split(','))

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

# find t
def find_t(start, l, loop):
    buses, plus_t = schedule(l)
#    print(buses)
#    print(plus_t)
    for i in range(start, start+loop*max(plus_t)):
        T = []
        for j in range(0, len(buses)):
            T.append((i+plus_t[j])%int(buses[j])==0)
        print('i:', i, T)
        # check condition at timestamp ranging time interval from start to 
        # some short time in the future, looping thru few iterations of departures
        flag = True
        for f in T:
            flag = flag and f
#        print(flag)
        if flag:
            print('i:', i, T)
            break
    return(i, T)

# test codes
t, result = find_t(L2_start, L2, 100000000000000)
print(t, result)

# find t
#t, result = find_t(L_start, L, 100000000000000)
#print(t, result)
