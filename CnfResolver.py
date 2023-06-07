from pysat.formula import CNF
import numpy as np


class CnfResolver:
    def __init__(self, path_to_file):
        self.positive_contribution = {}
        self.negative_contribution = {}
        self.cnf = CNF(from_file=path_to_file)
        self.nv = self.cnf.nv
        self.clauses_size = len(self.cnf.clauses)
        i = 0
        for clause in self.cnf.clauses:
            for variable in clause:
                if variable > 0:
                    if self.positive_contribution.get(variable) is None:
                        self.positive_contribution[variable] = set()
                    self.positive_contribution[variable].add(i)
                else:
                    if self.negative_contribution.get(-variable) is None:
                        self.negative_contribution[-variable] = set()
                    self.negative_contribution[-variable].add(i)
            i += 1

    def count_number_of_satisfactions(self, cnf_evaluation):
        result = 0
        satisfied_parts = np.zeros(self.clauses_size)
        for i in range(self.nv):
            if cnf_evaluation[i] == 1:
                contribution_set = self.positive_contribution[i+1]
                for part in contribution_set:
                    if satisfied_parts[part] == 0:
                        satisfied_parts[part] = 1
                        result += 1
            else:
                contribution_set = self.negative_contribution[i+1]
                for part in contribution_set:
                    if satisfied_parts[part] == 0:
                        satisfied_parts[part] = 1
                        result += 1

        return result
