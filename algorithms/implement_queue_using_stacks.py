class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tmp = []
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack:
            self.tmp.append(self.stack.pop())
        self.tmp.append(x)
        while self.tmp:
            self.stack.append(self.tmp.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0
