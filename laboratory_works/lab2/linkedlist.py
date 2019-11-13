class Item:

    def __init__(self, next__item=None, prev__item=None, elem=None):
        self.next__item = next__item
        self.prev__item = prev__item
        self.elem = elem


class DoubleLinkedList:

    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    def push(self, elem):
        if self.tail is None:  # length == 0
            item = Item(None, None, elem)
            self.head = item
            self.tail = self.head
            self.length = 1
        else:
            item = Item(None, self.tail, elem)
            self.tail.next__item = item
            self.tail = item
            self.length += 1

    def pop(self):
        if self.tail is None:
            return
        else:
            self.tail = self.tail.prev__item
            if self.tail is not None:
                self.tail.next__item = None
            self.length -= 1

    def add_to_start(self, elem):
        if self.head is None:
            item = Item(None, None, elem)
            self.head = item
            self.tail = self.head
            self.length = 1
        else:
            item = Item(self.head, None, elem)
            self.head.prev__item = item
            self.head = self.head.prev__item
            self.length += 1

    def shift(self):
        if self.head is None:  # length == 0
            return
        else:
            self.head = self.head.next__item
            if self.head is not None:
                self.head.prev__item = None
            self.length -= 1

    def len(self):
        return self.length

    def delete(self, elem):
        if self.head is None:
            pass  # return
        elif self.head.elem == elem:
            self.shift()
        else:
            cur = self.head.next__item
            while cur is not None:
                if (cur.elem == elem) and (cur.next__item is not None):
                    temporary_item = cur.prev__item.next__item
                    cur.prev__item.next__item = cur.next__item.prev__item
                    cur.next__item.prev__item = temporary_item
                    self.length -= 1
                    break  # return
                elif (cur.elem == elem) and (cur.next__item is None):
                    cur.prev__item.next__item = None
                    self.tail = cur.prev__item
                    self.length -= 1
                    break
                else:
                    cur = cur.next__item

    # O (N)
    def find(self, element):
        current = self.head
        while current != element:
            current = current.next__item
        return current

    # O (N)
    def find_min(self):
        minimal = self.head
        while minimal.next__item is not None:
            if minimal > minimal.next__item:
                minimal = minimal.next__item
            else:
                continue

        return minimal

    def first(self):
        return self.head

    def last(self):
        return self.tail
