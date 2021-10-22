import random
import numpy as np
import matplotlib.pyplot as plt
import math

set_range = 10.24
upper_bound = 5.12
lower_bound = -5.12



# Getting the input from the user
cand = []
var = []

print("Enter the number of candidates: ")
candidates = int(input())

"""for i in range(0, candidates):
    c = input()
    cand.append(c)"""

print("Enter the number of variables: ")
variables = int(input())

"""for j in range(0,variables*candidates):
    v = input()            # Individual variables for each candidate
    var.append(v)"""

test_array = np.empty([candidates, variables])

print("Generating random values for variables in the specified range")

for k in range(0, candidates):
    for h in range(0, variables):
        test_array[k][h] = round(random.uniform(lower_bound, upper_bound), 3)

# test_array = np.array([[0.5, 1], [-1, 2], [1, -2]])
print(test_array)

print("Enter the reduction factor: ")
reduction_factor = round(float(input()), 2)


def function_calc_sphere():
    list_fvalues = []

    for m in range(0, candidates):
        a = np.sum(np.square(np.array(test_array[m])))
        list_fvalues.append(a)

    # print(list_fvalues)

    return list_fvalues



def prob_calc(list_fvalues):
    temp_num = np.array(list_fvalues)
    list_pvalues = []
    for i in range(0, candidates):
        list_pvalues.append(((1 / list_fvalues[i]) / sum(np.reciprocal(temp_num))))

    # print(list_pvalues)
    return list_pvalues


def roulette_prob():
    list_roulette = []
    for t in range(0, candidates):
        list_roulette.append(round(random.uniform(0, 1), 2))
    # print(list_roulette)
    return list_roulette


def roulette(list_pvalues):
    list_cumulative = [sum(list_pvalues[0:x:1]) for x in range(0, candidates + 1)]
    # print(list_cumulative)
    return list_cumulative


def attempt(list_cumulative, list_roulette):
    global set_range

    aux = []
    arr = np.empty([candidates, variables])
    for i in list_roulette:
        # aux.append(list_cumulative.index(min(list_cumulative, key=lambda x: abs(x - i))))
        for j in range(0, len(list_cumulative) - 1):
            if list_cumulative[j] < i <= list_cumulative[j + 1]:
                aux.append(j)
    # print(aux)
    for l in range(0, candidates):
        p = aux[l]
        f = test_array[p]
        # print(f)

        arr[l] = f
    # print(arr)
    sampling_range = set_range * reduction_factor

    # print(sampling_range)
    new_upper_bound = round(sampling_range / 2, 3)
    new_lower_bound = round(-(sampling_range / 2), 3)
    set_range = new_upper_bound - new_lower_bound

    # print(new_upper_bound)
    # print(new_lower_bound)
    sampling_intervals = np.empty([candidates, variables], dtype=tuple)
    for q in range(candidates):
        for x in range(variables):
            temp3 = arr[q][x] + new_upper_bound
            temp4 = arr[q][x] + new_lower_bound
            if temp3 > upper_bound:
                temp3 = round(upper_bound, 3)
            if temp4 < lower_bound:
                temp4 = round(lower_bound, 3)
            sampling_intervals[q][x] = (temp4, temp3)
            test_array[q][x] = round(random.uniform(temp3, temp4), 3)
    # print(sampling_intervals)
    # print(test_array)


if __name__ == "__main__":

    x_graph = []
    y_graph = []

    for i in range(1,31):
        x_graph.append(i)
        a = function_calc_sphere()
        y_graph.append(a)
        c = prob_calc(a)
        d = roulette_prob()
        e = roulette(c)
        attempt(e, d)
    plt.plot(x_graph, y_graph)
    plt.xlabel("Iterations")
    plt.ylabel("function values")
    plt.show()
