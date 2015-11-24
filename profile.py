from stats.bernoulli import bernoulli
from stats.binomial import binomial
from time import time

start = time()

bern_draws = bernoulli(0.5).rvs(1000000)
mean = sum(bern_draws) / len(bern_draws)

binom_draws = binomial(100, 0.5).rvs(100)
print(binom_draws)

end = time()

print(end - start)