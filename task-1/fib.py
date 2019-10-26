def fib_0000():
    mod_result = 1
    v = 1
    number_of_element = 1
    while mod_result != 0:
        w = mod_result
        number_of_element = number_of_element + 1
        mod_result = (mod_result + v) % 10000
        v = w
    print(number_of_element)
    return w


if __name__ == "__main__":
    fib_0000()
