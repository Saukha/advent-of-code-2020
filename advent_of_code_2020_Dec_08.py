# advent of code: Dec 8, 2020 
# Part 1
import pandas as pd

df = pd.read_csv('12082020adventofcode.txt', sep=' ', 
                 header=None, names=['Instruction', 'Argument'])

ind_list = list(range(0, len(df)))
ind_flip = []
acc_value = 0
ind = 0
copy_ind = 0

def acc(arg):
    global acc_value
    acc_value += arg
    global ind
    ind += 1

def jmp(arg):
    global ind
    ind += arg
    
def nop(arg):
    global ind
    ind += 1
    
while ind in ind_list:
    copy_ind = ind
    instr = df.loc[ind,'Instruction']
    argu = df.loc[ind,'Argument']
    ind_list.remove(ind)
    global ind_flip
    ind_flip.append(ind)
    if instr == 'acc':
        acc(argu)
    elif instr == 'jmp':
        jmp(argu)
    elif  instr == 'nop':
        nop(argu)

print('Part 1:')
print('final acc_value:', acc_value)
print('last run ind:', copy_ind)
print(df.loc[copy_ind,:])
print('ind_flip for part 2:', ind_flip)
print('##############################################')


# part 2
# reset variables
ind_list = list(range(0, len(df)))
acc_value = 0
ind = 0
copy_ind = 0

def flip(row):
    instru = df.loc[row,'Instruction']
    if instru == 'jmp':
        df.loc[row,'Instruction'] = 'nop'
    elif instru == 'nop':
        df.loc[row,'Instruction'] = 'jmp'

def while_loop(x):
    global ind
    ind = x
    while ind in ind_list:
        instr = df.loc[ind,'Instruction']
        argu = df.loc[ind,'Argument']
        global copy_ind
        copy_ind = ind
        ind_list.remove(ind)
        if instr == 'acc':
            acc(argu)
        elif instr == 'jmp':
            jmp(argu)
        elif  instr == 'nop':
            nop(argu)

for i in ind_flip:
    flip(int(i))
    while_loop(ind)
    flip(int(i))
    if copy_ind == len(df)-1:
        break
    ind_list = list(range(0, len(df)))
    acc_value = 0
    ind = 0
    copy_ind = 0  

print('Part 2:')
print('last run ind:', copy_ind)
print('final acc_value:', acc_value)  
print(df.loc[copy_ind,:])
print('##############################################')
