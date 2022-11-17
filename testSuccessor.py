import numpy as np
from Successor import successor, Node

state = np.asarray(
    [['x', 'x', 'x', 'x', 'x'],
    ['x', '1p', '2b', '1p', 'x'],
    ['1', '1', '2b', '1', '1'],
    ['1', '1', '2', '1', '1']], dtype= np.str_
)
pos = [2, 1]
cost = 0

childs = successor(Node(state, pos, cost))

for child in childs:
    for row in child.state:
        print(end= "\t")
        for ch in row:
            print(ch, end= "\t")
        print()
    print(f"robot pos = {child.robotPos}")
    print(f"cost = {child.cost}")
    print("--------------------")