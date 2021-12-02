import pandas as pd

data = pd.read_csv('/home/ollie/Documents/Github/advent_of_code_2021/day_2/puzzle_input.csv',header=None)
data = data[0].str.split(' ',expand=True)


#%%timeit

#Part One - V1

forward_sum = data[data[0] == 'forward'][1].astype(int).sum()
up_sum = data[data[0] == 'up'][1].astype(int).sum()
down_sum = data[data[0] == 'down'][1].astype(int).sum()

forward_sum * (down_sum-up_sum)



#%%timeit

#Part One - V2

data[1] = data[1].astype(int)
all_sums = data.groupby(0).sum()

all_sums.loc['forward',1] * (all_sums.loc['down',1] - all_sums.loc['up',1])


#%%timeit

#Part Two

aim=0
depth=0
horiz=0

for i in data.index:
    if data.loc[i,0] == 'forward':
        horiz += data.loc[i,1]
        depth += data.loc[i,1]*aim
    elif data.loc[i,0] == 'up':
        aim -= data.loc[i,1]
    elif data.loc[i,0] == 'down':
        aim += data.loc[i,1]

horiz*depth
