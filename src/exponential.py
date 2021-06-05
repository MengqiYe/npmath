# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Mengqi Ye on 2021/6/5
"""
from scipy.stats import expon
import matplotlib.pyplot as plt
import numpy as np


def display_density_function(ax, dist: expon):
    # Display the density funtion
    x = np.linspace(dist.ppf(0.01), dist.ppf(0.99), 100)
    ax.plot(x, expon.pdf(x), 'r-', lw=5, alpha=0.6, label='expon pdf')

    return x


def freeze_distribution_and_display_frozen_pdf(ax, x, dist):
    # Freeze the distribution and display the frozen pdf
    rv = dist()
    ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')


def check_accuracy_of_cdf_and_ppf(dist):
    # Check accuracy of cdf and ppf
    vals = dist.ppf([0.001, 0.5, 0.999])
    assert np.allclose([0.001, 0.5, 0.999], dist.cdf(vals))


def generate_random_numbers_compare_the_histogram(ax):
    # Generate random numbers
    r = expon.rvs(size=1000)

    # And compare the histogram
    ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
    ax.legend(loc='best', frameon=False)


def main():
    fig, ax = plt.subplots(1, 1)
    mean, var, skew, kurt = expon.stats(moments='mvsk')

    x = display_density_function(ax, expon)
    freeze_distribution_and_display_frozen_pdf(ax, x, expon)
    check_accuracy_of_cdf_and_ppf(expon)
    generate_random_numbers_compare_the_histogram(ax)
    plt.show()


if __name__ == '__main__':
    main()
