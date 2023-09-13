# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:29:13 2023

@author: r.zor
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.load('data_time.npy')  # Timings of in this case (in microseconds, were  acquired with a controller)

# Mean
mean = np.mean(data)

# Standard deviation
sigma = np.std(data)

# Crop range (to center the main peak)
crop_num = 10000

# Reslution (number of bins)
res = 200

# Histogram
# hist, bins=np.histogram(integral, bins=1000, range=(A-0.01, A+0.01),density=True)
hist, bins = np.histogram(
    data, bins=res, range=(
        mean - crop_num, mean + crop_num), density=True)
hist = hist / np.sum(hist)
center = (bins[:-1] + bins[1:]) / 2
plt.figure(figsize=(8, 8))
plt.plot(center, hist, color='k')
plt.xlabel('Time ($\\mu$s)')
plt.ylabel('Probability density function')

plt.xlim([np.mean(data) - 5000, np.mean(data) + 5000])

plt.axvline(np.mean(data), color='darkgreen', linestyle='dotted', linewidth=2,
            label='Mean = ' + str(round(np.mean(data), 2)) + ' $\\mu$s')
plt.axvline(np.mean(data) + np.std(data), color='firebrick', linestyle='dotted',
            linewidth=2, label='+ $\\sigma$ (' + str(round(sigma)) + ' $\\mu$s) ')
plt.axvline(np.mean(data) - np.std(data), color='firebrick', linestyle='dotted',
            linewidth=2, label='- $\\sigma$ (' + str(round(sigma)) + ' $\\mu$s) ')
plt.axvline(np.mean(data) + 3 * np.std(data), color='darkslategray', linestyle='dotted',
            linewidth=2, label='+ 3$\\sigma$ (' + str(3 * round(sigma)) + ' $\\mu$s) ')
plt.axvline(np.mean(data) - 3 * np.std(data), color='darkslategray', linestyle='dotted',
            linewidth=2, label='- 3$\\sigma$ (' + str(3 * round(sigma)) + ' $\\mu$s) ')

plt.legend()
plt.show()
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
