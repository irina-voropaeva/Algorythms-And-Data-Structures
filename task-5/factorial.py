# Факториал


# задача 3.1
def numbers_of_end_zeros(n):  # n это то что будет n!
    last_dig = 1
    i = 2
    number_of_5 = 0
    while i < n:
        j = i
        number_of_2 = 0
        i += 1
        while j % 2 == 0:
            j = j // 2
            number_of_2 += 1
        last_dig = (last_dig * j) % 10
        while j % 5 == 0:
            j = j // 5
            number_of_5 = number_of_5 + 1
        last_dig = (last_dig * j) % 10
        number_of_2 -= number_of_5
        g = number_of_2 - number_of_5
        while g > 1:
            last_dig = (last_dig * 2) % 10
            g -= 1
    return number_of_5, last_dig


if __name__ == "__main__":
    print(numbers_of_end_zeros(10))



