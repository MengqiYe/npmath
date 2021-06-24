# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Mengqi Ye on 2021/6/6
"""
from matplotlib import pyplot
import numpy as np

x = np.linspace(-.1, 10, 110)
y_log = np.log(x)
y_log2 = np.log2(x)
y_log10 = np.log10(x)

pyplot.plot(x, y_log, marker='*')
pyplot.plot(x, y_log2, marker='.')
pyplot.plot(x, y_log10, marker='x')
pyplot.title('xn vs log')
pyplot.subplots_adjust(bottom=0.2)
pyplot.xlabel('Probability Distribution')
pyplot.ylabel('Log')
pyplot.show()
