import ctypes
from typing import Iterable, Any


class DynamicArray:
    def __init__(self) -> None:
        self._n: int = 0
        self._capacity: int = 1
        self._array = self._make_array(self._capacity)

    def __len__(self) -> int:
        # Time complexity: O(1)
        return self._n

    def __getitem__(self, index: int) -> Any:
        # Time complexity: O(1)
        if not 0 <= index < self._n:
            raise IndexError("Invalid index")
        return self._array[index]

    def append(self, obj: Any) -> None:
        # Time complexity: O(1)*
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._n] = obj
        self._n += 1

    def insert(self, obj: Any, index: int) -> None:
        # Time complexity: O(n - index + 1)*
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        for i in range(self._n, index, -1):
            # shift rightmost first [1,2,3,4] -> [1,2,*,3,4]
            self._array[i] = self._array[i - 1]
        self._array[index] = obj
        self._n += 1

    def extend(self, array: Iterable) -> None:
        # Time complexity: O(k)* where k=len(array)
        if self._n + len(array) >= self._capacity:
            required_capacity = self._n + len(array)
            new_capacity = self._capacity
            while new_capacity < required_capacity:
                new_capacity = 2 * new_capacity
            self._resize(new_capacity)
        
        for obj in array:
            self._array[self._n] = obj
            self._n += 1

    def remove(self, value: Any) -> None:
        # Time complexity: O(n)*
        for i in range(self._n):
            if self._array[i] != value:
                continue

            for j in range(i, self._n - 1):
                self._array[j] = self._array[j + 1]

            self._n -= 1
            # TODO: Resize the array if enough elements were removed
            return

        raise ValueError("Value not found")

    def pop(self, index: int) -> Any:
        temp = self._array[index]
        for i in range(index, self._n - 1):
            self._array[i] = self._array[i + 1]
        self._n -= 1

        # TODO: Resize the array if enough elements were removed
        return temp

    def _resize(self, capacity: int) -> None:
        new_array = self._make_array(capacity)
        for i, obj in enumerate(self._array):
            new_array[i] = obj
        self._array = new_array
        self._capacity = capacity

    def _make_array(self, capacity: int) -> ctypes.py_object:
        return (capacity * ctypes.py_object)()
