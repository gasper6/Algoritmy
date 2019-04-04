import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
from grafy import data1 as data
from classes import vrchol
from functions import vzd, sk, uhol

vrcholy = []

for i in range(len(data)):
    vrcholy.append(vrchol(data[i][0], data[i][1], i))

for i in range(len(data)):
    for j in data[i][2]:
        vrcholy[i].pridaj_suseda(vrcholy[j])

