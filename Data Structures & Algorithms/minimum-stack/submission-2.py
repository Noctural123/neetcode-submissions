class MinStack:

    def __init__(self):
        self.store = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.store.append(val)

        if not self.minStack:
            self.minStack.append(val)
            return

        if val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.minStack.pop()
        return self.store.pop()

    def top(self) -> int:
        return self.store[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
