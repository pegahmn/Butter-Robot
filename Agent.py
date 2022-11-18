import numpy as np
from Node import Node
from Environment import Environment

class Agent:
    env: Environment
    seen = []
    MOVES = {
        'R' : (0, 1),
        'U' : (1, 0),
        'L' : (0, -1),
        'D' : (-1, 0)
    }

    def __init__(self, env: Environment) -> None:
        self.env = env

    def isInTable(self, pos: list, table: np.ndarray) -> bool:
        if pos[0] < 0 or table.shape[0] <= pos[0]:
            return False

        if pos[1] < 0 or table.shape[1] <= pos[1]:
            return False

        return True

    def isValidMove(self, node: Node, move: str) -> bool:
        up, right = self.MOVES[move]

        newPos = [node.posR[0] + up, node.posR[1] + right]
        table = self.env.table
        
        if not self.isInTable(newPos, table):
            return False

        if  table[newPos[0], newPos[1]] == 'x':
            return False

        if newPos in node.posBs:
            if newPos in self.env.posPs:
                return False

            frontPos = [(newPos[0] if node.posR[0]==newPos[0] else (2 * newPos[0] - node.posR[0])),
                    (newPos[1] if node.posR[1]==newPos[1] else (2 * newPos[1] - node.posR[1]))]

            if not self.isInTable(frontPos, table):
                return False

            if  table[newPos[0], newPos[1]] == 'x':
                return False
            
            if frontPos in node.posBs:
                return False
            
        return True

    def getChilde(self, node: Node, move: str) -> Node:
        up, right = self.MOVES[move]

        newPos = [node.posR[0] + up, node.posR[1] + right]
        g = int(self.env.table[newPos[0], newPos[1]]) + node.g
        
        if newPos in node.posBs:
            PosBs = node.posBs.copy()
            Index = PosBs.index(newPos)
            PosBs[Index][0] += up
            PosBs[Index][1] += right
        else:
            PosBs = node.posBs

        return Node(self.env.table, newPos, self.env.posPs, PosBs, move, node.depth+1, g)

    def successor(self, node: Node) -> list[Node]:
        Childs = []

        for move in self.MOVES.keys():
            if self.isValidMove(node, move) and node in self.seen:
                Childs.append(self.getChilde(node, move))
        
        self.seen.append(node)
        return Childs