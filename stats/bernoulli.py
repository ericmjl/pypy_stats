from random import random

class bernoulli(object):
    """
    docstring for bernoulli
    """
    def __init__(self, p):
        super(bernoulli, self).__init__()
        self.p = p
        
    def rvs(self, n):
        draws = []
        for i in range(n):
            draws.append(int(random() > self.p))

        return draws