# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Mengqi Ye on 2021/6/5
"""
import numpy as np


def np_sum_cross_entropy(A, Y):
    m = A.size
    return -(1.0 / m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))


def np_dot_cross_entropy(A, Y):
    m = A.size
    return -(1.0 / m) * (np.dot(np.log(A), Y.T) + np.dot(np.log(1 - A), (1 - Y).T))
