#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Under the hood
==============
What happens behind the scene to compute the wave propagation in rods.

Two cases are considered:

* :class:`Waveprop` considers a single rod (with section change);
* :class:`WP2` considers several rods in contact. 

:class:`Waveprop` was the first implementation from the work of Bacon 1993. 
It was kept as it allows faster testing of new features since the computation
of the state of the bar is done internally, whereas this is done externally 
in the case of :class:`WP2` (see below :class:`Segment`).
"""

import numpy as np
import matplotlib.pyplot as plt
from elwaspatid import Waveprop, WP2, BarSingle, BarSet 

E = 210e9  # [MPa]
rho = 7800  # [kg/m3]
L = 1  # [m]
d = 0.02  # [m]

# %%
# Wave propagation with :class:`Waveprop`
# ---------------------------------------
# Bar configuration: one bar at rest with an incident wave.
# Indeed, :class:`Waveprop` eats a single :class:`BarSingle` continuous rod and
# computes internally the propagation of force and velocity along the rod
# and as time increases. 
#
# Since there is no contact interface (single rod), the implementation from 
# the work of Bacon 1993 is straightforward. For each time step:
# 1. compute the force and velocity at the left and right ends; 
# 2. compute the force and velocity in themiddle of the bar  (see :meth:`Waveprop.__init__`).
# All the force values can fill a single matrix, ditto for the velocities.

D = np.linspace(0.5, 4, 40)*d  # bar with linearly increasing diamter
bb = BarSingle(dx=0.01, d=D, E=E, rho=rho)

incw = np.zeros(80)  # incident wave
incw[0:20] = 1  # >0 means traction pulse
test = Waveprop(bb, incw, nstep=2*len(incw), left='free', right='free')

test.plot()  # plot Force and Velocity space-time diagrams
bb.plot(typ='DZ')  # plot discretization of the bar and impedance

# %%
# .. figure:: ../_static/Bacon1993_Figure2.png
#    :scale: 50%
# 
#    Discretization of the rod in elements (from [Bacon 1993])

# %%
# Wave propagation with :class:`WP2`
# ----------------------------------
# :class:`WP2` allows several rods in contact, which means compression crosses
# the contact interface whereas traction cannot cross the contact interface and 
# is therefore reflected.
# 
# Since we consider several rods in contact, the velocity is discontinuous along
# the propagation axis. Hence, force and velocity cannot be computed globally
# and must be evaluated for each rod. Each rod stores force and velocity in two
# matrices. 

# Bar configuration: one striker with initial velocity and one bar at rest
bar = BarSet([E, E], [rho, rho], [L, 0.5*L], [d, 0.8*d], nmin=6)
testk = WP2(bar, nstep=200, left='free', right='infinite', Vinit=5)
testk.plot()

# %%
# Internally, the bar :class:`BarSet` contains a list of :class:`Segment`, one
# for each independant rod. Each :class:`Segment` has been discretized in ``nX``
# elements along the propagation axis.
print(bar.seg)

# %%
# :class:`Segment` has the following methods:
#
# - :meth:`Segment.initCalc`
# - :meth:`Segment.compMiddle`
# - :meth:`Segment.compLeft`
# - :meth:`Segment.compRight`
#
# These methods are called by :meth:`WP2.__init__` which, while looping over time,
# iterates on all the :class:`Segment` in the list provided by :class:`BarSet` to
# compute the state (Force, Velocity) of all the elements of each :class:`Segment`.

# %%
# :class:`Bar` is used to store and plot the evolution of the properties 
# given to :class:`BarSet` at instantiation (in :attr:`BarSet.bar_continuous`)
# Be carfeul, afterwards modifications with :meth:`BarSet.changeSection` do not 
# affect :class:`Bar`.
bar.bar_continuous.plot()
plt.show()