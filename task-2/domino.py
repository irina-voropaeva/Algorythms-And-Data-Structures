class Domino:

    domino_source = [[]]
    powers = []
    visited_vertexes = []
    vertexes_number = 6
    knuckles_number = 0

    # Инициализация
    def init(self):
        # [4, 4]
        self.domino_source = [[0, 3], [0, 4], [1, 2], [1, 5], [2, 5], [3, 4], [3, 6], [4, 6], [5, 6]]
        print(self.domino_source)
        self.knuckles_number = len(self.domino_source)
        for i in range(self.vertexes_number + 1):
            self.powers.append(0)

        for i in range(self.vertexes_number):
            self.visited_vertexes.append(False)

    # Проверка графа на связность
    def is_connected_graph(self):
        self.visited_vertexes[0] = True

        for i in range(self.vertexes_number):
            for j in self.visited_vertexes:
                if any([j, i] or [i, j] in d for d in self.domino_source):
                    self.visited_vertexes[i] = True
                    continue

        number_of_true = 0
        for i in self.visited_vertexes:
            if i is True:
                number_of_true += 1
        return number_of_true == self.vertexes_number

    # Проверка существования эйлерова пути в графе
    def is_euler_path_exists(self):

        for i in range(len(self.domino_source)):

            self.powers[self.domino_source[i][0]] += 1
            self.powers[self.domino_source[i][1]] += 1
        odd_deg = 0
        print(self.powers)
        for j in range(self.vertexes_number):
            if self.powers[j] % 2 == 1:
                odd_deg += 1
        return odd_deg == 2


# Запуск
if __name__ == "__main__":
    domino = Domino()
    domino.init()
    is_conn = domino.is_connected_graph()
    is_eu_path = domino.is_euler_path_exists()

    print ("Is chain possible: ", is_conn and is_eu_path)
