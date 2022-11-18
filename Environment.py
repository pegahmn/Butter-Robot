import numpy as np

class Environment:
    table: np.ndarray
    posPs: list[list[int]]

    def __init__(self, table, posPs) -> None:
        self.table = table
        self.posPs = posPs