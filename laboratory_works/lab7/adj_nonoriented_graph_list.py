class AdjNonOrientedGraph:
    matrix = []

    def create_matrix(self, size: int):
        for i in range(size):
            self.matrix.append([])
            for j in range(size):
                self.matrix[i].append(0)

    def add_relation(self, node1: int, node2: int):
        self.matrix[node1][node2] = 1
        self.matrix[node2][node1] = 1

    def get_relation(self, node1, node2):
        return self.matrix[node1][node2]


if __name__ == "__main__":
    graph = AdjNonOrientedGraph()
    graph.create_matrix(4)
    graph.add_relation(0, 1)
    graph.add_relation(1, 2)
    print(graph.matrix)

