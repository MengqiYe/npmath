# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Mengqi Ye on 2021/6/24
"""
import numpy as np
from sympy.interactive import printing
printing.init_printing(use_latex=True)
import sympy as sp

x = sp.symbols('x')
func = sp.sin(sp.cos(sp.tan(x)))
rst = sp.diff(func, x)
print(rst)
