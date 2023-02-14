class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        
    def push(self, x: int) -> None:
        while len(self.stack_1) != 0:
            self.stack_2.append(self.stack_1.pop())

        self.stack_1.append(x)
        while len(self.stack_2) != 0:
            self.stack_1.append(self.stack_2.pop())

    def empty(self):
        if len(self.stack_1) == 0:
            return True
        elif len(self.stack_1) != 0:
            return False

    def pop(self) -> int:
        if not self.empty():
            return self.stack_1.pop()

    def peek(self) -> int:
        if not self.empty():
            return self.stack_1[-1]
        else:
            print("The queue is empty!")


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
