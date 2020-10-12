import numpy as np

from simpleoptics.waveguide import Waveguide
from simpleoptics.simulators.rectangular import *

# refer to planar.py for introductory remarks
wg1 = Waveguide(substrate=False, core='si', cladding='sio2',
                width=0.5, height=0.22)

simul = Simulation_Goell(waveguide=wg1,units='frequency',
                          start=191, stop=196, points=11,
                          modeclass=3, number_of_harmonics=12)

simul.simulate(wg1)

a = wg1.width
b = wg1.height

lam = wg1.wavelength
w = wg1.pulsation
f = wg1.frequency
ng = wg1.ng(frequency=191.2)
V = wg1.V
beta = wg1.beta
beta3norm = wg1.beta_normalised