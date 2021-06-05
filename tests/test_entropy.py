# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Mengqi Ye on 2021/6/5
"""
from math import log2
from matplotlib import pyplot
from numpy import asarray, mean

from entropy_math import *
from entropy_math import *

class TestCase_0:
    def setup(self):
        # define distributions
        self.events = ['red', 'green', 'blue']
        self.p = [0.10, 0.40, 0.50]
        self.q = [0.80, 0.15, 0.05]
        # print('P=%.3f Q=%.3f' % (sum(self.p), sum(self.q)))

    def test_plot(self):
        # plot first distribution
        pyplot.subplot(2, 1, 1)
        pyplot.bar(self.events, self.p)
        # plot second distribution
        pyplot.subplot(2, 1, 2)
        pyplot.bar(self.events, self.q)
        # show the plot
        pyplot.show()

    def test_entropy(self):
        # class 1
        p = asarray([1, 0, 0]) + 1e-15
        print(entropy(p))
        # class 2
        p = asarray([0, 1, 0]) + 1e-15
        print(entropy(p))
        # class 3
        p = asarray([0, 0, 1]) + 1e-15
        print(entropy(p))

    def test_cross_entropy(self):
        # calculate cross entropy H(P, Q)
        ce_pq = cross_entropy(self.p, self.q)
        print('H(P, Q): %.3f bits' % ce_pq)
        # calculate cross entropy H(Q, P)
        ce_qp = cross_entropy(self.q, self.p)
        print('H(Q, P): %.3f bits' % ce_qp)
        # calculate cross entropy H(P, Q)

    def test_elementwise_cross_entropy(self):
        # calculate cross entropy for each example
        results = list()
        for i in range(len(self.p)):
            # create the distribution for each event {0, 1}
            expected = [1.0 - self.p[i], self.p[i]]
            predicted = [1.0 - self.q[i], self.q[i]]
            # calculate cross entropy for the two events
            ce = cross_entropy(expected, predicted)
            print('>[y=%.1f, yhat=%.1f] ce: %.3f nats' % (self.p[i], self.q[i], ce))
            results.append(ce)

        # calculate the average cross entropy
        mean_ce = mean(results)
        print('Average Cross Entropy: %.3f nats' % mean_ce)
