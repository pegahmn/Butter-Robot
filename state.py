import numpy as np

class Position:
    row: int
    col: int

    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    def copy(self):
        return Position(self.row, self.col)

    def __hash__(self) -> int:
        return hash((self.row, self.col))

    def __eq__(self, __o: object) -> bool:
        return type(__o) == Position and self.row == __o.row and self.col == __o.col


class Node:
    posR: Position
    posBs: list[Position]
    move: str
    depth: int
    g: int
    h: int

    def __init__(self, posR, posBs, parent=None, move= '', depth= 0, g= 0, h= 0) -> None:
        self.parent = parent
        self.posR = posR
        self.posBs = posBs
        self.move = move
        self.depth = depth
        self.g = g
        self.h = h

    def __hash__(self) -> int:
        h = hash(self.posR)
        for pos in self.posBs:
            h = hash((h, pos))
        return h

    def __eq__(self, __o: object) -> bool:
        return type(__o) == Node and compare(self.posBs,__o.posBs) and self.posR == __o.posR

    def __gt__(self, __o):
        return (self.g + self.h) > (__o.g + __o.h)

    def __lt__(self, __o):
        return __o < self

class Environment:
    table: np.ndarray
    posPs: list[Position]

    def __init__(self, table, posPs) -> None:
        self.table = table
        self.posPs = posPs

def compare(A:list[Position],B:list[Position]):
    for butter in A:
        if butter not in B:
            return False

    for point in B:
        if point not in A:
            return False
            
    return True

def getBPRPositions(state: np.ndarray): #Get Position of Robot and Butter and Point
    shape=state.shape
    butterPositions=list()
    robotPosition=list()
    pointPositions=list()
    for i in range (shape[0]):
        for j in range (shape[1]):
            if 'b' in state[i,j]:
                butterPositions.append(Position(i, j))
                state[i,j]=state[i,j].replace("b","")
            if "r" in state[i,j]:
                robotPosition.append(Position(i, j))
                state[i,j]=state[i,j].replace("r","")
            if "p" in state[i,j]:
                pointPositions.append(Position(i, j))
                state[i,j]=state[i,j].replace("p","")
    return butterPositions, robotPosition, pointPositions