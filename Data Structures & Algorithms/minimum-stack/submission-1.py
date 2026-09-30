class MinStack:

    def __init__(self):
        self.extra_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.extra_stack) > 0:
            curr_min = self.extra_stack[len(self.extra_stack) - 1]
            if val < curr_min:
                self.extra_stack.append(val)
            else:
                smallest = self.extra_stack[len(self.extra_stack) - 1]
                self.extra_stack.append(smallest)
                print(self.extra_stack)
        else:
            self.extra_stack.append(val)

    def pop(self) -> None:
        #if self.extra_stack[len(self.extra_stack) - 1] == self.stack[len(self.stack) - 1]:
            
        self.stack.pop()
        self.extra_stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        return self.extra_stack[len(self.extra_stack) - 1]

        
