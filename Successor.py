import numpy as np

class Node:
    posR: list[int]
    posBs: list[list[int]]
    move: str
    depth: int
    g: int
    h: float

    def __init__(self, posR, posBs, move, depth, g, h= None) -> None:
        self.posR = posR
        self.posBs = posBs
        self.move = move
        self.depth = depth
        self.g = g
        self.h = h


class Environment:
    table: np.ndarray
    posPs: list[list[int]]

    def __init__(self, table, posPs) -> None:
        self.table = table
        self.posPs = posPs


class Agent:
    env: Environment
    seen = []
    MOVES = {
        'R' : (0, 1),
        'U' : (1, 0),
        'L' : (0, -1),
        'D' : (-1, 0)
    }

    def isInTable(self, pos: list, state: np.ndarray) -> bool:
        if pos[0] < 0 or state.shape[0] <= pos[0]:
            return False

        if pos[1] < 0 or state.shape[1] <= pos[1]:
            return False

        return True

    def isValidMove(self, node: Node, move: str) -> bool:
        up, right = self.MOVES[move]

        newPos = [node.posR[0] + up, node.posR[1] + right]
        state = node.state
        
        if not self.isInTable(newPos, state):
            return False

        if  state[newPos[0], newPos[1]] == 'x':
            return False

        if newPos in node.posBs:
            if newPos in self.env.PosPs:
                return False

            frontPos = [(newPos[0] if node.posR[0]==newPos[0] else (2 * newPos[0] - node.posR[0])),
                    (newPos[1] if node.posR[1]==newPos[1] else (2 * newPos[1] - node.posR[1]))]

            if not self.isInTable(frontPos, state):
                return False

            if  state[newPos[0], newPos[1]] == 'x':
                return False
            
            if frontPos in node.posBs:
                return False
            
        return True

    def getChilde(self, node: Node, move: str) -> Node:
        up, right = self.MOVES[move]

        newPos = [node.posR[0] + up, node.posR[1] + right]
        g = int(node.state[newPos[0], newPos[1]]) + node.g
        
        if newPos in node.posBs:
            PosBs = node.posBs.copy()
            Index = PosBs.index(newPos)
            PosBs[Index][0] += up
            PosBs[Index][1] += right
        else:
            PosBs = node.posBs

        return Node(node.state, newPos, node.PosPs, PosBs, move, node.depth+1, g)

    def successor(self, node: Node) -> list[Node]:
        Childs = []

        for move in self.MOVES.keys():
            if self.isValidMove(node, move) and node in self.seen:
                Childs.append(self.getChilde(node, move))
        
        self.seen.append(node)
        return Childs