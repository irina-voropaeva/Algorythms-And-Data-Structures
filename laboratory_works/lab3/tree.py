class BTree:
    def __init__(self, pair=None, left=None, right=None):
        self.pair = pair
        self.left = left
        self.right = right

    def __len__(self):
        return len(self.prefix_traverse())

    def __str__(self):
        return repr(self)

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


def frequency_table(string):
    d = {}
    for char in string:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d


def chars_by_frequency(table):
    kvpl = [(table[k], k) for k in table.keys()]
    kvpl.sort(key=lambda x: x[0], reverse=True)
    return kvpl


def huffman_tree(table):
    tree = BTree(pair=(0, '42'))
    for pair in chars_by_frequency(table):
        tree.add(pair)
    return tree


def char_code(char, tree):
    if char not in tree:
        return None
    code = ''
    current_tree = tree
    while char != current_tree.pair[1]:
        if current_tree.left and char in current_tree.left:
            current_tree = current_tree.left
            code += '0'
        else:
            current_tree = current_tree.right
            code += '1'
    return code


def huffman_encode(string):
    d = frequency_table(string)
    t = huffman_tree(d)
    char_codes = {char: char_code(char, t) for char in set(string)}
    encoded = [char_code(char, t) for char in string]
    encoded = ','.join(encoded)
    return {'table': d, 'tree': t, 'char codes': char_codes, 'encoded': encoded}


def huffman_decode(encoded, table):
    decoded = [key_by_value(fragment, table) for fragment in encoded.split(',')]
    return ''.join(decoded)


def key_by_value(value, dct):
    for key in dct.keys():
        if dct[key] == value:
            return key
    return None


b = BTree(left=4, right=5)
b.add('text')
