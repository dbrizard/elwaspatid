.. Tutorial documentation master file, created by
   sphinx-quickstart on Fri Dec 17 17:01:18 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================================
ELastic WAves SPace-TIme Diagrams
=================================

.. image:: https://readthedocs.org/projects/elwaspatid/badge/?version=latest
   :target: https://elwaspatid.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://badge.fury.io/py/elwaspatid.svg
   :target: https://badge.fury.io/py/elwaspatid

``elwaspatid`` is a Python module for the computation of space-time diagrams for
the propagation of elastic waves in 1D rods. The rods can have impedance variations
along the propagation axis, and it is possible to consider several rods in contact.

Initial conditions can be:

* a prescribed input force at the left end of the left (first) rod;
* a prescribed velocity of the left rod, which impacts the next rod.

Boundary conditions can be:

* free end;
* fixed end;
* contact interface with another rod;
* infinite end (ie. anechoic condition).

This module is the extention of the following reference:

Bacon, C. (1993). Numerical prediction of the propagation of elastic waves in 
longitudinally impacted rods : Applications to Hopkinson testing. 
*International Journal of Impact Engineering*, 13(4), 527‑539. 
https://doi.org/10.1016/0734-743X(93)90084-K


.. figure:: auto_examples/images/sphx_glr_plot_1_WP2_001.png

   Example of force space-time diagram: two successive compression pulses 
   traveling down two bars (with identical cross-section) in contact.


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   getting-started
   auto_examples/index
   api
   changelog


.. TODO:
   * larger figures
   * link to meth and class in html...
   * WRITE ALL THE EXAMPLES !:
     - under the hood

   * comment WP2 and SHPB

.. DONE:
   * Examples:
      - ElasticImpact and comparison with WP
   * trouver mieux que "plain" condition


Indices and tables
==================

.. * :ref:`modindex`
* :ref:`genindex`
* :ref:`search`
