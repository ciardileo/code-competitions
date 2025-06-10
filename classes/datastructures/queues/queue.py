"""
estrutura de dados queue/fila
"""

# method 1: using deque (most efficient O(1))

from collections import deque

queue = deque()

queue.append("first") # enqueue
queue.append("second")
queue.append("third")

print(queue.popleft()) # dequeue 

# method 2: using lists (less efficient O(n))

queue = []

queue.append("first") # enqueue
queue.append("second")
queue.append("third")

print(queue.pop(0)) # dequeue

# circular queue

class CircularQueue:
    def __init__(self, capacity):
        """
        front = index do primeiro elemento da fila
        rear = index do último elemento da fila
        """
        
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
    

    def enqueue(self, item):
        if (self.rear + 1) % self.capacity == self.front:
            print("A fila está cheia")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print(f"{item} foi adicionado à fila")

    def dequeue(self):
        if self.front == -1:
            print("A fila está vazia")
            return

        item = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        print(f"{item} foi removido da fila")

    def display(self):
        if self.front == -1:
            print("A fila está vazia")
            return

        print("Fila atual:")
        
        # se a fila é simples:
        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
                
        # se a fila já virou circular:
        else:
            for i in range(self.front, self.capacity):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")

        print()


# Exemplo de uso
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6)
cq.display()
cq.dequeue()
cq.enqueue(190)
cq.display()
cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6)
cq.display()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.display()
cq.dequeue()