import math


class MyTree:
    def __init__(self, children, pair=None):
        self.pair = pair
        self.children = []
        if children is not None:
            for child in children:
                self.children.append(MyTree(child))

    def find(self, key):
        if self.pair[0] == key:
            return self.pair[1]
        else:
            for child in self.children:
                val = child.find(key)
                if val is not None:
                    return val
            return None

    def add(self, node_to_add):
        if node_to_add[1] in self:
            return
        if self.pair is None:
            self.pair = node_to_add
        self.children.append(MyTree(node_to_add))

    # слева направоо
    def infix_traverse(self):
        kvp = []
        for n in range(math.ceil(len(self.children) / 2)):
            kvp.append(self.children[n].infix_traverse())
        if self.pair is not None:
            kvp.append(self.pair)
        for n in range(math.ceil(len(self.children) / 2), len(self.children)):
            kvp.append(self.children[n].infix_traverse())
        return kvp

    # сверху вниз
    def prefix_traverse(self):
        kvp = []
        if self.pair is not None:
            kvp.append(self.pair)
        for child in self.children:
            kvp.append(child.prefix_traverse())
        return kvp

    # снизу вверх
    def postfix_traverse(self):
        kvp = []
        for child in self.children:
            kvp.append(child.postfix_traverse())
        if self.pair is not None:
            kvp.append(self.pair)
        return kvp
