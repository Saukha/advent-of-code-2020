#!/usr/bin/env python
# coding: utf-8

# 2020 day 13 part 1

# inputs
with open('2020_day13.txt', 'r') as f:
    data = f.readlines()
    earliest = int(data[0])
    l = data[1]

l = list(l.split(','))
buses = [int(x) for x in l if x !='x']

# calculate min missed bus at earliest available time
wait = []
for bus in buses:
    wait.append(bus - earliest % bus)
#    print('bus',bus, 'miss', earliest % bus, 'wait', bus - earliest % bus)

# answer wait time of the next soonest bus times the bus number
for i in range(0, len(wait)):
    if wait[i] == min(wait):
        print('part 1:', buses[i]*wait[i])


######################################################
# 2020 day 13 part 2 version f

# inputs
part2_earliest = 100000000000000
# buses   = [ 19, 37, 883, 23, 13, 17, 797, 41, 29]
# offsets = [  0, 13,  19, 27, 32, 36,  50, 60, 79]
# max(buses) = 883
# find i-19 when all conditions below are met:
# (i   -19)%19  ==0  # bus 19
# (i+13-19)%37  ==0  # bus 37
# (i+19-19)%883 ==0  # bus 883
# (i+27-19)%23  ==0  # bus 23
# (i+32-19)%13  ==0  # bus 13
# (i+36-19)%17  ==0  # bus 17
# (i+50-19)%797 ==0  # bus 797
# (i+60-19)%41  ==0  # bus 41
# (i+79-19)%29  ==0  # bus 29

# according to the offsets, bus 19 will take off again when 883 takes off
# similarly buses 17, 41, 13 would have taken off with 883 before 
#    taking off at preset offset times

start = (part2_earliest//(883*19*17*41*13)+1)*883*19*17*41*13
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
        print('part 2:', i-19)
        break
