class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.size() == 0:
            return self.items.pop()
        else:
            return None

    def tail(self):
        if not self.size() == 0:
            return self.items[len(self.items)-1]
        else:
            return None

    def len(self):
        return self.items.__len__()

    def size(self):
        return len(self.items)

    # O (log n)
    def find(self, x):
        i = 0
        j = self.items.__len__() - 1
        m = int(j / 2)
        while self.items[m] != x and i < j:
            if x > self.items[m]:
                i = m + 1
            else:
                j = m - 1
            m = int((i + j) / 2)
        if i > j:
            return None
        else:
            return m

    def get(self, index):
        return self.items[index]

    def remove(self, element):
        self.items.remove(element)
