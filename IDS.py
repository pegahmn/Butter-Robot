import numpy as np
from Node import Node
from Environment import Environment
from Agent import Agent, CheckerType
from SetCompare import Compare
from GetBPR import GetBPRPosition
from stack01 import Stack

def IDS(Root: Node,Agent: Agent,PointPosition:list):
    limit=0
    while True: #()
        stack=Stack()
        stack.push(Root)
        Agent.resetSeen()
        max_depth=0
        while True:
            if stack.is_empty():
                break
            node=stack.pop()

            if limit == 18:
                Moves = []
                nodeKeeper = node
                while nodeKeeper != None:
                    Moves.append(nodeKeeper.move)
                    nodeKeeper = nodeKeeper.parent

                for i in range(len(Moves)-2,-1,-1):
                    print(Moves[i], end=' ')

                cm = ['R', 'R', 'D', 'D', 'R', 'R', 'U', 'R', 'R', 'D', 'U', 'L', 'D', 'D', 'D', 'U', 'R', 'R']
                
                print(end= '\n')

                for i in range(len(Moves)-1):
                    if cm[i] == Moves[-(i+2)]:
                        print('+', end = ' ')
                    else:
                        print('-', end= ' ')

                print()


            if Compare(node.posBs,PointPosition):
                return node
            if node.depth<limit:
                childs=Agent.successor(node, CheckerType.PATH_CHECK)
                for child in childs:
                    stack.push(child)
            if node.depth>max_depth:
                max_depth=node.depth
            
        if limit>max_depth:
            return None
            
        limit+=1