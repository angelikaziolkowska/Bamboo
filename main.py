subtaskId = 4
growthRate = [1, 1, 2, 3, 5, 8, 13, 21]

# Dont change anything above this line
# ===================================

#             0  1  2  3  4  5   6   7
# FIBONACCI
username = "hsaziolk"

queue = [7, 6, 5, 7, 4, 6, 7, 5,
         7, 2, 6, 7, 3, 5, 7, 6,
         4, 7, 1, 6, 7, 5, 4, 7,
         6, 5, 7, 3, 7, 6, 5, 7,
         4, 6, 7, 2, 6, 7, 5, 3,
         7, 6, 4, 7, 6, 5, 7, 0]


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
