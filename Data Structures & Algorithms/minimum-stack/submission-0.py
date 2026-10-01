class MinStack:
    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, val: int) -> None:
        if len(self.min_s) == 0 or self.min_s[-1] >= val:
            self.min_s.append(val)
        self.s.append(val)

    def pop(self) -> None:
        val = self.s.pop()
        if len(self.min_s) and self.min_s[-1] == val:
            self.min_s.pop() 

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]
