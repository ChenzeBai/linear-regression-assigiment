import random
import time
import matplotlib.pyplot as plt


def selection_sort(lst):
    lst = lst.copy()

    for i in range(len(lst)):
        min = lst[i]
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < min:
                min = lst[j]
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def bubble_sort(lst):
    lst = lst.copy()

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


def insertion_sort(lst):
    lst = lst.copy()
    
    for i in range(len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1

        lst[j+1] = key

    return lst


def generate_lst(n):
    lst = [random.randint(-10 * n, 10 * n) for i in range(n)]

    return lst


def n_values_generate():
    n_values = [n for n in range(5000, 20000, 1000)]

    return n_values


def experiment_time(show= True):
    n_values = n_values_generate()

    for n in n_values:
        lst = generate_lst(n)

        if show:
            print(f'=====Experiment {(n - 4000) // 1000}, n value= {n}=====')

        time_start_selection = time.time()
        selection_sort(lst)
        time_end_selection = time.time()
        time_used_selection = time_end_selection - time_start_selection


        time_start_bubble = time.time()
        bubble_sort(lst)
        time_end_bubble = time.time()
        time_used_bubble = time_end_bubble - time_start_bubble

        time_start_insertion = time.time()
        insertion_sort(lst)
        time_end_insertion = time.time()
        time_used_insertion = time_end_insertion - time_start_insertion




        if show:
            print(f'The selection sort uesd {time_used_selection} second(s) to sort {n} elements')
            print(f'The bubble sort uesd {time_used_bubble} second(s) to sort {n} elements')
            print(f'The inserction sort uesd {time_used_insertion} second(s) to sort {n} elements')




def main():
    experiment_time(show= True)


main()
