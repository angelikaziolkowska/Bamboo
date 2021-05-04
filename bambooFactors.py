subtaskId = 3
growthRate = [1, 2, 3, 4, 12]

# Dont change anything above this line
# ===================================

# FACTORS
username = "hsaziolk"

# initial drawing of tree:
# 4-4-4-4-4-4-4-4-4-4-4
# -3-----3-----3-----3-
# ---2-------2-----2---
# -----1---------1-----
# ---------0-----------

le = len(growthRate)

queue = []
# smallest two nums sporadically appended
for i in range(1, -1, -1):
    # largest with second/third largest appended
    for j in range(le-2, 1, -1):
        queue.append(le-1)
        queue.append(j)
    queue.append(le-1)
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
