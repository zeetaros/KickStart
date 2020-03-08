import numpy as np
from scipy import stats
from random import seed, randint, gauss

"""
A possible way to get a discrete distribution that looks like the normal distribution
is to draw from a multinomial distribution where the probabilities are calculated from
a normal distribution.
"""

class GameMaster():
    def __init__(self):
        pass

def generate_number(lbound=1, ubound=100, mean=None, std=None):
    """
    By default uniform distrn; if specify mean and std, normal distrn

    ====PARAM====
    lbound: set the lower bound of the range in which the number will be drawn from (inclusive)
    ubound: set the upper bound of the range in which the number will be drawn from (inclusive)
    """
    x = np.arange(lbound, ubound + 1)
    if mean and std:
        prob = stats.norm.pdf(x, loc=mean, scale=std)
        prob = prob / prob.sum() #normalize the probabilities so they sum up to 1
    else:
        prob = np.repeat(1 / len(x), len(x))
    num = np.random.choice(x, p=prob)
    return num