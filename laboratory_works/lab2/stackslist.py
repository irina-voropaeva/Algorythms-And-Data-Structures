from .stack import Stack


class List:
    def __init__(self):
        self.leftItems = Stack()
        self.rightItems = Stack()

    def is_empty(self):
        return self.rightItems.is_empty() and self.leftItems.is_empty()

    def push(self, item):
        self.leftItems.push(item)

    def insert(self):
        if not self.rightItems.is_empty():
            return self.rightItems.pop()
        elif not self.leftItems.is_empty():
            return self.leftItems.pop()
        else:
            return None

    def tail(self):
        return self.leftItems.tail()

    def move_left(self):
        if not self.leftItems.is_empty():
            self.rightItems.push(self.leftItems.pop())
            return True
        return False

    def move_right(self):
        if not self.rightItems.is_empty():
            self.leftItems.push(self.rightItems.pop())
            return True
        return False

    def size(self):
        return self.leftItems.size() + self.rightItems.size()

    # O (N * log N)
    def find_min(self):
        min_el = self.leftItems.get(0)
        for i in range(5):
            if self.leftItems.get(i) < min_el:
                min_el = self.leftItems.get(i)
        for i in range(5):
            if self.rightItems.get(i) < min_el:
                min_el = self.rightItems.get(i)
        return min_el

    def len(self):
        return self.leftItems.len() + self.rightItems.len()

