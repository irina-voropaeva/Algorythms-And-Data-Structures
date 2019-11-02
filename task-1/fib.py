# Число Фибоначчи с 0000
def fib_0000():
    mod_result = 1
    mod_result_next = 1
    number_of_element = 1
    while mod_result != 0:
        result = mod_result
        number_of_element = number_of_element + 1
        mod_result = (mod_result + mod_result_next) % 10000
        mod_result_next = result
    print(number_of_element)
    return result


# Запуск
if __name__ == "__main__":
    fib_0000()
