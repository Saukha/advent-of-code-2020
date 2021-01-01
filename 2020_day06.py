#!/usr/bin/env python
# coding: utf-8

# 2020 day 6 part 1

with open('2020_day06.txt', 'r') as f:
    data = f.readlines()

q = set()
count_list = []
i = 0
l = ''

while i < len(data)-1:
#    print('i: ', i, data[i])
    l = l + data[i].rstrip('\n')
#    print(l)
    if data[i+1] == '\n':
        count_list.append(len(set(l)))
#        print(len(set(l)), set(l))
        l = ''
    i += 1  

print('part 1:', sum(count_list))

#### part 2
# update tallies for each person's answer set
def update_tallies(l):    
    for a in list(l):
        x = q.find(a)     # find position of a in q
    #    print(x)
        tallies[x]  += 1  # add 1 to the position if a letter is found
    tallies[26] += 1      # add 1 for each person's answers
    return tallies[26]    # return the total of people so far

# get total of questions everyone answers 'yes' per group 
def q_count(tallies):
    q = 0
    # update q comparing value of each question/key to T
    for i in range(0, 26):
        if tallies[i] == tallies[26]:
            q += 1
    return q

# initialize variables
sum_of_count = 0      # cumulative sum for all groups
count        = 0      # count of questions per group
i            = 0      # to iterate through data
tallies      = [0]*27 # to store tallies for each person
q 			 = 'abcdefghijklmnopqrstuvwxyzT'  

# loop through all data
while i < len(data)-1:
    l = data[i].rstrip('\n')
    # update tallies for each person
    if l!='':  # if line is not blank
        update_tallies(l)
#        print(l)
#        print(tallies)

    # if next line is blank/end of one group    
    if data[i+1] == '\n': 
        # get count of questions that everyone answered 'yes'
        count = q_count(tallies)
        # cumulative total for groups so far
        sum_of_count = sum_of_count + count
        
        #reset for next group
        tallies = [0]*27
        count   = 0
    i += 1  # to process next line

print('part 2:', sum_of_count)
