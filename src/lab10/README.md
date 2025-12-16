### Задание 1
``` python
from collections import deque

class Stack:
    def __init__(self, data: list = []):
        self._data = data

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


print("              Stack test\n")
s = Stack()
print(f"Заносим элементы в стек: 5 -> 3 -> 4")
s.push(5)
s.push(3)
s.push(4)
print(f"Стек: {s._data}")
print(f"Удаление элемента из вершины стека: {s.pop()}")
print(f"Стек: {s._data}")
print(f"Просмотр элемента из вершины стека: {s.peek()}")
print(f"Кол-во элементов в стеке: {s.__len__()}")
print(f"Проверка стека на пустоту: {s.is_empty()}")
print(f"Удаление элемента из вершины стека: {s.pop()}")
print(f"Удаление элемента из вершины стека: {s.pop()}")
print(f"Кол-во элементов в стеке: {s.__len__()}")
print(f"Проверка стека на пустоту: {s.is_empty()}")


class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self._data == []:
            raise IndexError("Queue is empty.")
        else:
            return self._data.pop(0)

    def peek(self):
        if not self._data:
            return None
        else:
            return self._data[0]

    def is_empty(self) -> bool:
        if self._data == []:
            return True
        else:
            return False
        
    def __len__(self):
        return len(self._data)
    

print("\n              Queue test\n")
q = Queue()
print(f"Заносим элементы в очередь: 5 -> 3 -> 4")
q.enqueue(5)
q.enqueue(3)
q.enqueue(4)
print(f"Очередь: {q._data}")
print(f"Удаление элемента из начала очереди: {q.dequeue()}")
print(f"Очередь: {q._data}")
print(f"Просмотр элемента из начала очереди: {q.peek()}")
print(f"Кол-во элементов в очереди: {q.__len__()}")
print(f"Проверка очереди на пустоту: {q.is_empty()}")
print(f"Удаление элемента из начала очереди: {q.dequeue()}")
print(f"Удаление элемента из начала очереди: {q.dequeue()}")
print(f"Кол-во элементов в очереди: {q.__len__()}")
print(f"Проверка очереди на пустоту: {q.is_empty()}")
```
<img width="314" height="384" alt="Снимок экрана 2025-12-17 в 01 08 58" src="https://github.com/user-attachments/assets/0135f930-00d0-4e27-aee1-f3d5bf4910f7" />


### Задание 2
``` python
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
```
<img width="406" height="294" alt="Снимок экрана 2025-12-17 в 01 12 34" src="https://github.com/user-attachments/assets/19b33f58-2bec-47b5-b5da-8478c042fcf7" />
