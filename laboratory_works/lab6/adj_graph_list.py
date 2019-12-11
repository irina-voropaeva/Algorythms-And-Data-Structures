class AdfGraphList:
    gr_list = []
    n = 0
    visited = []

    def create_list(self, size: int):
        n = size + 1
        self.visited = [False] * n  # массив "посещена ли вершина?"
        for i in range(size):
            self.gr_list.append([])

    def add_relation(self, node1: int, node2: int):  # связь node1 -> node2
        if self.gr_list.__len__() >= node1 and self.gr_list[node1].__contains__(node2):
            return
        self.gr_list[node1].append(node2)

    def is_relation_exists(self, node1, node2):
        return self.gr_list[node1].__contains__(node2)

    # поиск в глубину
    def dfs(self, v):
        self.visited[v] = True
        for w in self.gr_list[v]:
            if not self.visited[w]:  # посещён ли текущий сосед?
                self.dfs(w)


if __name__ == "__main__":
    graph = AdfGraphList()
    graph.create_list(4)
    graph.add_relation(0, 1)
    graph.add_relation(1, 0)
    graph.add_relation(0, 1)
    graph.add_relation(1, 2)
    graph.add_relation(2, 3)
    print(graph.gr_list)
    print(graph.is_relation_exists(0, 1))
    print(graph.is_relation_exists(2, 3))
    graph.dfs(0)
    print(graph.visited.count(True))
