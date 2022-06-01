Getting started
===============

Installation
------------

From PyPI
^^^^^^^^^

Run the following `pip` command in a terminal to install the module:

::

  pip install elwaspatid


From VCS (GitHub)
^^^^^^^^^^^^^^^^^

To get the last version available on GitHub, run:

::

  python3 -m pip install -e git+https://github.com/dbrizard/elwaspatid.git#egg=elwaspatid

You can also specify the version you want. 
See `VCS Support <https://pip.pypa.io/en/latest/topics/vcs-support/>`_ 
or `Installing from VCS <https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-vcs>`_.

Dependencies
^^^^^^^^^^^^

The present module only requires:

* `numpy <https://numpy.org/>`_
* `matplotlib <https://matplotlib.org/>`_



Testing installation
--------------------

To test the installation, run all the examples. 

The examples can be retrieved from the 
`Github repository <https://github.com/dbrizard/elwaspatid>`_ 
or from the section :ref:`ExamplesLabel`.

*Note: there are no automated tests of the module, because the aim of the module is 
to plot propagation diagrams and the underlying data is made of large matrices. 
However, running all the examples will test all the functionnalities of the module 
and one can check that we get the expected results/diagrams (ie. the correct
relfection/transmission of waves).*


