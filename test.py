import numpy as np
from Node import Node
from Environment import Environment
from Agent import Agent
from GetBPR import GetBPRPosition
from DFS import DFS
from BFS import BFS
from UCS import UCS
from A_star import A_star
from Gready import Gready

Algorithms = [UCS, BFS, DFS, A_star, Gready]

for algoritm in Algorithms:
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

    Answer=algoritm(root, agent,PointPosition)
    print("--------------" + algoritm.__name__ + "--------------")

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