# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Mengqi Ye on 2021/6/23
"""

from scipy import random
import numpy as np
import matplotlib.pyplot as plt

# 1. Function to Integrate
# 2. Limits
# 3. Random Number Generator
# 4. Loop through M.C. Equation


a = 0
b = np.pi  # Limits of integration
N = 1000


def func(x):
    return np.sin(x)


areas = []
for i in range(N):
    # xrand = np.zeros(N)
    # for i in range(len(xrand)):
    #     xrand[i] = random.uniform(a, b)
    xrand = random.uniform(a, b, N)
    integral = 0.0

    for i in range(N):
        integral += func(xrand[i])

    answer = (b - a) / float(N) * integral
    print(f"The integral from 0 to pi of sin(x): {answer}")

    areas.append(answer)

plt.title("Distribution of Areas Calculated.")
plt.hist(areas, bins=32, ec='cyan')
plt.xlabel("Areas")
plt.show()


