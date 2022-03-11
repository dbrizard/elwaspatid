Changelog
=========

.. raw:: html

   <!--- CHANGELOG.md file is the master file. Do not edit changelog.rst file, which is generated with pandoc --->

All notable changes to this project will be documented in this file.

Trying to comply with `semantic
versioning <https://semver.org/spec/v2.0.0.html>`__ and to follow the
format defined at https://keepachangelog.com/en/1.1.0/.

[Unreleased]
------------

To add
~~~~~~

-  plastic wave (may require too large changes).
-  ``fixed`` or ``clamped`` boundary condition
-  ``friction`` and ``damped`` boundary conditions (see DeJuhasz)
-  ``elastic``, ``mass``, ``dashpot`` end conditions (see Graff)
-  impacting mass (left end)

To change
~~~~~~~~~

To fix
~~~~~~

[1.1.0] -2022-03
----------------

Added
~~~~~

-  ``Segment.Z`` must be array and not scalar any more. **CHECK against
   Barhomo.**
-  ``Segment.resetImpedance`` to allow impedance variation inside
   ``Segment``
-  ``WP2.plotDeSaintVenant`` displacement diagram plotting method
-  ``Waveprop.plotDeSaintVenant`` displacement diagram plotting method

Changed
~~~~~~~

-  ``plain`` boundary condition is now called ``infinite``

.. _section-1:

[1.0.2] - 2022-03
-----------------

.. _added-1:

Added
~~~~~

-  detect end of contact between rod with displacement;
-  update boundary conditions (segment.left, .right) accordingly;
-  plot impedance of ``Segment``, and of ``Barhete``

.. _section-2:

[1.0.1] - 2022-02
-----------------

.. _added-2:

Added
~~~~~

-  ``Waveprop``: compute and plot displacement of nodes, stress in
   elements;
-  ``WP2``: compute displacement of nodes (**experimental**)
-  ``WP2.getSignal``: choice of time scale (s, ms, µs)

.. _section-3:

[1.0.0] - 2021
--------------

.. _added-3:

Added
~~~~~

-  ``ElasticImpact`` class.

.. _changed-1:

Changed
~~~~~~~

-  use of ``plt.pcolormesh`` modified in ``WP2.subplot`` method;
-  test cases are now external files (removed from bottom of module).

.. _section-4:

[0.8.0] - 2016
--------------

.. _added-4:

Added
~~~~~

-  ``WP2`` class to overcome the limitations of ``Waveprop``.

.. _section-5:

[0.5.0] - 2014
--------------

.. _added-5:

Added
~~~~~

-  ``Waveprop`` class.
