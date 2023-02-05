from Agent import *
from data_structures import *
from state import *

#Butter Number = k, Point= k, Table= m*n, max_depth = h, min_depth have solution = s
def DFS(root: Node,agent: Agent,pointPositions:list[Position]): #time in O(k^2 * 4^h) & space in O(4hk)
    stack=Stack()
    stack.push(root)
    while True:
        if stack.is_empty():
            return None
        state=stack.pop()
        if agent.isSeenNode(state, CheckerType.CYCLE_CHECK):
            continue
        if compare(state.posBs,pointPositions):
            return state
        childs=agent.successor(state)
        for child in childs:
            stack.push(child)

def BFS(root: Node,agent: Agent,pointPositions:list[Position]):# time in O(K^2 * 4^s) & space in O(k * 4^s)
    queue=Queue()
    queue.enqueue(root)
    while True:
        if queue.is_empty():
            return None
        state=queue.dequeue()
        if agent.isSeenNode(state, CheckerType.CYCLE_CHECK):
            continue
        if compare(state.posBs,pointPositions):
            return state
        childs=agent.successor(state)
        for child in childs:
            queue.enqueue(child)

def UCS(root: Node , agent: Agent, pointPositions: list[Position]): # time in O(k^2 * 4^h) & space in O(k * 4^h)
    mht=MHT()
    mht.push(root)
    while True:
        if mht.is_empty():
            return None
        state=mht.pop()
        if agent.isSeenNode(state, CheckerType.CYCLE_CHECK):
            continue
        if compare(state.posBs,pointPositions):
            return state
        childs=agent.successor(state)
        for child in childs:
            mht.push(child)

def IDS(root: Node,agent: Agent,pointPositions:list[Position]): # time in O(k^2 (4^s + 2*4^(s-1) + ... + s * 4^1 + s+1)) = O(k^2 * 4^s) & space in O(k * 4s)
    limit=0
    while True:
        stack=Stack()
        stack.push(root)
        agent.resetSeen()
        max_depth=0
        while True:
            if stack.is_empty():
                break
            state=stack.pop()
            if agent.isSeenNode(state, CheckerType.PATH_CHECK):
                continue
            if compare(state.posBs,pointPositions):
                return state
            if state.depth<limit:
                childs=agent.successor(state)
                for child in childs:
                    stack.push(child)
            if state.depth>max_depth:
                max_depth=state.depth
            
        if limit>max_depth:
            return None
            
        limit+=1

def Gready(root: Node,agent: Agent,pointPositions:list[Position]): #time in O(k^2 * 4^h) & space in O(4hk)
    stack=Stack()
    stack.push(root)
    while True:
        if stack.is_empty():
            return None
        state=stack.pop()
        if agent.isSeenNode(state, CheckerType.CYCLE_CHECK):
            continue
        if compare(state.posBs,pointPositions):
            return state
        childs=agent.successor(state)
        for child in childs:
            child.h=agent.H(child)

        while childs != []:
            maxH = childs[0].h
            index = 0

            for i in range(1, len(childs)):
                if childs[i].h > maxH:
                    index = i
                    maxH = childs[i].h

            stack.push(childs.pop(index))

def A_star(root: Node,agent: Agent,pointPositions:list[Position]): #time in O(k^2 * 4^h) & space in O(k * 4^h)
    mht=MHT()
    mht.push(root)
    while True:
        if mht.is_empty():
            return None
        state=mht.pop()
        if agent.isSeenNode(state, CheckerType.CYCLE_CHECK):
            continue
        if compare(state.posBs,pointPositions):
            return state
        childs=agent.successor(state)
        for child in childs:
            child.h = agent.H(child)
            mht.push(child)