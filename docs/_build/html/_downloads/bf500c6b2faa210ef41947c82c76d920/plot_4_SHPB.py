#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Use :class:`Waveprop` to simulate SHPB
======================================

"""

import matplotlib.pyplot as plt
from prop1D import WP2, Barhete


# %%
# Define material parameters
E = 201e9  # Young modulus [Pa]
rho = 7800  # Density [kg/m3]


# %%
# SHPB bar configuration
b_kolsky = Barhete([E, E, 0.8*E, E], [rho, rho, rho, rho], [.6, 3, .05, 3.1],
                   [0.028, 0.030, 0.025, 0.030], nmin=4)
testk = WP2(b_kolsky, nstep=400, left='free', right='free', Vinit=5)
testk.plot('shpb')



# %%
# Get force at both ends of sample (segment index ``iseg=2``)
f1, v1, x1, ind1 = testk.getSignal(x=0, iseg=2, plot=False)
f2, v2, x2, ind2 = testk.getSignal(x=0.05, iseg=2, plot=False)


# %%
# Plot forces in the sample
plt.figure('Fsample')
plt.plot(testk.time*1e6, -f1/1000, '-', label='left')
plt.plot(testk.time*1e6, -f2/1000, '-', label='right')
plt.xlabel('time [µs]')
plt.ylabel('force [kN]')
plt.legend()
