class LoadedTree:
    def __init__(self, col=None):
        self.children = dict()
        if col:
            for el in col:
                self.add(el)

    def add(self, el):
        if el[0] not in self.children:
            self.children[el] = dict()
        else:
            n = 1
            key = el[0]
            child = self.children[key]

            while n < len(el) - 1:
                key = el[n]
                n += 1
                child = child[key]

            child[el[n + 1]] = dict()

    def get(self, el):

        if el in self.children:
            return self.children[el]

        else:
            child = self.children
            for char in el:
                if char in child:

                    child = child[char]
                else:
                    return None
            return child