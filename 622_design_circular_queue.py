class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.size = 0
        self.f = -1
        self.b = 0
        self.queue = [None] * k
        # queue[f] = front element
        # queue[b] = back element

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.f = (self.f + 1) % self.capacity
        self.queue[self.f] = value
        self.size += 1
        # print(self.f, self.queue)
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.queue[self.b] = None

        self.b = (self.b + 1) % self.capacity
        self.size -= 1
        # print(self.b, self.queue)
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """

        # print(self.b, self.queue)
        return -1 if self.isEmpty() else self.queue[self.b]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        # print(self.f, self.queue)
        return -1 if self.isEmpty() else self.queue[self.f]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()