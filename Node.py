from SetCompare import Compare
class Node:
    posR: list[int]
    posBs: list[list[int]]
    move: str
    depth: int
    g: int
    h: float

    def __init__(self, posR, posBs, move= '', depth= 0, g= 0, h= None) -> None:
        self.posR = posR
        self.posBs = posBs
        self.move = move
        self.depth = depth
        self.g = g
        self.h = h

    def __eq__(self, __o: object) -> bool:
        return type(__o) == Node and Compare(self.posBs,__o.posBs) and self.posR == __o.posR