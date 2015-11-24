from random import random

class bernoulli(object):
    """
    docstring for bernoulli
    """
    def __init__(self, p):
        super(bernoulli, self).__init__()
        self.p = p
        
    def rvs(self, num_draws):
        draws = []
        for i in range(num_draws):
            draws.append(int(random() > self.p))

        return draws