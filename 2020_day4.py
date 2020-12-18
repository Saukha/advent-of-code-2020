#!/usr/bin/env python
# coding: utf-8

'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''

# day 4
# part 1

f = open('2020_day4.txt') # open file to read
data = f.readlines()
f.close()

f = open('2020_day4d.txt', 'a')
valid = 0
i = 0
while i < len(data):
    l = data[i]
#    print('current i:', i, l)
    if l !='\n':
        while i+1<len(data) and data[i+1]!='\n':
#            print('next i:', i+1, 'next line:', data[i+1].strip())
            l = l.strip() + ' ' + data[i+1].strip()
#            print('concat:', l)
            i+=1
#    print('final l:', l)
    f.write(l+'\n')
    count = l.count(':')
    if 'cid' in l:
        if count == 8:
            valid +=1
    elif count == 7:
        valid += 1
#    print('i:', i, 'count:', count, 'valid:', valid, 'complete l:', l)
    i+=1
f.close()

print('valid: ', valid)

# write cleaned data to text
fp2 = open('2020_day4a.txt', 'w')
i = 0
 #   print('current line:', data[i])
while i < len(data):
    l = data[i].strip()
#    print('current i:', i, l)  
    while i+1<len(data) and data[i+1]!='\n':
#            print('next i:', i+1, 'next line:', data[i+1].strip())
        l = l.strip() + ' ' + data[i+1].strip()
#            print('concat:', l)
        i+=1
    fp2.write(l.strip()+'\n')
    i+=1
#    print(' ')   
fp2.close()

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

fp = open('2020_day4a.txt', 'r')           
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
    t1 = 'cm' in x
    t2 = 'in' in x
    t3 = False
    t4 = False
    if t1:
        t3 = int(x.rstrip('cm')) in hgtcm_range
    if t2:
        t4 = int(x.rstrip('in')) in hgtin_range
    return (t1 or t2) and (t3 or t4)
 
# initialize test results 
T1 = False
T2 = False
T3 = False
T4 = False
T5 = False
T6 = False
T7 = False
T8 = False
byr = []
iyr = []
eyr = []
ecl = []
pid = []
hcl = []
hgt = []

# execute tests
valid_count = 0  
i = 0
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
    T8 = T1 and T2 and T3 and T4 and T5 and T6 and T7
    if T8 == True:
        valid_count +=1

#    print('i:', i, j)
#    print('byr:', byr, T1, 'iyr:', iyr, T2, 'eyr:', eyr, T3, 
#          'ecl:', ecl, T4, 'pid:', pid, T5, 'hcl:', hcl, T6, 
#          'hgt:', hgt, T7)
#    print(T8, 'valid count =', valid_count)
#    print(' ')

    # reset results
    T1 = False
    T2 = False
    T3 = False
    T4 = False
    T5 = False
    T6 = False
    T7 = False
    byr = []
    iyr = []
    eyr = []
    ecl = []
    pid = []
    hcl = []
    hgt = []

print('valid count =', valid_count)

    

    
