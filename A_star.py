import numpy as np
from Node import Node
from Environment import Environment
from Agent import Agent
from SetCompare import Compare
from GetBPR import GetBPRPosition
from MinHeapTree import MHT

def A_star(Root: Node,Agent: Agent,PointPosition:list):
    mht=MHT()
    mht.push(Root)
    while True:
        if mht.is_empty():
            return None
        state=mht.pop()
        if Compare(state.posBs,PointPosition):
            return state
        childs=Agent.successor(state)
        for child in childs:
            child.h = Agent.H(child)
            mht.push(child)