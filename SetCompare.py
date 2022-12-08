import numpy as np
#O(K^2)
def Compare(ButterPosition:list,PointPosition:list):
    for Butter in ButterPosition:
        if Butter not in PointPosition:
            return False
    for Point in PointPosition:
        if Point not in ButterPosition:
            return False
            
    return True
#------------------------------------------------
# Test=Compare([[1,0], [2,3]],[[2,3], [1,0]])
# print(Test)

# [[1,0], [2,3]]
# [[2,3], [1,0]]
# #output is True