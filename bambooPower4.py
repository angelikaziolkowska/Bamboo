subtaskId = 2
growthRate = [3, 12, 48, 192, 768, 3072]

# Dont change anything above this line
# ===================================

# POWER4
username = "hsaziolk"

le = len(growthRate)
queue = [5 for i in range(le*2)]

for j in range(1, le*2, 2):
    if j < 7:
        queue[j] = int(le - j/2 -1)
    elif j == 7:
        queue[j] = int(le - 2)
    else:
        queue[j] = int(le - j/2)

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
