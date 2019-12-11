class BTree:
    def __init__(self, pair=None, left=None, right=None):
        self.pair = pair
        self.left = left
        self.right = right

    def __repr__(self, indent=0):
        s = repr(self.pair)
        ls = (' ' * (indent + len(s))) + 'None\n' if self.left is None else self.left.__repr__(indent + len(s))
        rs = (' ' * (indent + len(s))) + 'None\n' if self.right is None else self.right.__repr__(indent + len(s))
        return (' ' * indent) + s + '\n' + ls + rs

    def find(self, key):
        if self.pair[0] == key:
            return self.pair[1]
        else:
            lval = self.left.find(key)
            if lval is not None:
                return lval
            rval = self.right.find(key)
            if rval is not None:
                return rval
            return None

    def find_pair(self, key):
        if self.pair[0] == key:
            return self.pair
        else:
            lval = self.left.find_pair(key) if type(self.left) == BTree else None
            if lval is not None:
                return lval
            rval = self.right.find_pair(key) if type(self.right) == BTree else None
            if rval is not None:
                return rval
            return None

    def add(self, pair):
        if pair[1] in self:
            return
        if self.pair is None:
            self.pair = pair
        elif pair[1] <= self.pair[1]:
            if self.left is None:
                self.left = BTree(pair)
            else:
                self.left.add(pair)
        else:
            if self.right is None:
                self.right = BTree(pair)
            else:
                self.right.add(pair)

    def infix_traverse(self):
        kvp = []
        if type(self.left) == BTree:
            kvp.extend(self.left.infix_traverse())
        if self.pair is not None:
            kvp.append(self.pair)
        if type(self.right) == BTree:
            kvp.extend(self.right.infix_traverse())
        return kvp

    def prefix_traverse(self):
        kvp = []
        if self.pair is not None:
            kvp.append(self.pair)
        if type(self.left) == BTree:
            kvp.extend(self.left.prefix_traverse())
        if type(self.right) == BTree:
            kvp.extend(self.right.prefix_traverse())
        return kvp

    def postfix_traverse(self):
        kvp = []
        if type(self.left) == BTree:
            kvp.extend(self.left.postfix_traverse())
        if type(self.right) == BTree:
            kvp.extend(self.right.postfix_traverse())
        if self.pair is not None:
            kvp.append(self.pair)
        return kvp