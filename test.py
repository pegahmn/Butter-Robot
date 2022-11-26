import numpy as np
from Node import Node
from Environment import Environment
from Agent import Agent
from GetBPR import GetBPRPosition
from DFS import DFS
from BFS import BFS
from UCS import UCS
from IDS import IDS
from A_star import A_star
from Gready import Gready

# state = np.asarray(
#     [['x', 'x', 'x', 'x', 'x'],
#     ['x', '1', '2b', '1p', 'x'],
#     ['1', '1p', '2b', '1r', '1'],
#     ['1', '1', '2', '1', '1']], dtype= np.str_
# )

state = []

n, m = (int(x) for x in input().split())

for i in range(n):
    state.append(input().split())

state = np.asarray(state)

Algorithms = [DFS, BFS, UCS, IDS, A_star, Gready]

ButterPosition, RobotPosition, PointPosition=GetBPRPosition(state)
env = Environment(state, PointPosition)
agent = Agent(env)
root = Node(RobotPosition[0], ButterPosition)

for algoritm in Algorithms:
    agent.resetSeen()
    Answer=algoritm(root, agent, PointPosition)
    print("-------------- " + algoritm.__name__ + " --------------")

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