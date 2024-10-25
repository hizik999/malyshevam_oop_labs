class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Элементы стека:")
        for item in self.items:
            print(item)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.display()

print("Выталкиваем элементы из стека:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

stack.display()

print("Пуст ли стек?", stack.is_empty())

print(stack.pop())
print(stack.pop())

print("Пуст ли стек?", stack.is_empty())

try:
    stack.pop()
except IndexError as e:
    print(e)