class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Элементы очереди:")
        for item in self.items:
            print(item)


queue = Queue()

print("Добавляем элементы в очередь:")
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.display()

print("Удаляем элементы из очереди:")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

queue.display()

print("Пуста ли очередь?", queue.is_empty())

print(queue.dequeue())
print(queue.dequeue())

print("Пуста ли очередь?", queue.is_empty())

try:
    queue.dequeue()
except IndexError as e:
    print(e)