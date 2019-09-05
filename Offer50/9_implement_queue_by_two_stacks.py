""" [利用栈实现队列](https://www.lintcode.com/problem/implement-queue-by-two-stacks/description?_from=ladder&&fromId=6)
利用两个栈实现队列, 主要考察的是栈的FILO和队列的FIFO特性
"""


class MyQueue:

    def __init__(self):
        self._q, self._stack = [], []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        self._q.append(element)

    """
    @return: An integer
    """

    def pop(self):
        if not self._q:
            return -1
        while self._q:
            self._stack.append(self._q.pop())
        val = self._stack.pop()
        while self._stack:
            self._q.append(self._stack.pop())
        return val

    """
    @return: An integer
    """

    def top(self):
        if not self._q:
            return -1
        while self._q:
            self._stack.append(self._q.pop())
        val = self._stack[-1]
        while self._stack:
            self._q.append(self._stack.pop())
        return val
