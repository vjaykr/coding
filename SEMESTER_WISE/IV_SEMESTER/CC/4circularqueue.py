class CircularQueue:
    def __init__(self, k):
        self.capacity = k
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full. Cannot enqueue.")
            return

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
            return -1

        removedValue = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return removedValue

    def getFront(self):
        if self.isEmpty():
            print("Queue is empty.")
            return -1

        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            print("Queue is empty.")
            return -1

        return self.queue[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


queue = CircularQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print("Front element:", queue.getFront())
print("Rear element:", queue.getRear())
print("Dequeuing:", queue.dequeue())
print("Dequeuing:", queue.dequeue())
print("Front element:", queue.getFront())
print("Rear element:", queue.getRear())

queue.enqueue(6)
queue.enqueue(7)

print("Front element:", queue.getFront())
print("Rear element:", queue.getRear())
