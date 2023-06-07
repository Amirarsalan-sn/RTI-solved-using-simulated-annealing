from pysat.formula import CNF
from pysat.solvers import Minisat22
import numpy as np
import random
import math

cnf = CNF(from_file='Input.cnf')
max_iteration = len(cnf.clauses)
max_answer = cnf.nv
temperature = len(cnf.clauses)
t_coefficient = 0.8
noise_possibility = 0.4


def convert_to_cnf(cnf_valuation):

    return [(i+1 if cnf_valuation[i] == 1 else -(i+1)) for i in range(len(cnf_valuation))]


def fitness(cnf_valuation):
    global cnf

    result = 0
    for parentheses in cnf.clauses:
        solver = Minisat22()
        solver.add_clause(parentheses)
        if solver.solve(convert_to_cnf(cnf_valuation)):
            result += 1
    return result


def add_noise(cnf_valuation):
    global noise_possibility

    for value in range(len(cnf_valuation)):
        random_number = random.randint(1, 10)
        if random_number <= noise_possibility:
            cnf_valuation[value] ^= 1

    return cnf_valuation


def possibility(fitness1, fitness2):
    global temperature

    delta_f = math.fabs(fitness1 - fitness2)
    result = math.exp(-delta_f / temperature)
    return result


def simulated_annealing(starting_point):
    print('process started')
    for i in range(max_iteration):
        while True:
            temp_cnf_valuation = add_noise(cnf_valuation=starting_point)
            fitness1 = fitness(starting_point)
            fitness2 = fitness(temp_cnf_valuation)
            if fitness1 < fitness2:
                starting_point = temp_cnf_valuation
                break
            rand_num = random.random()
            if rand_num <= possibility(fitness1, fitness2):
                starting_point = temp_cnf_valuation
                break

        # checking the end conditions:
        if fitness(starting_point) == max_answer:
            break
    print(starting_point)


simulated_annealing(np.random.choice([0, 1], size=cnf.nv))
