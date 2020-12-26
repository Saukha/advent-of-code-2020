# 2020 day5 part 1

def F(row):
    x, y = row
    y = y - (y - x - 1)/2 -1
    return (x, y)

def B(row):
    x, y = row
    x = x + (y - x -1)/2 + 1
    return (x, y)

def R(col):
    x, y = col
    x = x + (y - x -1)/2 + 1
    return (x, y)

def L(col):
    x, y = col
    y = y - (y - x - 1)/2 -1
    return (x, y)

def ID(row, col):
    return row*8+col

def find_seat(l):
    # initialize
    row=(0, 127) 
    col=(0, 7) 
    
    # find row
    for i in l[0:7]:
        if i=='F':
            row=F(row)
        elif i=='B':
            row=B(row)

    # find col
    for j in l[7:10]:
        if j=='L':
            col=L(col)
        elif j=='R':
            col=R(col)
    
    return [row[0], col[0], ID(row[0], col[0])]

with open('2020_day5.txt', 'r') as f:
    data = f.readlines()

max_id = 0
for l in data:
    seat = find_seat(l)
    if seat[2] > max_id:
        max_id = seat[2]
    
print('max ID:', int(max_id))

#############
# part 2
id_list = []
for l in data:
def F(row):
    x, y = row
    y = y - (y - x - 1)/2 -1
    return (x, y)

def B(row):
    x, y = row
    x = x + (y - x -1)/2 + 1
    return (x, y)

def R(col):
    x, y = col
    x = x + (y - x -1)/2 + 1
    return (x, y)

def L(col):
    x, y = col
    y = y - (y - x - 1)/2 -1
    return (x, y)

def ID(row, col):
    return row*8+col

def find_seat(l):
    # initialize
    row=(0, 127) 
    col=(0, 7) 
    
    # find row
    for i in l[0:7]:
        if i=='F':
            row=F(row)
        elif i=='B':
            row=B(row)

    # find col
    for j in l[7:10]:
        if j=='L':
            col=L(col)
        elif j=='R':
            col=R(col)
    
    # find ticket ID        
    id = ID(row[0], col[0])
    
    return [row[0], col[0], id]

with open('2020_day5.txt', 'r') as f:
    data = f.readlines()

max_id = 0
for l in data:
    seat = find_seat(l)
    if seat[2] > max_id:
        max_id = seat[2]
    
print('max ID:', int(max_id))

    if id_list[i+1]-id_list[i]!=1:
        print('my ticket id:', int(id_list[i]+1))


