#!/usr/bin/env python
# -*- coding:utf-8 -*-

class LinkedListNode:
    def __init__(self, data, next_node=None) -> None:
        self.__data = data
        self.__next_node = next_node
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
    
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        self.__next_node = next_node


class SinglyLinkedList:
    def __init__(self) -> None:
        self.__head = None
    
    def find_by_value(self, value):
        node = self.__head
        while (node is not None) and (node.data != value):
            node = node.next_node
        return node
    
    def find_by_index(self, index):
        node = self.__head
        pos = 0
        while (pos != index) and (node is not None):
            node = node.next_node
            pos += 1
        return node
