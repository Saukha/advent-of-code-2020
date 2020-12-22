# 2020 day 13 part 2 version e
# inputs
# buses   = [ 19, 37, 883, 23, 13, 17, 797, 41, 29]
# offsets = [  0, 13,  19, 27, 32, 36,  50, 60, 79]
# max(buses) = 883
L_earliest = 100000000000000
next_883_bus = L_earliest - L_earliest%883 + 883
start = (L_earliest//(883*19)+1)*883*19
end   = start*200

#t0 = (i   )%19  ==0  # 19
#t1 = (i+13)%37  ==0  # 37
#t2 = (i+19)%883 ==0  # 883
#t3 = (i+27)%23  ==0  # 23
#t4 = (i+32)%13  ==0  # 13
#t5 = (i+36)%17  ==0  # 17
#t6 = (i+50)%797 ==0  # 797
#t7 = (i+60)%41  ==0  # 41
#t8 = (i+79)%29  ==0  # 29

for i in range(start, end, 883*19):
    if   (i+31)%797!=0: # 797
        continue
    elif (i+41)%41!=0:  # 41
        continue
    elif (i-6)%37!=0:   # 37
        continue
    elif (i+60)%29!=0:  # 29
        continue
    elif (i+8)%23!=0:   # 23
        continue
    elif (i+17)%17!=0:  # 17
        continue
    elif (i+13)%13!=0:  # 13
        continue
    else:
        print('Offset departures starts with 1st bus at:', i)
        break