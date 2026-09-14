class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            minval = val
        else:
            curmin = self.stack[-1][1]
            minval = min(val, curmin)
        
        self.stack.append((val, minval))

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


        
