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