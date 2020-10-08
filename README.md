# Simple Guided Optics
A small collection of several classical methods for guided optics.
____
It's written in Python during my PhD which I didn't achevie. The main benefit of the package is that it is written in an OOP logic. One can create and manipulate such classes as Waveguide and Simulation and deal with them in the abstraction of the calculation methods.
____

The package contains the following features:

* The calculatiion of propagation constant, effective index, group velocity, GDD, D2 frequency depencences;
* Frequency dependent materials are supported as well as constant values;

* Planar geometry is resolved analytically (Pollock Lipson);
* Slab geometry is resolved with the famework of a modified Marcatili method (Menon, 2002);
* Goell's method is supported as well;


Features to come asap:

* Coupled wave solutions for waveguide Bragg gratings: planar, slab, TE/TM modes propagation/radiation type;
* Several primitive devices such as rings (add-drop, all pass), modulators;
* Pulse propagation in linear media;


Installation via PyPI