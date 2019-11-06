class CircularArray:
    def __init__(self):
        self.items = []

    def add(self, element):
        self.items.append(element)

    def remove(self, element):
        self.items.remove(element)

    def pop(self):
        self.items.pop()

    def get(self, number):
        len_items = len(self.items)
        element_number = number
        if number >= len_items:
            while True:
                element_number -= len_items
                if element_number < len_items:
                    return self.items[element_number]
        else:
            return self.items[number]

    def len(self):
        return len(self.items)

    def min(self):
        return min(self.items)