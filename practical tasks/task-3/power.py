def quick_pow(num, deg):
    if 0 == num:
        return 0
    if 0 == deg:
        return 1
    if deg % 2 == 0:
        return (quick_pow(num, deg / 2) ** 2) % 100 
    return (num * quick_pow(num, deg - 1)) % 100


if __name__ == "__main__":
    print(quick_pow(2, 3))
