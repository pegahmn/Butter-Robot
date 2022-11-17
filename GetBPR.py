import numpy as np
def GetBPRPosition(State: np.ndarray): #Get Position of Robot and Butter and Point
    Shape=State.shape #Tupple 
    ButterPosition=list()
    RobotPosition=list()
    PointPosition=list()
    for i in range (Shape[0]):
        for j in range (Shape[1]):
            if 'b' in State[i,j]:
                ButterPosition.append([i, j])
                State[i,j]=State[i,j].replace("b","")
            if "r" in State[i,j]:
                RobotPosition.append([i,j])
                State[i,j]=State[i,j].replace("r","")
            if "p" in State[i,j]:
                PointPosition.append([i,j])
                State[i,j]=State[i,j].replace("p","")
    return ButterPosition, RobotPosition, PointPosition
                
                
# state = np.asarray([
#     ["1", "2", "3"],
#     ["2b", "4p", "5r"]
# ])
# A=GetButterPosition(state)
# print(A)
# print(state)
# # ([[1, 0]], [[1, 2]], [[1, 1]])
# [['1' '2' '3']
#  ['2' '4' '5']]