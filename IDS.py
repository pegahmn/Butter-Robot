import numpy as np
from Node import Node
from Environment import Environment
from Agent import Agent
from SetCompare import Compare
from GetBPR import GetBPRPosition
from stack01 import Stack

def IDS(Root: Node,Agent: Agent,PointPosition:list):
    stack=Stack()
    limit=0
    
    while True:
        stack.push(Root)
        Agent.resetSeen()
        max_depth=0
        while True:
            if stack.is_empty():
                break
            node=stack.pop()
            node:Node
            if Compare(node.posBs,PointPosition):
                return node
            if node.depth<limit:
                childs=Agent.successor(node)
                for child in childs:
                    stack.push(child)
            if node.depth>max_depth:
                max_depth=node.depth
            
        if limit>max_depth:
            return None
        
        limit+=1