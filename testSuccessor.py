import numpy as np
from Node import Node
from Environment import Environment
from Agent import Agent

state = np.asarray(
    [['x', 'x', 'x', 'x', 'x'],
    ['x', '1', '2b', '1p', 'x'],
    ['1', '1p', '2', '1r', '1b'],
    ['1', '1', '2', '1', '1']], dtype= np.str_
)

table = np.asarray(
    [
        ['x', 'x', 'x', 'x', 'x'],
        ['x', '1', '2', '1', 'x'],
        ['1', '1', '2', '1', '1'],
        ['1', '1', '2', '1', '1']
    ]
)

posPs = [[2, 1], [1, 3]]
posBs = [[1, 2], [2, 4]]
posR = [2, 3]

env = Environment(table, posPs)
agent = Agent(env)
root = Node(posR, posBs)
childs = agent.successor(root)

print(childs)

for child in childs:
    print(f"move = {child.move}")
    print(f"depth = {child.depth}")
    print(f"cost = {child.g}")
    for i in range(table.shape[0]):
        print(end= "\t")
        for j in range(table.shape[1]):
            cell = table[i, j]
            cell += 'p' if [i, j] in posPs else ''
            cell += 'b' if [i, j] in child.posBs else ''
            cell += 'r' if [i, j] == child.posR else ''
            print(cell, end= "\t")
        print()
    print("---------------------------------------------")