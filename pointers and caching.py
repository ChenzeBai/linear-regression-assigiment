import random
import time
import matplotlib.pyplot as plt
import math



def threesum_pointers(lst, sum=0):
    lst = sorted(lst)
    result = set()

    for i in range(len(lst) - 2):
        left = i + 1
        right = len(lst) - 1

        while left < right:
            total = lst[i] + lst[left] + lst[right]

            if total == sum:
                result.add((lst[i], lst[left], lst[right]))
                left += 1
                right -= 1

            elif total < sum:
                left += 1

            else:
                right -= 1

    return result



def threesum_caching(lst, sum = 0):
    unique_pairs = set()

    for i in range(len(lst)):
        cache = set()
        for j in range(i+1, len(lst)):
            v2 = sum - lst[i] - lst[j]
            if v2 in cache:
                result = sorted((lst[i], v2, lst[j]))
                unique_pairs.add(tuple(result))
            cache.add(lst[j])

    return unique_pairs



def generate_list(n):
    lst = [random.randint(-10 * n, 10 * n) for i in range(n)]

    return lst


def testing_function(n):
    for i in range(3):
        lst = generate_list(n)
        print(f'{i+1}. {lst}')
        result_pointers = threesum_pointers(lst, sum=0)
        result_caching = threesum_caching(lst, sum = 0)
        print(f'result for pointers: {result_pointers}')
        print(f'result for caching: {result_caching}')
        print(f'Checking whether they are equal: {result_caching == result_pointers}')




def experiment_function(show=True):
    n_values = [n for n in range(2500, 9501, 500)]

    time_pointers_1 = []
    time_pointers_2 = []
    time_pointers_3 = []

    time_caching_1 = []
    time_caching_2 = []
    time_caching_3 = []


    for n in n_values:
        for i in range(3):
            lst = generate_list(n)

            if show:
                print(f'=========No.{(n - 2000) // 500} ,experiment time {i + 1} experiment data==========')
            time_start_pointers = time.time()
            threesum_pointers(lst, sum=0)
            time_end_pointers = time.time()
            time_used_pointers = time_end_pointers - time_start_pointers
            if show:
                print(f'The pointers used {time_used_pointers} to sorting {n} values')


            time_start_caching = time.time()
            threesum_caching(lst, sum=0)
            time_end_caching = time.time()
            time_used_caching = time_end_caching - time_start_caching
            if show:
                print(f'The caching used {time_used_caching} to sorting {n} values')

            if i == 0:
                time_pointers_1.append(time_used_pointers)
                time_caching_1.append(time_used_caching)

            elif i == 1:
                time_pointers_2.append(time_used_pointers)
                time_caching_2.append(time_used_caching)

            elif i ==2:
                time_pointers_3.append(time_used_pointers)
                time_caching_3.append(time_used_caching)


    return n_values, time_caching_1, time_caching_2, time_caching_3, time_pointers_1, time_pointers_2, time_pointers_3



def experiment_graph_both(n_values, time_caching_1, time_caching_2, time_caching_3, time_pointers_1, time_pointers_2, time_pointers_3):

    plt.scatter(n_values, time_caching_1, label='Caching 1',marker='x')
    plt.scatter(n_values, time_caching_2, label='Caching 2',marker='+')
    plt.scatter(n_values, time_caching_3, label='Caching 3',marker='o')

    plt.scatter(n_values, time_pointers_1, label='Pointers 1',marker='x')
    plt.scatter(n_values, time_pointers_2, label='Pointers 2',marker='+')
    plt.scatter(n_values, time_pointers_3, label='Pointers 3',marker='o')

    plt.xlabel('N size')
    plt.ylabel('Working time')
    plt.title('Caching and pointers Algorithm for 3-sum comparation')

    plt.legend()
    plt.show()


