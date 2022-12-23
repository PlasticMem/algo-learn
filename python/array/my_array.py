#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: PlasticMem
@time: 2022/12/23 14:43:19
@function: 
"""

from typing import Any


class MyArray:
    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, position: int):
        return self._data[position]

    def __setitem__(self, index: int, value: Any):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, position: int):
        try:
            return self._data[position]
        except IndexError:
            return None

    def delete(self, position: int):
        try:
            self._data.pop(position)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: Any):
        if len(self) >= self._capacity:
            return False
        return self._data.insert(index, value)

    def print_all(self):
        for item in self:
            print(item)


def test_myarray():
    array = MyArray(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()


if __name__ == "__main__":
    test_myarray()
