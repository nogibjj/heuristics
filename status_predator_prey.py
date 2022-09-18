#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple predator-prey model using status strategies:  ["dominance", "virtue", "achievment"]

Initial idea is figure out group membership effects on the predator-prey model where it is a zero sum game to achieve status.

https://scientific-python.readthedocs.io/en/latest/notebooks_rst/3_Ordinary_Differential_Equations/02_Examples/Lotka_Volterra_model.html
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

Other ideas:

* Can we model an iterative prisoner's dilemma where multiple group memberships create a better outcome in status by playing the game
a metaheruistic game?

possibile inspiration: https://github.com/INASIC/predator-prey_systems/blob/master/Modelling%20Predator-Prey%20Systems%20in%20Python.ipynb

"""
from random import random

TOTAL_STATUS = 100


def get_status():
    return random() * TOTAL_STATUS


def get_status_group(status):
    if status < 25:
        return "low"
    elif status < 50:
        return "mid"
    else:
        return "high"
