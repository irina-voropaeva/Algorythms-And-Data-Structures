from .circarray import CircularArray


class Queue:
    def __init__(self):
        self.items = CircularArray()

    def is_empty(self):
        return self.items == []

    def add(self, item):
        self.items.add(item)
        return item

    def remove(self):
        if not self.size() == 0:
            return self.items.pop()
        else:
            return None

    # O(N)
    def delete_min(self):
        min_el = self.items.get(0)
        for i in range(5):
            if self.items.get(i) < min:
                min_el = self.items.get(i)
        self.items.remove(min_el)

    def size(self):
        return self.items.len()

    # O (log n)
    def bin_search(self, x):
        i = 0
        j = self.items.len() - 1
        m = int(j / 2)
        while self.items.get(m) != x and i < j:
            if x > self.items.get(m):
                i = m + 1
            else:
                j = m - 1
            m = int((i + j) / 2)
        if i > j:
            return None
        else:
            return m
