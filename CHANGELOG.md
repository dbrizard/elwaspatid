Changelog
=========

<!--- CHANGELOG.md file is the master file. Do not edit changelog.rst file, which is generated with pandoc --->

All notable changes to this project will be documented in this file.

Trying to comply with [semantic versioning](https://semver.org/spec/v2.0.0.html) and to follow the format defined at https://keepachangelog.com/en/1.1.0/.

## [Unreleased]
### To add
* plastic wave (may require too large changes).
* `fixed` or `clamped` boundary condition
* `friction` boundary condition
* `damped` boundary condition
* `elastic`, `mass`, `dashpot` end conditions (see Graff)

### To change

### To fix


## [1.1.0] -2022-03
### Added
* `Segment.Z` must be array and not scalar any more. __CHECK against Barhomo.__
* `Segment.resetImpedance` to allow impedance variation inside `Segment`

### Changed
* `plain` boundary condition is now called `infinite`

## [1.0.2] - 2022-03
### Added
* detect end of contact between rod with displacement;
* update boundary conditions (segment.left, .right) accordingly;
* plot impedance of `Segment`, and of `Barhete`

## [1.0.1] - 2022-02
### Added
* `Waveprop`: compute and plot displacement of nodes, stress in elements;
* `WP2`: compute displacement of nodes (__experimental__)
* `WP2.getSignal`: choice of time scale (s, ms, µs)


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
