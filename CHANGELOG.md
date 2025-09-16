Changelog
=========

<!--- CHANGELOG.md file is the master file. Do not edit changelog.rst file, which is generated with pandoc

_Readthedoc_:
* il est parfois nécessaire d'attendre après un commit pour pouvoir compiler la doc. 
* `requirements: docs/RTDrequirements_short.txt` in .readthedocs.yaml does not works
* requirement was therefore added online in Admin > Advanced Settings

Types of changes:
 * `Added` for new features.
 * `Changed` for changes in existing functionality.
 * `Deprecated` for soon-to-be removed features.
 * `Removed` for now removed features.
 * `Fixed` for any bug fixes.
 * `Security` in case of vulnerabilities.

--->

All notable changes to this project will be documented in this file.

Trying to comply with [semantic versioning](https://semver.org/spec/v2.0.0.html) and to follow the format defined at https://keepachangelog.com/en/1.1.0/.

## [Unreleased]
### To add
#### Long term
* plastic wave (probably impossible here as it requires too large changes);

#### Middle term
* `friction` and `damped` boundary conditions (see DeJuhasz reference);
* `elastic`, `mass`, `dashpot` end conditions (see Graff reference);
* impacting mass (left end);

#### Short term
* test and check `indV` argument of `Waveprop` class;
* plot Stress and Strain in `Segment` for `WP2`;
* ~~_Lagrangian x-t diagram_ keyword should appear and be in description~~ and in JOSS paper;
* modeling of impact on transfer flange (for tension testing simulation).

### To change


## [2.0.2] - 2022-06-29
Minor fixes (paper update). Release related to JOSS review.

## [2.0.1] - 2022-04-19
### Added
* more comments on the interpretation of space-time diagrams of the examples.

### Changed
* `Barhete` is now `BarSet`, which is more meaningfull;
* `Barhomo` is now `BarSingle`, which is more meaningfull too.


## [2.0.0] - 2022-03-08
### Changed
* New name for the module (`elwaspatid`), identical to project name, for consitancy.


## [1.1.0] - 2022-03-15
### Added
* `Segment.Z` must be array and not scalar any more;
* `Segment.resetImpedance` to allow impedance variation inside `Segment`;
* `WP2.plotDeSaintVenant` displacement diagram plotting method;
* `Waveprop.plotDeSaintVenant` displacement diagram plotting method;
* `fixed` boundary condition for `Waveprop`;
* `fixed` boundary condition for `WP2`;
* compute Stress and Strain in `Segment` for `WP2`;

### Changed
* `plain` boundary condition is now called `infinite` (meaningful).


## [1.0.2] - 2022-03
### Added
* detect end of contact between rod with displacement;
* update boundary conditions (segment.left, .right) accordingly;
* plot impedance of `Segment`, and of `Barhete`.


## [1.0.1] - 2022-02
### Added
* `Waveprop`: compute and plot displacement of nodes, stress in elements;
* `WP2`: compute displacement of nodes (__experimental__);
* `WP2.getSignal`: choice of time scale (s, ms, µs).


## [1.0.0] - 2021
### Added
* `ElasticImpact` class.

### Changed
* use of `plt.pcolormesh` modified in `WP2.subplot` method;
* test cases are now external files (removed from bottom of module).


## [0.8.0] - 2016
### Added
* `WP2` class to overcome the limitations of `Waveprop`.


## [0.5.0] - 2014
### Added
* `Waveprop` class.
