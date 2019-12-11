class ListSet:

    def __init__(self):
        self.l = []

    def __len__(self):
        return len(self.l)

    def __str__(self):
        return str(self.l)

    def __repr__(self):
        return repr(self.l)

    def __contains__(self, el):
        return el in self.l

    def get(self, key):
        return self.l[key]

    def set(self, key, value):
        if value in self.l:
            raise ValueError('Set already has value: ' + str(value))
        self.l[key] = value

    def add(self, value):
        if value in self.l:
            raise ValueError('Set already has value: ' + str(value))
        self.l.append(value)

    def remove(self, value):
        self.l.remove(value)