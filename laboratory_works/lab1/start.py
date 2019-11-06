from task import sort_bubble, insertion_sort, quick_sort, generate_rand_list


if __name__ == "__main__":
    print("Bubble sort 1000 elements: ", sort_bubble(generate_rand_list(1000)))
    print("Bubble sort 2000 elements: ", sort_bubble(generate_rand_list(2000)))
    print("Bubble sort 3000 elements: ", sort_bubble(generate_rand_list(3000)))
    print("Bubble sort 4000 elements: ", sort_bubble(generate_rand_list(4000)))
    print("Bubble sort 5000 elements: ", sort_bubble(generate_rand_list(5000)))
    print("Bubble sort 6000 elements: ", sort_bubble(generate_rand_list(6000)))

    print("Insertion sort 1000 elements: ", insertion_sort(generate_rand_list(1000)))
    print("Insertion sort 2000 elements: ", insertion_sort(generate_rand_list(2000)))
    print("Insertion sort 3000 elements: ", insertion_sort(generate_rand_list(3000)))
    print("Insertion sort 4000 elements: ", insertion_sort(generate_rand_list(4000)))
    print("Insertion sort 5000 elements: ", insertion_sort(generate_rand_list(5000)))
    print("Insertion sort 6000 elements: ", insertion_sort(generate_rand_list(6000)))

    print("Quick sort 1000 elements: ", quick_sort(generate_rand_list(1000)))
    print("Quick sort 2000 elements: ", quick_sort(generate_rand_list(2000)))
    print("Quick sort 3000 elements: ", quick_sort(generate_rand_list(3000)))
    print("Quick sort 4000 elements: ", quick_sort(generate_rand_list(4000)))
    print("Quick sort 5000 elements: ", quick_sort(generate_rand_list(5000)))
    print("Quick sort 6000 elements: ", quick_sort(generate_rand_list(6000)))