import numpy as np
from Node import Node
from Environment import Environment
from Agent import Agent
from SetCompare import Compare
from GetBPR import GetBPRPosition
from queue01 import Queue
from stack01 import Stack

def Gready(Root: Node,Agent: Agent,PointPosition:list):
    stack=Stack()
    stack.push(Root)
    while True:
        if stack.is_empty():
            return None
        state=stack.pop()
        if Compare(state.posBs,PointPosition):
            return state
        childs=Agent.successor(state)
        while childs != []:
            maxH = childs[0].h
            index = 0

            for i in range(1, len(childs)):
                if childs[i].h > maxH:
                    index = i
                    maxH = childs[i].h

            stack.push(childs.pop(index))