# ELastic WAve SPAce-TIme Diagrams

[![Documentation Status](https://readthedocs.org/projects/elwaspatid/badge/?version=latest)](https://elwaspatid.readthedocs.io/en/latest/?badge=latest)

[![PyPI version](https://badge.fury.io/py/elwaspatid.svg)](https://badge.fury.io/py/elwaspatid)

`elwaspatid` is a Python module for the computation of space-time diagrams for
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


## Installation

`pip install elwaspatid`

## Documentation

[ReadTheDocs](https://elwa-spatid.readthedocs.io)

## Usage

See the examples in the documentation and in the `examples` folder of the github source.


