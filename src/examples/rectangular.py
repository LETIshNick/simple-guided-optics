import numpy as np

from simpleoptics.waveguide import Waveguide
from simpleoptics.simulators.rectangular import *

# look for examples/planar.py to introductory remarks
wg1 = Waveguide(substrate='sio2', core='si', cladding='sio2',
                width=10, height=0.22)

# for the modeclass notation cf. [Menon 2002]
sim = Simulation_rectangular(waveguide=wg1,units='wavelength',
                          start=1.3, stop=1.9,
                          points=101,
                          modeclass=3, method='Menon',
                          polarisation='ex')

sim.simulate(wg1)

## A simple text output
a = wg1.width
b = wg1.height

lam = wg1.wavelength
w = wg1.pulsation
f = wg1.frequency
ng = wg1.ng
V = wg1.V
beta = wg1.beta
beta3norm = wg1.beta_normalised

np.savetxt(output_path + f'/menon_ex11-{a}x{b}-w,lam,beta,ng-const',
           np.column_stack((w,lam,beta,ng)), delimiter=' ')