def lin_reg(x, y):
    n = len(x)

    sum_x = 0
    sum_y = 0
    sum_x_squared = 0
    sum_xy = 0
    
    for i in range(n):
        sum_x += x[i]
        sum_y += y[i]
        sum_x_squared += x[i] ** 2
        sum_xy += x[i] * y[i]
    
    k = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    
    m = (sum_y - k * sum_x) / n
    
    return m, k


def average_time_caused(n_values, time_caching_1, time_caching_2, time_caching_3, time_pointers_1, time_pointers_2, time_pointers_3):
    time_average_caching = []
    time_average_pointers = []
    
    
    for i in range(len(n_values)):
        average_caching = (time_caching_1[i] + time_caching_2[i] + time_caching_3[i]) / 3
        time_average_caching.append(average_caching)

        average_pointers = (time_pointers_1[i] + time_pointers_2[i] + time_pointers_3[i]) / 3
        time_average_pointers.append(average_pointers)

    return time_average_caching, time_average_pointers



def log_log_calculate(n_values, time_caching_1, time_caching_2, time_caching_3, time_pointers_1, time_pointers_2, time_pointers_3):
    time_average_caching, time_average_pointers = average_time_caused(n_values, time_caching_1, time_caching_2, time_caching_3, time_pointers_1, time_pointers_2, time_pointers_3)

    log_n_caching = []
    log_time_caching = []
    log_n_pointers = []
    log_time_pointers = []

    for i in range(len(n_values)):
        log_n_caching.append(math.log(n_values[i]))
        log_n_pointers.append(math.log(n_values[i]))

        log_time_caching.append(math.log(time_average_caching[i]))
        log_time_pointers.append(math.log(time_average_pointers[i]))

    m_caching, k_caching = lin_reg(log_n_caching, log_time_caching)
    m_pointers, k_pointers = lin_reg(log_n_pointers, log_time_pointers)

    return m_caching, k_caching, m_pointers, k_pointers, log_n_caching, log_time_caching, log_n_pointers, log_time_pointers


def straight_line_fit_graph(m_caching, k_caching, m_pointers, k_pointers, log_n_caching, log_time_caching, log_n_pointers, log_time_pointers):
    fit_caching = []
    fit_pointers = []

    for i in log_n_caching:
        fit_caching.append(m_caching + k_caching * i)

    for j in log_n_pointers:
        fit_pointers.append(m_pointers + k_pointers * j)

    plt.plot(log_n_caching, fit_caching, label='Caching fit line')
    plt.scatter(log_n_caching, log_time_caching, label='Caching data', marker='o')

    plt.plot(log_n_pointers, fit_pointers, label='Pointer fit line')
    plt.scatter(log_n_pointers, log_time_pointers, label='Pointers data',marker='x')

    plt.xlabel('log(n)')
    plt.ylabel('log(time)')
    plt.title('log-log regression')

    plt.legend()
    plt.show()


def main():
    print('========Testing==========')
    testing_function(15)


    print('=====Getting data and showing graphs, please wait...======')
    n_values, time_caching_1, time_caching_2, time_caching_3, time_pointers_1, time_pointers_2, time_pointers_3 = experiment_function(show=False)
    experiment_graph_both(n_values, time_caching_1, time_caching_2, time_caching_3, time_pointers_1, time_pointers_2, time_pointers_3)

    print('=====Calculating result...=====')
    result = log_log_calculate(n_values, time_caching_1, time_caching_2, time_caching_3, time_pointers_1, time_pointers_2, time_pointers_3)
    m_caching = result[0]
    k_caching = result[1]
    m_pointers = result[2]
    k_pointers = result[3]
    log_n_caching = result[4]
    log_time_caching = result[5]
    log_n_pointers = result[6]
    log_time_pointers = result[7]
    print(f'The resulting coefficient of caching is: {k_caching}\n')
    print(f'The resulting coefficient of pointers is: {k_pointers}\n')

    print('=====Showing out graphs=====')
    straight_line_fit_graph(m_caching, k_caching, m_pointers, k_pointers, log_n_caching, log_time_caching, log_n_pointers, log_time_pointers)

main()
