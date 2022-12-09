from state import *

class CheckerType:
    PATH_CHECK = 1
    CYCLE_CHECK = 2
class Agent:
    env: Environment
    seen = set()
    MOVES = {
        'R' : (0, 1),
        'U' : (-1, 0),
        'L' : (0, -1),
        'D' : (1, 0)
    }
    
    def __init__(self, env: Environment) -> None:
        self.env = env

    def isInTable(self, pos: Position) -> bool:
        if pos.row < 0 or self.env.table.shape[0] <= pos.row:
            return False

        if pos.col < 0 or self.env.table.shape[1] <= pos.col:
            return False

        return True

    def isValidMove(self, node: Node, move: str) -> bool:
        up, right = Agent.MOVES[move]

        newPos = Position(node.posR.row + up, node.posR.col + right)
        table = self.env.table
        
        if not self.isInTable(newPos):
            return False

        if  table[newPos.row, newPos.col] == 'x':
            return False

        if newPos in node.posBs:
            if newPos in self.env.posPs:
                return False

            frontPos = Position(newPos.row + up, newPos.col + right)

            if not self.isInTable(frontPos):
                return False

            if  table[frontPos.row, frontPos.col] == 'x':
                return False
            
            if frontPos in node.posBs:
                return False
            
        return True

    def getChilde(self, node: Node, move: str) -> Node:
        up, right = Agent.MOVES[move]

        newPos = Position(node.posR.row + up, node.posR.col + right)
        g = int(self.env.table[newPos.row, newPos.col]) + node.g
        
        if newPos in node.posBs:
            PosBs = []
            for i in range(len(node.posBs)):
                if node.posBs[i] == newPos:
                    PosBs.append(node.posBs[i].copy())
                    PosBs[i].row += up
                    PosBs[i].col += right
                else:
                    PosBs.append(node.posBs[i])
        else:
            PosBs = node.posBs

        return Node(newPos, PosBs, node, move, node.depth+1, g)

    def resetSeen(self):
        self.seen.clear()

    def d(self, pos1: Position, pos2: Position):
        return abs(pos1.row - pos2.row) + abs(pos1.col - pos2.col)

    def h(self, pos: Position, posList: list[Position]):
        minIndex = 0
        minDistance = self.d(pos, posList[0])
        for i in range(1, len(posList)):
            distance = self.d(pos, posList[i])
            if distance < minDistance:
                minIndex = i
                minDistance = distance

        return minDistance, minIndex

    def H(self, node: Node) -> int:
        PosBs = node.posBs.copy()
        PosPs = self.env.posPs.copy()
        PosR = node.posR

        H = 0
        while PosBs != []:
            nearestB, indexB = self.h(PosR, PosBs)
            PosR = PosBs.pop(indexB)

            nearestP, indexP = self.h(PosR, PosPs)
            PosR = PosPs.pop(indexP)
            
            H += nearestB + nearestP
        
        return H

    def isSeenNode(self, node: Node, checkerType: int = CheckerType.CYCLE_CHECK) -> bool:
        if checkerType == CheckerType.CYCLE_CHECK:
            if node in self.seen:
                return True
            self.seen.add(node)
            return False

        if checkerType == CheckerType.PATH_CHECK:
            if node.parent == None:
                node.seen = set()
            else:
                node.seen = node.parent.seen.copy()
                node.seen.add(node.parent)
            if node in node.seen:
                return True
            return False

        raise Exception(f'not valid CheckerType: {checkerType}')

    def successor(self, node: Node) -> list[Node]:
        Childs = []

        for move in Agent.MOVES.keys():
            if self.isValidMove(node, move):
                childe = self.getChilde(node, move)
            
                Childs.append(childe)

        return Childs