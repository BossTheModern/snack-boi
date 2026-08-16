'''
    queue.py

    custom queue class 
'''
from collections import deque
from typing import Any, Optional

class Queue:
    def __init__(self, max_size: Optional[int] = None) -> None:
        self._items: deque = deque(maxlen=max_size)

    def __len__(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()

    def is_full(self) -> bool:
        return self._items.maxlen is not None and len(self._items) == self._items.maxlen

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def enqueue(self, item: Any) -> None:
        if self.is_full():
            raise OverflowError("queue is full")
        self._items.append(item)

    def dequeue(self) -> None:
        if self.is_empty():
            raise IndexError("Cannot dequeue an empty queue")

        return self._items.popleft()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Cannot peek on an empty queue")
        return self._items[0]
    

