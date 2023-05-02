from __future__ import annotations
from typing import Any
from random import shuffle

class Node:
    def __init__(self, val : Any, parent : Node = None, childs : dict[Any : "Node"] = None) -> None:
        self.__val = val
        if childs == None:
            childs = {}
        self.childs = childs
        self.parent = parent

    def get_val(self):
        return self.__val

    def set_val(self, new_val):
        self.__val = new_val
    
    def is_root(self):
        return self.parent == []
    
    def is_leaf(self):
        return self.childs == {}

class Binary_sort_node(Node):
    def __init__(self, val: Any, parent: Binary_sort_node | None = None, childs: dict[str : 'Binary_sort_node'] | None = None) -> None:
        super().__init__(val, parent, childs)

    def add_value(self, value : Any):
        if value >= self.get_val():
            if self.childs.get('r', 0) == 0:
                self.childs['r'] = Binary_sort_node(value, self)
            else:
                self.childs['r'].add_value(value)
        else:
            if self.childs.get('l', 0) == 0:
                self.childs['l'] = Binary_sort_node(value, self)
            else:
                self.childs['l'].add_value(value)

    def get_sorted(self) -> list:
        if self.is_leaf():
            return [self.get_val()]
        elif self.childs.get('l', 0) == 0:
            return [self.get_val()] + self.childs['r'].get_sorted()
        elif self.childs.get('r', 0) == 0:
            return self.childs['l'].get_sorted() + [self.get_val()]
        return self.childs['l'].get_sorted() + [self.get_val()] + self.childs['r'].get_sorted()
    
if __name__ == '__main__':
    x = [i for i in range(1000)]
    shuffle(x)
    tree = Binary_sort_node(x.pop(0))
    for i in x:
        tree.add_value(i)
    print(tree.get_sorted())
