class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return "Невозможно извлечь данные из пустого стека"
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        if self.is_empty():
            return "Пустой стек"
        return self.stack[-1]


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("Размер стека:", stack.size())
print("Вершина стека:", stack.peek())

print("Выталкиваем элемент:", stack.pop())
print("Выталкиваем элемент:", stack.pop())

print("Размер стека:", stack.size())
print("Вершина стека:", stack.peek())

while not stack.is_empty():
    print("Выталкиваем элемент:", stack.pop())

print("Размер стека:", stack.size())
print("Вершина стека:", stack.peek())