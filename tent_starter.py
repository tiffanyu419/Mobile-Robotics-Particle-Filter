#E28_problem_set_9
#Tiffany Yu

import numpy as np
import matplotlib.pyplot as plt

# Given an array of values x in the interval [-0.5, 0.5], evaluate the
# probability density function for each x value. The total area under
# the PDF should integrate to 1.
def tent_pdf(x):
    result = []
    for i in x:
        if i < 0:
            y = 2+4*i
        else:
            y = 2-4*i
        result.append(y)
    
    return result

# Given an array of values in the interval [-0.5, 0.5], evaluate the
# cumulative density function for each x value. The CDF should be
# monotonically increasing from 0 at -0.5 to 1 at 0.5.
def tent_cdf(x):
    result = []
    for i in x:
        if i < 0:
            y = 2*i + 2*np.power(i,2) +0.5
        else:
            y = 2*i - 2*np.power(i,2) +0.5
        result.append(y)

    return result

# Given an array of probabilities q in the interval [0,1], return the
# corresponding values x in the range [-0.5, 0.5] such that cdf(x) = q.
def tent_invcdf(q):
    result = []
    for i in q:
        if i < 0.5:
            y = np.sqrt(i/2) -0.5
        else:
            y = -np.sqrt((1-i)/2) + 0.5
        result.append(y)
    
    return result

# Sample from the tent distribution by first sampling uniform random
# variables and mapping each one through the inverse cumulative
# density function. 
def tent_sample(count):
    list_prob = []
    for i in range(0, count):
        point = np.random.uniform(0,1)
        list_prob.append(point)
    
    list = tent_invcdf(list_prob)

    return list

if __name__ == '__main__':

    x = np.linspace(-0.5, 0.5, 201)
    q = np.linspace(0, 1, 201)

    samples = tent_sample(50000)

    plt.subplot(3,1,1)
    plt.plot(x, tent_pdf(x), 'b-', label='p(x)')
    plt.plot(x, tent_cdf(x), 'r--', label='cdf(x)')
    plt.title('PDF and CDF')
    plt.axis([-0.5, 0.5, 0, 2])
    plt.legend(loc='upper left')

    plt.subplot(3,1,2)
    plt.plot(q, tent_invcdf(q), 'b-')
    plt.axis([0, 1, -0.5, 0.5])
    plt.title('Inverse CDF')

    plt.subplot(3,1,3)
    plt.hist(samples, 25, range=(-0.5, 0.5))
    plt.title('Histogram')
    
    plt.show()

    

    


