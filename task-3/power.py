# TODO: recheck
def quick_pow(a, n, d):
    A = (quick_pow(a, n // 2, d)**2) % d
    if n % 2 == 0:
        return A
    else:
        return (A*a) % d


if __name__ == "__main__":
    print(quick_pow(2, 3, 2))
