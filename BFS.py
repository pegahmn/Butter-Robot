import numpy as np
from Node import Node
from Environment import Environment
from Agent import Agent
from SetCompare import Compare
from GetBPR import GetBPRPosition
from queue01 import Queue
from stack01 import Stack

def BFS(Root: Node,Agent: Agent,PointPosition:list):
    queue=Queue()
    queue.enqueue(Root)
    while True:
        if queue.is_empty():
            return None
        state=queue.dequeue()
        if Compare(state.posBs,PointPosition):
            return state
        childs=Agent.successor(state)
        for child in childs:
            queue.enqueue(child)