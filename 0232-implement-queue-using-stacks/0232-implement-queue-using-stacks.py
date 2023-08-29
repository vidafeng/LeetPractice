class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []
        

    def push(self, x: int) -> None:
        self.front.append(x)
        
# Remove element from front of the queue and return it 
    def pop(self) -> int:
        self.peek()
        return self.back.pop()


        
# Returns element at front of the queue
    def peek(self) -> int:
        if not self.back:
            while self.front:
                self.back.append(self.front.pop())

        return self.back[-1]


        
# returns true if the queue is empty
# returns false if otherwise
# not is boolean operator
    def empty(self) -> bool:
        return not self.front and not self.back
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()