import numpy as np

class Node:
    state: np.ndarray(0)
    PosR: list[int]
    PosPs: list[list[int]]
    PosBs: list[list[int]]
    move: str
    g: int
    h: float

    def __init__(self, state, posR, posPs, posBs, move, g, h= None) -> None:
        self.state = state
        self.PosR = posR
        self.PosPs = posPs
        self.PosBs = posBs
        self.move = move
        self.g = g
        self.h = h

def isValidPos(curPos: list, newPos: list, state: np.ndarray) -> bool:
    if newPos[0] < 0 or state.shape[0] <= newPos[0]:
        return False

    if newPos[1] < 0 or state.shape[1] <= newPos[1]:
        return False

    newPosVal = state[newPos[0], newPos[1]]

    if len(newPosVal) == 3:
        return False

    if  newPosVal == 'x':
        return False

    if len(newPosVal) == 1:
        return True

    if newPosVal[1] == 'p':
        return True

    frotPos = [(newPos[0] if curPos[0]==newPos[0] else (2 * newPos[0] - curPos[0])),
                (newPos[1] if curPos[1]==newPos[1] else (2 * newPos[1] - curPos[1]))
                ]
    if frotPos[0] < 0 or state.shape[0] <= frotPos[0]:
        return False

    if frotPos[1] < 0 or state.shape[1] <= frotPos[1]:
        return False

    frotPosVal = state[frotPos[0], frotPos[1]]
    if len(frotPosVal) == 3:
        return False
    
    if  frotPosVal == 'x':
        return False

    if len(frotPosVal) == 1:
        return True

    if frotPosVal[1] == 'p':
        return True
    
    return False

def getLeftState(state: np.ndarray, pos: list) -> Node:
    newPos = [pos[0], pos[1] - 1]
    newPosVal = state[newPos[0], newPos[1]]
    cost = int(newPosVal[0])

    if len(newPosVal) == 1 or newPosVal[1] == 'p':
        newState = state
    else:
        newState = state.copy()
        newState[newPos[0], newPos[1]] = newPosVal[0]
        newState[pos[0], pos[1] - 2] += "b"
    
    return Node(newState, newPos, cost)

def getRightState(state: np.ndarray, pos: list) -> Node:
    newPos = [pos[0], pos[1] + 1]
    newPosVal = state[newPos[0], newPos[1]]
    cost = int(newPosVal[0])

    if len(newPosVal) == 1 or newPosVal[1] == 'p':
        newState = state
    else:
        newState = state.copy()
        newState[newPos[0], newPos[1]] = newPosVal[0]
        newState[pos[0], pos[1] + 2] += "b"
    
    return Node(newState, newPos, cost)

def getUpState(state: np.ndarray, pos: list) -> Node:
    newPos = [pos[0] - 1, pos[1]]
    newPosVal = state[newPos[0], newPos[1]]
    cost = int(newPosVal[0])

    if len(newPosVal) == 1 or newPosVal[1] == 'p':
        newState = state
    else:
        newState = state.copy()
        newState[newPos[0], newPos[1]] = newPosVal[0]
        newState[pos[0] - 2, pos[1]] += "b"
    
    return Node(newState, newPos, cost)

def getDownState(state: np.ndarray, pos: list) -> Node:
    newPos = [pos[0] + 1, pos[1]]
    newPosVal = state[newPos[0], newPos[1]]
    cost = int(newPosVal[0])

    if len(newPosVal) == 1 or newPosVal[1] == 'p':
        newState = state
    else:
        newState = state.copy()
        newState[newPos[0], newPos[1]] = newPosVal[0]
        newState[pos[0] + 2, pos[1]] += "b"
    
    return Node(newState, newPos, cost)

def successor(node: Node) -> list[Node]:
    Childs = []

    state = node.state
    pos = node.RPos

    if isValidPos(pos, [pos[0], pos[1]+1], state):
        Childs.append(getRightState(state, pos))

    if isValidPos(pos, [pos[0]-1, pos[1]], state):
        Childs.append(getUpState(state, pos))

    if isValidPos(pos, [pos[0], pos[1]-1], state):
        Childs.append(getLeftState(state, pos))

    if isValidPos(pos, [pos[0]+1, pos[1]], state):
        Childs.append(getDownState(state, pos))
    
    return Childs