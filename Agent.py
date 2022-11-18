import numpy as np
from Node import Node
from Environment import Environment

class Agent:
    env: Environment
    seen = []
    MOVES = {
        'R' : (0, 1),
        'U' : (-1, 0),
        'L' : (0, -1),
        'D' : (1, 0)
    }

    def __init__(self, env: Environment) -> None:
        self.env = env

    def isInTable(self, pos: list) -> bool:
        if pos[0] < 0 or self.env.table.shape[0] <= pos[0]:
            return False

        if pos[1] < 0 or self.env.table.shape[1] <= pos[1]:
            return False

        return True

    def isValidMove(self, node: Node, move: str) -> bool:
        up, right = Agent.MOVES[move]

        newPos = [node.posR[0] + up, node.posR[1] + right]
        table = self.env.table
        
        if not self.isInTable(newPos):
            return False

        if  table[newPos[0], newPos[1]] == 'x':
            return False

        if newPos in node.posBs:
            if newPos in self.env.posPs:
                return False

            frontPos = [newPos[0] + up, newPos[1] + right]

            if not self.isInTable(frontPos):
                return False

            if  table[newPos[0], newPos[1]] == 'x':
                return False
            
            if frontPos in node.posBs:
                return False
            
        return True

    def getChilde(self, node: Node, move: str) -> Node:
        up, right = Agent.MOVES[move]

        newPos = [node.posR[0] + up, node.posR[1] + right]
        g = int(self.env.table[newPos[0], newPos[1]]) + node.g
        
        if newPos in node.posBs:
            PosBs = []
            for i in range(len(node.posBs)):
                PosBs.append(node.posBs[i].copy())
                if PosBs[i] == newPos:
                    PosBs[i][0] += up
                    PosBs[i][1] += right
        else:
            PosBs = node.posBs

        return Node(newPos, PosBs, move, node.depth+1, g)

    def successor(self, node: Node) -> list[Node]:
        Childs = []

        for move in Agent.MOVES.keys():
            if self.isValidMove(node, move):
                childe = self.getChilde(node, move)
                if childe not in self.seen:
                    Childs.append(childe)
        
        self.seen.append(node)
        return Childs