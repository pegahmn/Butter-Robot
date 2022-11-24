import numpy as np
from Node import Node
from Environment import Environment
from Agent import Agent
from SetCompare import Compare
from GetBPR import GetBPRPosition
from MinHeapTree import MHT

state = np.asarray(
    [['x', 'x', 'x', 'x', 'x'],
    ['x', '1', '2b', '1p', 'x'],
    ['1', '1p', '2b', '1r', '1'],
    ['1', '1', '2', '1', '1']], dtype= np.str_
)


ButterPosition, RobotPosition, PointPosition=GetBPRPosition(state)
env = Environment(state, PointPosition)
agent = Agent(env)
root = Node(RobotPosition[0], ButterPosition)

def UCS(Root: Node,Agent: Agent,PointPosition:list):
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
            mht.push(child)

Answer=UCS(root,agent,PointPosition)
if Answer==None:
    print("There is no answer")
else:
    node = Answer
    Moves = []
    while node != None:
        Moves.append(node.move)
        node = node.parent

    print("Moves: ")
    for i in range(len(Moves)-1,-1,-1):
        print(f"{Moves[i]} ", end='')

    print(f"depth = {Answer.depth}")
    print(f"cost = {Answer.g}")
    for i in range(state.shape[0]):
        print(end= "\t")
        for j in range(state.shape[1]):
            cell = state[i, j]
            cell += 'p' if [i, j] in PointPosition else ''
            cell += 'b' if [i, j] in Answer.posBs else ''
            cell += 'r' if [i, j] == Answer.posR else ''
            print(cell, end= "\t")
        print()
    print("---------------------------------------------")