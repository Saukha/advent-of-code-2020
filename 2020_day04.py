#!/usr/bin/env python
# coding: utf-8

# 2020 day04 part 1

# read inputs
f = open('2020_day04.txt') # open file to read
data = f.readlines()
f.close()

valid = 0
# count & write cleaned/re-organized data to file
with open('2020_day04_from_part1.txt', 'w') as f:
    i = 0
    valid = 0
     #   print('current line:', data[i])
    while i < len(data):
        l = data[i].strip()
        while i+1<len(data) and data[i+1]!='\n':
            l = l.strip() + ' ' + data[i+1].strip()
            i+=1
        
        # valid count 
        count = l.count(':')
        if 'cid' in l:
            if count == 8:
                valid +=1
        elif count == 7:
            valid += 1    

        # write organized data in file
        f.write(l.strip()+'\n')
        
        # go to next data
        i+=1
            
print('part 1:', valid)

# part 2

''' 
for passport to be valid:
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
      If cm, the number must be at least 150 and at most 193.
      If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''

import re

# inputs
fp = open('2020_day04_from_part1.txt', 'r')           
data = fp.readlines()
fp.close()

# range and list
byr_range = range(1920, 2003)
iyr_range = range(2010, 2021)
eyr_range = range(2020, 2031)
hgtcm_range = range(150, 194)
hgtin_range = range(59, 77)
ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

# define tests
def test_hgt(x):
    if 'cm' in x:
        return int(x.rstrip('cm')) in hgtcm_range
    if 'in' in x:
        return int(x.rstrip('in')) in hgtin_range

# initialize test results 
T1 = False
T2 = False
T3 = False
T4 = False
T5 = False
T6 = False
T7 = False

# initialize
valid_count = 0  
i           = 0
flag        = True

# test data line by line
for line in data: 
    i +=1
    j = line.strip()
    if re.findall(r"byr:[\w\.-]+", j)!=[]:
        byr = re.findall(r"byr:[\w\.-]+", j)[0].lstrip('byr:')
        T1 = int(byr) in byr_range
    if re.findall(r"iyr:[\w\.-]+", j)!=[]:
        iyr = re.findall(r"iyr:[\w\.-]+", j)[0].lstrip('iyr:')
        T2 = int(iyr) in iyr_range
    if re.findall(r"eyr:[\w\.-]+", j)!=[]:
        eyr = re.findall(r"eyr:[\w\.-]+", j)[0].lstrip('eyr:')
        T3 = int(eyr) in eyr_range
    if re.findall(r"ecl:[\w\.-]+", j)!=[]:
        ecl = re.findall(r"ecl:[\w\.-]+", j)[0].lstrip('ecl:')
        T4 = ecl in ecl_list
    if re.findall(r"pid:[\w\.-]+", j)!=[]:
        pid = re.findall(r"pid:[\w\.-]+", j)[0].lstrip('pid:')
        T5 = len(re.findall(r"[0-9]", pid))==9
    if re.findall(r"hcl:#[\w\.-]+", j)!=[]:
        hcl = re.findall(r"hcl:#[\w\.-]+", j)[0].lstrip('hcl:')
        T6 = len(re.findall(r"[0-9]", hcl)) + len(re.findall(r"[a-f]", hcl))==6
    if re.findall(r"hgt:[\w\.-]+", j)!=[]:
        hgt = re.findall(r"hgt:[\w\.-]+", j)[0].lstrip('hgt:')
        T7 = test_hgt(hgt)
    if T1 and T2 and T3 and T4 and T5 and T6 and T7:
        valid_count +=1

    # reset results
    T1 = False
    T2 = False
    T3 = False
    T4 = False
    T5 = False
    T6 = False
    T7 = False

print('part 2:', valid_count)
