class BitVectorSet:

    def __init__(self, size):
        self.array = []
        for n in range(size):
            self.array[n] = False

    def __contains__(self, el: int):
        if len(self.array) < (el - 1):
            return False
        return self.array[el] == True

    def insert(self, el: int):
        if el not in self:
            self.array[el] = True

    def remove(self, el: int):
        if el in self:
            self.array[el] = False
