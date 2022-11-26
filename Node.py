from SetCompare import Compare
class Node:
    posR: list[int]
    posBs: list[list[int]]
    move: str
    depth: int
    g: int
    h: int

    def __init__(self, posR, posBs, parent=None, move= '', depth= 0, g= 0, h= 0) -> None:
        self.parent = parent
        self.posR = posR
        self.posBs = posBs
        self.move = move
        self.depth = depth
        self.g = g
        self.h = h

    def __eq__(self, __o: object) -> bool:
        return type(__o) == Node and Compare(self.posBs,__o.posBs) and self.posR == __o.posR

    def __hash__(self) -> int:
        h = hash((self.depth, self.g, self.h, self.move))
        h = hash((h, self.posR[0], self.posR[1]))
        for pos in self.posBs:
            h = hash((h, pos[0], pos[1]))
        return h

    def __gt__(self, __o):
        return (self.g + self.h) > (__o.g + __o.h)

    def __lt__(self, __o):
        return __o.__gt__(self)
