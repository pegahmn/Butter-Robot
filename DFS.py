import numpy as np
from Node import Node
from Environment import Environment
from Agent import Agent
from SetCompare import Compare
from GetBPR import GetBPRPosition
from queue01 import Queue
from stack01 import Stack

state = np.asarray(
    [['1r','1', '1', '1', 'x', 'x', '1', '1','1','1'],
     ['1', 'x', '1', '1', '2', '2', '1', '1','1','1'],
     ['x', '1', '1', '2b','2', '2', '2b','1','x','x'],
     ['x', '1', '1', 'x', 'x', '2', '2', '1','1p','x'],
     ['1', '1', '1', '1', '2', '2', '1', '1','1','1'],
     ['1', '1', '1', '1', 'x', '1p', 'x','x','1','1']], dtype= np.str_
)
ButterPosition, RobotPosition, PointPosition=GetBPRPosition(state)
env = Environment(state, PointPosition)
agent = Agent(env)
root = Node(RobotPosition[0], ButterPosition)
i=0
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

Answer=DFS(root, agent, PointPosition)

if Answer==None:
    print("can't pass the butter")
else:
    node = Answer
    Moves = []
    while node != None:
        Moves.append(node.move)
        node = node.parent

    for i in range(len(Moves)-1,-1,-1):
        print(Moves[i], end=' ')

    print()
    print(Answer.g)
    print(Answer.depth)