import numpy as np

def GoalTest(ButterPosition:list,PointPosition:list):
    for Butter in ButterPosition:
        if Butter not in PointPosition:
            return False
    for Point in PointPosition:
        if Point not in ButterPosition:
            return False
            
    return True
#------------------------------------------------
Test=GoalTest([[1,0], [2,3]],[[2,3], [1,0]])
print(Test)

# [[1,0], [2,3]]
# [[2,3], [1,0]]
# #output is True



