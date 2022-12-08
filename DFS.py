import numpy as np
from Node import Node
from Environment import Environment
from Agent import Agent
from SetCompare import Compare
from GetBPR import GetBPRPosition
from queue01 import Queue
from stack01 import Stack

def DFS(Root: Node,Agent: Agent,PointPosition:list):
    stack=Stack()
    stack.push(Root)
    while True:
        if stack.is_empty():
            return None
        state=stack.pop()
        if Compare(state.posBs,PointPosition):
            return state
        childs=Agent.successor(state)
        for child in childs:
            stack.push(child)