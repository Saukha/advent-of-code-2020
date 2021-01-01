#!/usr/bin/env python
# coding: utf-8

# 2020 day 13 part 1
# Examples
# earliest = 939
# buses = [7,13,59,31,19]

# inputs
earliest = 1006605
buses = [19,37,883,23,13,17,797,41,29]

# calculate min missed bus at earliest available time
miss = []
wait = []
for bus in buses:
    miss.append(earliest % bus)
    wait.append(bus - earliest % bus)
#    print('bus',bus, 'miss', earliest % bus, 'wait', bus - earliest % bus)

# answer wait time of the next soonest bus times the bus number
for i in range(0, len(wait)):
    if wait[i] == min(wait):
        print('part 1:', buses[i]*wait[i])

######################################################
# 2020 day 13 part 2 version f

# inputs
L_earliest = 100000000000000
# l ='19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,883,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,x,x,797,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'

'''
# create buses and departure offsets
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
'''

# buses   = [ 19, 37, 883, 23, 13, 17, 797, 41, 29]
# offsets = [  0, 13,  19, 27, 32, 36,  50, 60, 79]
# max(buses) = 883
# find i-19 when all conditions are met:
#t0 = (i   -19)%19  ==0  # bus 19
#t1 = (i+13-19)%37  ==0  # bus 37
#t2 = (i+19-19)%883 ==0  # bus 883
#t3 = (i+27-19)%23  ==0  # bus 23
#t4 = (i+32-19)%13  ==0  # bus 13
#t5 = (i+36-19)%17  ==0  # bus 17
#t6 = (i+50-19)%797 ==0  # bus 797
#t7 = (i+60-19)%41  ==0  # bus 41
#t8 = (i+79-19)%29  ==0  # bus 29

# baccording to the offsets, bus 19 will take off again when 883 takes off
# similarly buses 17, 41, 13 would have taken off with 883 before 
#    taking off at preset offset times

start = (L_earliest//(883*19*17*41*13)+1)*883*19*17*41*13
end   = start*200

# step thru time when buses 883, 19, 17, 41 and 13 take off together
for i in range(start, end, 883*19*17*41*13):
    if   (i+31)%797!=0: # bus 797
        continue
    elif (i-6)%37!=0:   # bus 37
        continue
    elif (i+60)%29!=0:  # bus 29
        continue
    elif (i+8)%23!=0:   # bus 23
        continue
    else:
        print('part 2: offset departures start with bus 19 at', i-19)
        break
