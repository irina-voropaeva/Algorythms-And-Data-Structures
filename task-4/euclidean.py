# TODO: looks that it is not work; recheck
A = 3
B = 5


def ExtGCD(A, B):
    x = A
    y = B
    u1 = 1
    v1 = 0
    u2 = 0
    v2 = 1
    d = -1
    v = -1
    u = -1
    while x != y:
        if x > y:
            x = x - y
            u1 = u1 - u2
            v1 = v1 - v2
        else:
            y = y - x
            u2 = u2 - u1
            v2 = v2 - v1
        d = x
        u = u1
        v = v1
    return d, u, v


if __name__ == "main":
    d, u, v = ExtGCD(A, B)
    print(ExtGCD(A, B))

    M = min(A, B)
    N = M
    while True:
        i = 0
        Yes = True
        while True:
            if i == M or not Yes:
                break
            Yes = (Yes and (N + i == u*A, v*B))
            i = i + 1
        if not Yes:
            N = N + i
    print(M, N)
