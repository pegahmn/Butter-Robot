from data_structures import *
from agent import *
from algorithms import *
from state import *

state = np.asarray(
    [['1r','1', '1', '1',  'x', 'x', '1', '1', '1', '1'],
    [ '1', 'x', '1', '1',  '2', '2', '1', '1', '1', '1'],
    [ 'x', '1', '1', '2b', '2', '2', '2b','1', 'x', 'x'],
    [ 'x', '1', '1', 'x',  'x', '2', '2', '1', '1p','x'],
    [ '1', '1', '1', '1',  '2', '2', '1', '1', '1', '1'],
    [ '1', '1', '1', '1',  'x', '1p','x', '1', '1', '1']], dtype= np.str_
)

# state = []

# n, m = (int(x) for x in input().split())

# for i in range(n):
#     state.append(input().split())

# state = np.asarray(state)

algorithms = [DFS, BFS, UCS, IDS, A_star, Gready]

butterPositions, robotPositions, pointPositions=getBPRPositions(state)
env = Environment(state, pointPositions)
agent = Agent(env)
root = Node(robotPositions[0], butterPositions)

for algorithm in algorithms:
    agent.resetSeen()
    Answer=algorithm(root, agent, pointPositions)

    print("-------------- " + algorithm.__name__ + " --------------")
    if Answer==None:
        print("can't pass the butter")
    else:
        node = Answer
        Moves = []
        while node != None:
            Moves.append(node.move)
            node = node.parent

        for i in range(len(Moves)-2,-1,-1):
            print(Moves[i], end=' ')

        print()
        print(Answer.g)
        print(Answer.depth)