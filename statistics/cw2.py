import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import bernoulli


def zad1():
    x = np.arange(6)
    p = (1/6, 1/6, 1/6, 1/6, 1/6, 1/6)
    rozklad = stats.rv_discrete(name='rozklad', values=(x, p))
    print("median: ",stats.rv_discrete.median(rozklad))
    print("mean: ",stats.rv_discrete.mean(rozklad))
    print("standard deviation",stats.rv_discrete.std(rozklad))
    print("variance",stats.rv_discrete.var(rozklad))

def zad2_and_3():
    n, p, mu = 100, 1/6,1/6
    mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
    print("binomial distribution")
    print("mean: ",mean)
    print("variance: ",var)
    print("skewnes: ",skew)
    print("kurtosis",kurt)

    mean, var, skew, kurt = bernoulli.stats(p, moments='mvsk')
    print("bernoulli distribution")
    print("mean: ",mean)
    print("variance: ",var)
    print("skewnes: ",skew)
    print("kurtosis",kurt)

    mean, var, skew, kurt = poisson.stats(n, p, moments='mvsk')
    print("poisson distribution")
    print("mean: ",mean)
    print("variance: ",var)
    print("skewnes: ",skew)
    print("kurtosis",kurt)

def zad4():
    n, p, mu = 100, 1/6,1/6
    fig = plt.figure()
    fig.suptitle('Zad4', fontsize=20)
    plt.subplot(1, 3,1)
    x = np.arange(bernoulli.ppf(0.01, p),
                bernoulli.ppf(0.99, p))
    plt.plot(x, bernoulli.pmf(x, p), 'bo', ms=8, label='bernoulli pmf')
    plt.vlines(x, 0, bernoulli.pmf(x, p), colors='b', lw=5, alpha=0.5)

    plt.subplot(1,3,2)
    x = np.arange(binom.ppf(0.01, n, p),
                binom.ppf(0.99, n, p))
    plt.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
    plt.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)

    plt.subplot(1,3,3)
    x = np.arange(poisson.ppf(0.01, mu),
                poisson.ppf(0.99, mu))
    plt.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
    plt.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)
    

def zad5():
    sum = 0
    for i in range(21):
        x = binom.pmf(i,20,0.4)
        sum = sum + x
    print(sum)

def zad6():
    data = stats.norm.rvs(0, 2, size=100)
    print(data)

def zad7():
    fig = plt.figure()
    data = stats.norm.rvs(1, 2, size=500)
    plt.subplot(1,2,1)
    plt.hist(data)
    data = stats.norm.pdf(-1,0.5)
    plt.subplot(1,2,2)
    fig.suptitle('Zad 7', fontsize=20)

zad1()
zad2_and_3()
zad4()
zad5()
zad6()
zad7()
plt.show()
