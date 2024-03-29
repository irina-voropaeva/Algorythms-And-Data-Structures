if __name__ == "__main__":
    N, M = map(int, input().split())

    Edges = []

    for i in range(M):
        start, end, weight = map(int, input().split())
        Edges.append([weight, start, end])

    Edges.sort()

    Comp = [i for i in range(N)]
    Ans = 0

    for weight, start, end in Edges:
        if Comp[start] != Comp[end]:
            Ans += weight
            a = Comp[start]
            b = Comp[end]
            for i in range(N):
                if Comp[i] == b:
                    Comp[i] = a