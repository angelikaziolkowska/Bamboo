subtaskId = 4
growthRate = [1, 1, 2, 3, 5, 8, 13, 21]

# Dont change anything above this line
# ===================================

# FIBONACCI
username = "hsaziolk"

# tree structure initial idea:
# |7--7--7-7--7--7--7--7--7--7-7--7--7--7--7--7--7-|
# |-6---6----6----6---6----6----6---6--6----6--6---|
# |--5----5-----5-------5---5----5-------5------5--|
# |----4-----------4-----4---------4---------4-----|
# |------------3--------------3-----------3--------|
# |---------2-------------------------2------------|
# |------------------1-----------------------------|
# |-----------------------------------------------0|

queue = [7, 6, 5, 7, 4, 6, 7, 5,
         7, 2, 6, 7, 3, 5, 7, 6,
         4, 7, 1, 6, 7, 5, 4, 7,
         6, 5, 7, 3, 7, 6, 5, 7,
         4, 6, 7, 2, 6, 7, 5, 3,
         7, 6, 4, 7, 6, 5, 7, 0]

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
