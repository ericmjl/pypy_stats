from random import random
from stats.bernoulli import bernoulli

class binomial(object):
    """
    docstring for binomial
    """
    def __init__(self, n, p):
        super(binomial, self).__init__()
        self.p = p
        self.n = n
        
    def rvs(self, num_draws):
        
        draws = []

        for i in range(self.n):
            bern_draws = sum(bernoulli(self.p).rvs(self.n))
            draws.append(bern_draws)

        return draws