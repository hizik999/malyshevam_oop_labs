class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)


bst = BinarySearchTree()

import random
numbers = [random.randint(1, 20) for _ in range(10)]
for num in numbers:
    bst.insert(num)

print('Numbers')
print(numbers)

search_values = [random.randint(1, 20) for _ in range(5)]
print("search_values")
print(search_values)
for value in search_values:
    result = bst.search(value)
    if result is not None:
        print(f"Значение {value} найдено в дереве")
    else:
        print(f"Значение {value} не найдено в дереве")