====================
Simple Guided Optics
====================

A small collection of several classical methods for guided optics.



General description
___________________

The package written in Python during my PhD which I didn't achevie. The main benefit of the package is that it is written in an OOP logic. One can create and manipulate such classes as Waveguide and Simulation and deal with them in the abstraction of the calculation methods.

The package contains the following features:

* The calculatiion of propagation constant, effective index, group velocity, GDD, D2 frequency depencences;
* Frequency dependent material parameters are supported as well as constant ones;

* Planar geometry is resolved analytically (Pollock Lipson);
* Slab geometry is resolved with the famework of a modified Marcatili method (Menon, 2002);
* Goell's method is supported as well;



Features to come asap
_____________________

* Coupled wave solutions for waveguide Bragg gratings: planar, slab, TE/TM modes propagation/radiation type;
* Several primitive devices such as rings (add-drop, all pass), modulators;
* Pulse propagation in linear media;



Putting the package on use
__________________________

There are two main classes in the package ``Waveguide`` and ``Simulation``. By calling the ''Waveguide'' instance, the waveguide can be created. Initially, it contains the following attributes:
- height, width in micrometers;
- substrate, core and cladding materials;
+ in the case of a rectandular cross-section there will be only the cladding;


Installation 
____________
via PyPI