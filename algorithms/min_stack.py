import math


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(min(self.min[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return int(self.min[-1])
