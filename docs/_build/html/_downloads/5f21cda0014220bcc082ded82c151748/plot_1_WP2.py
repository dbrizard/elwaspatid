#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test :class:`WP2` class
=======================

Define a :class:`Barhete` bar configuration and use it with :class:`WP2` to compute
elastic wave propagation in simple test cases.
"""

import numpy as np
from elwaspatid import WP2, BarSet


# %%
# Define a few parameters
E = 201e9  # Young modulus [Pa]
rho = 7800  # Density [kg/m3]
d = 0.020  # diameter [m]
k = 2.4  # diamters ratio [-]


# %%
# Create the bar configurations
nm = 15
bc = BarSet([E, E], [rho, rho], [.1, .13], [d, d], nmin=nm)
bc2 = BarSet([E, E], [rho, rho], [.1, .13], [d, k*d], nmin=nm)
bc3 = BarSet([E, E], [rho, rho], [.1, .13], [k*d, d], nmin=nm)
bc4 = BarSet([E, E], [rho, rho], [.1, .3], [d, d], nmin=nm)

# %%
# Define the incident wave vector
comp = np.zeros(20)  # incident wave
#comp[0:20] = -1e3  # heavyside, compression (<0)
comp[0:7] = -2e3
comp[15:] = -1e3

# %%
# Two identical bars, free-ends
# -----------------------------
test2 = WP2(bc, comp, nstep=100, left='free', right='free')
test2.plot('2b_free')

# %%
# Two identical bars, free and fixed ends
# ---------------------------------------
test2 = WP2(bc, comp, nstep=100, left='free', right='fixed')
test2.plot('2b_freefixed')

# %%
# Two identical bars, infinite-ends
# ---------------------------------

test2f = WP2(bc, comp, nstep=100, left='infinite', right='infinite')
test2f.plot('2b_anech')

# %%
# Two identical bars with traction pulse
# --------------------------------------
test2t = WP2(bc, -comp, nstep=100, left='free', right='free')
test2t.plot('2b_trac')

# %%
# Two bars, cross-section increase
# --------------------------------
test2a = WP2(bc2, comp, nstep=100, left='free', right='free')
test2a.plot('2b_incre')
# test2av = WP2(bc2, comp, nstep=100, left='free', right='free', Vinit=10)
# test2av.plot('2baugmv')

# %%
# Two bars, cross-section reduction
# ----------------------------------
test2d = WP2(bc3, comp, nstep=100, left='free', right='free')
test2d.plot('2b_reduc')
# test2dv = WP2(bc3, comp, nstep=100, left='free', right='free', Vinit=10)
# test2dv.plot('2bdimiv')
test2d.plotInterface(figname='interf')

# %%
# First bar with initial velocity
# -------------------------------
# Positive velocity: compression
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
test2v = WP2(bc4, comp, nstep=100, left='free', right='free', Vinit=10)
test2v.plot('2b_veloc')

# %%
# Negative velocity
# ^^^^^^^^^^^^^^^^^
# Nothing happens, the left bar travels to the left.
test2vn = WP2(bc4, comp, nstep=100, left='free', right='free', Vinit=-10)
test2vn.plot('2b_negveloc')
