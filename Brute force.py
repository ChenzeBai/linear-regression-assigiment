import random
import time
import matplotlib.pyplot as plt
import math


def generate_lst(n):
    lst = [random.randint(-10 * n,10 * n) for i in range(n)]
    return lst


def sum_three(lst, sum = 0):
    result = set()

    for i in range(len(lst) - 2):
        for j in range(i+1, len(lst) - 1):         
            for n in range(j+1, len(lst)):
                v1 = lst[i]
                v2 = lst[j]
                v3 = lst[n]
                if v1 + v2 + v3 == sum:
                    if v1 > v2:
                        v1, v2 = v2, v1
                    if v2 > v3:
                        v2, v3 = v3, v2
                    if v1 > v2:
                        v1, v2 = v2, v1
                    result.add((v1, v2, v3))

    return list(result)
 

def check_time(lst):
    
    start_time = time.time()
    sum_three(lst, sum = 0)

    used_time = time.time() - start_time

    return used_time


def three_random_lists():
    for i in range(3):
        lst = generate_lst(15)
        result = sum_three(lst, sum = 0)

        print(lst)
        print(result,'\n')


def generate_15_sizes():
    for n in range(300, 825, 35):
        lst = generate_lst(n)
        timee = check_time(lst)

        print(f'{(n - 265) // 35}. n = {n}, {timee}')


def three_attempt_time():
    n_values = [n for n in range(300, 825, 35) ]
    time_1 = []
    time_2 = []
    time_3 = []

    for n in n_values:
        lst = generate_lst(n)
        time_caused = check_time(lst)
        time_1.append(time_caused)
    for n in n_values:
        lst = generate_lst(n)
        time_caused = check_time(lst)
        time_2.append(time_caused)
    for n in n_values:
        lst = generate_lst(n)
        time_caused = check_time(lst)
        time_3.append(time_caused)

    return time_1, time_2, time_3, n_values


def three_attempts_graph(time_1, time_2, time_3, n_values):

    plt.scatter(n_values, time_1, label = 'attempt 1', marker = 'o')
    plt.scatter(n_values, time_2, label = 'attempt 2', marker = '+')
    plt.scatter(n_values, time_3, label = 'attempt 3', marker = 'x')

    plt.xlabel('Size n')
    plt.ylabel('Working time')
    plt.title('3-sum Algorithm(Force)')

    plt.legend()
    plt.show()


def average_time_calculate(time_1, time_2, time_3, n_values):

    average_time = []

    for i in range(len(n_values)):
        average = (time_1[i] + time_2[i] + time_3[i]) / 3
        average_time.append(average)

    return n_values, average_time

def average_time_graph(time_1, time_2, time_3, n_values):
    n_values, average_time = average_time_calculate(time_1, time_2, time_3, n_values)

    plt.scatter(n_values, average_time,label='Average time',marker='+')
    plt.xlabel('Size n')
    plt.ylabel('average time')
    plt.title('Average time for three attempts')

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


def log_log_regression(time_1, time_2, time_3, n_values):
    n_values, average_time = average_time_calculate( time_1, time_2, time_3, n_values)

    log_n = []
    log_time = []

    for i in range(len(n_values)):
        log_n.append(math.log(n_values[i]))
        log_time.append(math.log(average_time[i]))

    m, k = lin_reg(log_n, log_time)

    return log_n, log_time, m, k


def predict_function(time_1, time_2, time_3, n_values):
    log_n, log_time, m, k = log_log_regression( time_1, time_2, time_3, n_values)
    predict_log_time = []

    for i in range(len(log_n)):
        predict_log_time.append(m + k * log_n[i])

    return log_n, log_time, predict_log_time


def log_log_regression_graph( time_1, time_2, time_3, n_values):
    log_n, log_time, predict_log_time = predict_function( time_1, time_2, time_3, n_values)
    plt.plot(log_n, predict_log_time, label = 'Regression line')
    plt.scatter(log_n, log_time, label = 'actual data',marker='x')

    plt.xlabel('log(n)')
    plt.ylabel('log(time)')
    plt.title('log-log regression')

    plt.legend()
    plt.show()


def main():
    print('Requirement c\n')
    three_random_lists()


    time_1, time_2, time_3, n_values = three_attempt_time()


    print('Requirement d ii\n')
    three_attempts_graph(time_1, time_2, time_3, n_values)


    print('Requirement d iii\n')
    average_time_graph(time_1, time_2, time_3, n_values)

    print('Requirement d v\n')
    k = log_log_regression(time_1, time_2, time_3, n_values)[3] 
    print(f'The resulting coefficient is {k}')

    print('Requirement d vi\n')
    log_log_regression_graph(time_1, time_2, time_3, n_values)



main()
