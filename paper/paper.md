---
title: 'ELWA-SPATID: A Python package to compute space-time diagrams for the propagation of elastic waves in 1D rods'
tags:
  - Python
  - mechanics
  - elastic wave propagation
  - space-time diagram
authors:
  - name: Denis Brizard^[First author] # note this makes a footnote saying 'Co-first author'
    orcid: 0000-0003-2264-7131
    affiliation: 1 # (Multiple affiliations must be quoted)
affiliations:
 - name: Univ Lyon, Université Claude Bernard Lyon 1, Univ Gustave Eiffel, LBMC UMR_T 9406, F-69622, Lyon, France
   index: 1
date: March 2022
bibliography: paper.bib

---

# Summary

*Begin your paper with a summary of the high-level functionality of your software for a non-specialist reader. Avoid jargon in this section.*


Space-time diagrams are a way to visualize the propragation of mechanical 
(traction-compression) waves. Transmission and reflection of waves across section
changes and contact interfaces can quickly become hard to compute manually 
[@johnson_impact_1972] or with the graphodynamical method [@dejuhasz_graphical_1949]
[@fischer_longitudinal_1959] when multiple waves are combined because of wave 
superposition. 
Additionally, we are often limited to simple wave shapes such as the classical
rectangular pulse and to bars with constant cross-section; deviating from these
conditions rapidly complicates the calculations. 

# Statement of need

`ELWA-SPATID` is a Python package for 1D elastic wave propagation dedicated to 
the computation of space-time diagrams. 


The package is limited to non dispersive propagation, but this approximation 
is rather acceptable in numerous cases, when XXX. The material is also supposed
to stay in the elastic range. 




# Functionality

The underlying equations are derived from [@bacon_numerical_1993], with a 
formulation in Force and Velocity. The rods are discretized -between nodes- into segments, each
segment is supposed to have a constant impedance. The length of each segments is
chosen so that the transit time of the elastic wave in all the segments is 
identical, which enables the use of the method of characteristics. 

Force and Velocit are computed at the nodes, the Displacement is then deduced 
from the Velocity of the nodes. From the Displacement of the nodes, we deduce
the Strain in the segments from the Displacement at the nodes, and the Stress 
in the elements from the Strain in the elements.

## Initial conditions

The bars are initially at rest (null velocity). It is also possible to prescribe 
the intiial velocity of the left bar and therefore model an impactor or stricker.
Conversly, one can provide the pulse shape arriving at the left end of the bar(s).

## Boundary conditions

The following boundry conditions are available:

* contact interface between two bars. Compression waves can cross the interface,
  traction waves cannot;
* free end;
* fixed end (equivalent to a bar clamped to another bar of infinite impedance);
* infinite end. Equivalent to anechoic condition, no reflection of wave occur.

## Visualization

Space-time diagrams are pseudocolor plots with space as x-axis, time as y-axis 
and the wave quantity as color. The wave-related quantity can be:

* force
* velocity
* displacement

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Example

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References
