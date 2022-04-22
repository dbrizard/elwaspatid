#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Displacement and contact loss
=============================
This example illustrates the loss of contact when two bars in contact do not
have the same impedance. 
 
"""

import numpy as np
import matplotlib.pyplot as plt
from elwaspatid import Waveprop, WP2, BarSingle, BarSet 
plt.close('all')

E = 210e9  # [MPa]
rho = 7800  # [kg/m3]
L = 1  # [m]
d = 0.02  # [m]

incw = np.zeros(80)  # incident wave
incw[0:20] = 1  # /!\ traction pulse

# %%
# Small impedance against large impedance
# ---------------------------------------
# The impacting bar stays in contact with the right bar during one back-and-forth
# travel of the compression wave in it. Then contact ceases and the left bar
# strarts travelling to the left.
# A Heaviside compression pulse travels down the right bar.
L = 1  # [m]
bar = BarSet([E, E], [rho, rho], [L, 0.5*L], [d, 2*d], nmin=6)
testk = WP2(bar, left='free', right='infinite', Vinit=5)
testk.plot()
testk.plotInterface(0, 'interface')

# %%
# Large impedance against small impedance
# ---------------------------------------
# In that case, the impacting bar stays in contact indefinitly with the right
# bar and a "stair" compression pulse develops in the right bar, with steps of
# decreasing amplitude.
# See also :ref:`sphx_glr_auto_examples_plot_2_ElasticImpact.py`
bar = BarSet([E, E], [rho, rho], [L, L], [d, 0.5*d], nmin=6)
testl = WP2(bar, nstep=150, left='free', right='infinite', Vinit=5)
testl.plot()

testl.plotInterface(0, 'interface2')

# %% 
# Contact loss detection
# ----------------------
# *Did not find yet a combination of bar set and initial conditions (or incident
# wave) showing the usefulness of automatic contact loss detection.*
# 
# This example however shows how to:
#
# - use contact loss detection;
# - modify the section of a bar in a :class:`BarSet`.
#
# Second bar with section increase
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bar = BarSet([E, E], [rho, rho], [.2*L, L], [.8*d, d], nmin=12)
bar.changeSection(iseg=1, l=L/4, d=2*d)  # first section change on second bar
bar.changeSection(iseg=1, l=L/2, d=4*d)  # second section change on second bar
bar.plotProperties('Z')

# %% 
# No contact loss
# ^^^^^^^^^^^^^^^
# Check that no force cross the interface after separation of the two bars.
testm = WP2(bar, nstep=150, left='free', right='infinite', Vinit=5, contactLoss=None)
testm.plot()
testm.plotInterface(0, 'NoCL')
print(testm.contact)

# %% 
# Contact loss
# ^^^^^^^^^^^^
# Again, check that no force cross the interface after separation of the two bars.
testc = WP2(bar, nstep=150, left='free', right='infinite', Vinit=5, contactLoss=1e-9)
testc.plot()
testc.plotInterface(0, 'CL')
print(testc.contact)
