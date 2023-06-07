from CnfResolver import CnfResolver
import numpy as np
import random
import math

cnf = CnfResolver('Input.cnf')
max_iteration = cnf.clauses_size
max_answer = cnf.nv
temperature = cnf.clauses_size
t_coefficient = 0.8
noise_possibility = 0.4


def convert_to_cnf(cnf_valuation):

    return [(i+1 if cnf_valuation[i] == 1 else -(i+1)) for i in range(len(cnf_valuation))]


def fitness(cnf_valuation):
    global cnf

    return cnf.count_number_of_satisfactions(cnf_valuation)


def add_noise(cnf_valuation):
    global noise_possibility

    for value in range(len(cnf_valuation)):
        random_number = random.random()
        if random_number <= noise_possibility:
            cnf_valuation[value] ^= 1

    return cnf_valuation


def possibility(fitness1, fitness2):
    global temperature

    delta_f = math.fabs(fitness1 - fitness2)
    result = math.exp(-delta_f / temperature)
    return result


def simulated_annealing(starting_point):
    global temperature
    global t_coefficient

    for i in range(max_iteration):
        print(f'iter {i}')
        temperature *= t_coefficient
        while True:
            temp_cnf_valuation = add_noise(cnf_valuation=starting_point)
            fitness1 = fitness(starting_point)
            fitness2 = fitness(temp_cnf_valuation)
            if fitness1 < fitness2:
                starting_point = temp_cnf_valuation
                print(f'new value {fitness2}')
                break
            rand_num = random.random()
            if rand_num <= possibility(fitness1, fitness2):
                starting_point = temp_cnf_valuation
                print(f'new value {fitness2}')
                break

        # checking the end conditions:
        if fitness(starting_point) == max_answer:
            break
    print(starting_point)


simulated_annealing(np.random.choice([0, 1], size=cnf.nv))
