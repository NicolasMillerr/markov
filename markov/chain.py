import numpy as np


class MarkovChain:
    def __init__(self, input_list):
        self.input = input_list
        self.states = set(input_list)
        self.transition = {}
        self.build_transition()

    def make_pairs(self):
        pairs = []
        for i in range(len(self.input) - 1):
            pairs.append((self.input[i], self.input[i + 1]))
        return pairs

    def build_transition(self) -> None:
        for v1, v2 in self.make_pairs():
            if v1 in self.transition.keys():
                self.transition[v1].append(v2)
            else:
                self.transition[v1] = [v2]

    def sample_next(self, value):
        return np.random.choice(self.transition[value])

    def build_sequence(self, n: int, root) -> list:
        rv = [root]
        curr = root
        for _ in range(n - 1):
            curr = self.sample_next(curr)
            rv.append(curr)
        return rv
