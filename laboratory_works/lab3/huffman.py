from .binarytree import BTree


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
