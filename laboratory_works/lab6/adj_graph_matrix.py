class AdjGraph:
    matrix = []

    def create_matrix(self, size: int):
        for i in range(size):
            self.matrix.append([])
            for j in range(size):
                self.matrix[i].append(0)

    def add_relation(self, node1: int, node2: int):  # связь node1 -> node2
        self.matrix[node1][node2] = 1

    def get_relation(self, node1, node2):
        return self.matrix[node1][node2]


if __name__ == "__main__":
    graph = AdjGraph()
    graph.create_matrix(4)
    graph.add_relation(0, 1)
    graph.add_relation(1, 0)
    print(graph.matrix)

