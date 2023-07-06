import random

class pmf:
    def __init__(self, probabilities, values):
        self.probabilities = probabilities
        self.values = values

def sample_once(pmf):
    randomValue = random.uniform(0, 1)
    probabilitySum = 0
    index = 0
    while (index < len(pmf.probabilities)):
        probabilitySum = probabilitySum + pmf.probabilities[index]
        if (randomValue < probabilitySum):
            return pmf.values[index]
        index = index + 1
    return pmf.values[-1]

def sample(sample_size, pmf):
    returnList = []
    for i in range(sample_size):
        returnList.append(sample_once(pmf))
    return returnList

def repeated_sample_sum(num_samples, sample_size, pmf):
    returnList = []
    for i in range(num_samples):
        sample_sum = sum(sample(sample_size, pmf))
        returnList.append(sample_sum)
    return returnList