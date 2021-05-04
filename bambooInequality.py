subtaskId = 1
growthRate = [2000, 1, 1]

# Dont change anything above this line
# ===================================

# INEQUALITY
username = "hsaziolk"

growthRate = sorted(growthRate, reverse=True)

queue = []
# if one value is bigger than the sum of all other values
if growthRate[0] > sum(growthRate[1:]):
    for i in range(len(growthRate)-1, 0, -1):
        queue.append(0)
        queue.append(i)

print('queue:', queue)

# ====================================
# Dont change anything below this line

from collections import deque

solution = deque()
# add each element to the solution
for i in queue:
    solution.append(i)

import bamboo

# records your solution
bamboo.calculateRatio(growthRate, solution, username, subtaskId)