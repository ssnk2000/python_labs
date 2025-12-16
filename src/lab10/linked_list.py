from typing import Any, Optional, Iterator


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError("negative index is not supported")

        if idx == 0:
            self.prepend(value)
            return

        current = self.head
        for n in range(idx - 1):
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def remove(self, value):
        if self.head is None:
            raise ValueError(f"")
        
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return
        
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current

                current.next = current.next.next
                self._size -= 1
                return
            current = current.next

        raise ValueError(f"")

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"
    

print("             Singly linked list test\n")
sll = SinglyLinkedList()
print(f"Заносим элементы в список: 50 -> 30 -> 40")
sll.append(50)
sll.append(30)
sll.append(40)
print(f"Список: {sll}")
print(f"Добавление элемента 20 в начало:")
sll.prepend(20)
print(f"Список: {sll}")
print(f"Добавление элемента 15 по индексу 1:")
sll.insert(1, 15)
print(f"Список: {sll}")
print(f"Добавление элемента 35 по индексу 3:")
sll.insert(3, 35)
print(f"Список: {sll}")
print(f"Вставка элемента 40 в конец:")
sll.insert(4, 40)
print(f"Список: {sll}")
print(f"Удаление элемента 30:")
sll.remove(30)
print(f"Список: {sll}")
print(f"Удаление элемента 20:")
sll.remove(20)
print(f"Список: {sll}")
print(f"Удаление элемента 40:")
sll.remove(40)
print(f"Список: {sll}")
print(f"Кол-во элементов в списке: {len(sll)}")
print(f"Проверка списка на пустоту: {len(sll) == 0}")