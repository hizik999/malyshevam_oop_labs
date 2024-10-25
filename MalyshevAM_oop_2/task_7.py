class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print(elements)

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next


linked_list = LinkedList()

linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)

print("Данные связанного списка:")
linked_list.display()

linked_list.insert(6)

print("Обновленные данные связанного списка:")
linked_list.display()

linked_list.delete(3)

print("Обновленные данные связанного списка после удаления:")
linked_list.display()