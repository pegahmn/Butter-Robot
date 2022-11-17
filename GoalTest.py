import numpy as np

def GoalTest(ButterPosition:list,PointPosition:list):
    ButterPosition=set()
    PointPosition=set()
    if ButterPosition == PointPosition:
        return True
    else:
        return False
#------------------------------------------------
# Test=GoalTest([[1,0], [2,3]],[[2,3], [1,0]])
# print(Test)

# # [[1,0], [2,3]]
# # [[2,3], [1,0]]
# # #output is True

