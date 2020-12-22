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
    print('bus',bus, 'miss', earliest % bus, 'wait', bus - earliest % bus)

# answer wait time of the next soonest bus times the bus number
for i in range(0, len(wait)):
    if wait[i] == min(wait):
        print('answer:', buses[i]*wait[i])


