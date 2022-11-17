import numpy as np

class Node:
    state: np.ndarray(0)
    PosR: list[int]
    PosPs: list[list[int]]
    PosBs: list[list[int]]
    move: str
    depth: int
    g: int
    h: float

    def __init__(self, state, posR, posPs, posBs, move, depth, g, h= None) -> None:
        self.state = state
        self.PosR = posR
        self.PosPs = posPs
        self.PosBs = posBs
        self.move = move
        self.depth = depth
        self.g = g
        self.h = h

def isInTable(pos: list, state: np.ndarray) -> bool:
    if pos[0] < 0 or state.shape[0] <= pos[0]:
        return False

    if pos[1] < 0 or state.shape[1] <= pos[1]:
        return False

    return True

def isValidMove(node: Node, move: str) -> bool:
    up, right = {
        'R' : (0, 1),
        'U' : (1, 0),
        'L' : (0, -1),
        'D' : (-1, 0)
    }[move]

    newPos = [node.PosR[0] + up, node.PosR[1] + right]
    state = node.state
    
    if not isInTable(newPos, state):
        return False

    if  state[newPos[0], newPos[1]] == 'x':
        return False

    if newPos in node.PosBs:
        if newPos in node.PosPs:
            return False

        frontPos = [(newPos[0] if node.PosR[0]==newPos[0] else (2 * newPos[0] - node.PosR[0])),
                (newPos[1] if node.PosR[1]==newPos[1] else (2 * newPos[1] - node.PosR[1]))]

        if not isInTable(frontPos, state):
            return False

        if  state[newPos[0], newPos[1]] == 'x':
            return False
        
        if frontPos in node.PosBs:
            return False
        
    return True

def cycleCheck(node: Node) -> bool:
    pass

def getChilde(node: Node, move: str) -> Node:
    up, right = {
        'R' : (0, 1),
        'U' : (1, 0),
        'L' : (0, -1),
        'D' : (-1, 0)
    }[move]

    newPos = [node.PosR[0] + up, node.PosR[1] + right]
    g = int(node.state[newPos[0], newPos[1]]) + node.g
    
    if newPos in node.PosBs:
        PosBs = node.PosBs.copy()
        Index = PosBs.index(newPos)
        PosBs[Index][0] += up
        PosBs[Index][1] += right
    else:
        PosBs = node.PosBs

    return Node(node.state, newPos, node.PosPs, PosBs, move, node.depth+1, g)

def successor(node: Node, Seen: list[Node]) -> list[Node]:
    Childs = []

    MOVES = ['R', 'U', 'L', 'D']
    for move in MOVES:
        if isValidMove(node, move):
            Childs.append(getChilde(node, move))
    
    return Childs