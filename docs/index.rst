.. Tutorial documentation master file, created by
   sphinx-quickstart on Fri Dec 17 17:01:18 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================================
Elastic waves space-time diagrams
=================================

ELWA-SPATID is a Python module for the computation of space-time diagrams for
the propagation of elastic waves in 1D rods. The rods can have impedance variations
along the propagation axis, and it is possible to consider several rods in contact.

Initial conditions can be:

* a prescribed input force at the left end of the first rod;
* a prescribed velocity of the left rod, which impacts the next rod.

Boundary conditions can be:

* two rods in contact;
* free end (total reflexion of waves);
* fixed end;
* infinite end (no reflexion, equivalent to anechoic condition).


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
   * trouver mieux que "plain" condition

.. DONE:
   * Examples:
      - ElasticImpact and comparison with WP


Indices and tables
==================

.. * :ref:`modindex`
* :ref:`genindex`
* :ref:`search`
