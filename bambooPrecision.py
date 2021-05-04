subtaskId = 5
growthRate = [1000, 1999, 2001]

# Dont change anything above this line
# ===================================

# PRECISION
username = "hsaziolk"

# both work-> many orderings work
queue = [0, 1, 2]
# queue = [2, 1, 0]

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
