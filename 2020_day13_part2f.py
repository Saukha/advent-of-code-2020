# 2020 day 13 part 2 version f

# inputs
L_earliest = 100000000000000
# buses   = [ 19, 37, 883, 23, 13, 17, 797, 41, 29]
# offsets = [  0, 13,  19, 27, 32, 36,  50, 60, 79]
# max(buses) = 883
# bus 19 will take off again when 883 takes off
# similarly buses 17, 41, 13 would have taken off with 883 before 
#    taking off at their next departures at offset time

start = (L_earliest//(883*19*17*41*13)+1)*883*19*17*41*13
end   = start*200

#t0 = (i   -19)%19  ==0  # bus 19
#t1 = (i+13-19)%37  ==0  # bus 37
#t2 = (i+19-19)%883 ==0  # bus 883
#t3 = (i+27-19)%23  ==0  # bus 23
#t4 = (i+32-19)%13  ==0  # bus 13
#t5 = (i+36-19)%17  ==0  # bus 17
#t6 = (i+50-19)%797 ==0  # bus 797
#t7 = (i+60-19)%41  ==0  # bus 41
#t8 = (i+79-19)%29  ==0  # bus 29

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
        print('part 2: Offset departures starts with bus 19 at', i-19)
        break

