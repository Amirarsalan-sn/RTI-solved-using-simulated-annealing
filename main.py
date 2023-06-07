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
n_coefficient = 0.9


def fitness(cnf_valuation):
    global cnf

    result = 0
    for parentheses in cnf.clauses:
        solver = Minisat22()
        solver.add_clause(parentheses)
        if solver.solve(cnf_valuation):
            result += 1
    return result


def add_noise(cnf_valuation):
    global noise_possibility
    global n_coefficient

    for value in range(len(cnf_valuation)):
        random_number = random.randint(1, 10)
        if random_number <= noise_possibility:
            cnf_valuation[value] ^= 1

    noise_possibility *= n_coefficient


def possibility(delta_f):
    global temperature
    global t_coefficient
    pass


def simulated_annealing(starting_point):
    pass


simulated_annealing(np.random.choice([0, 1], size=cnf.nv))
