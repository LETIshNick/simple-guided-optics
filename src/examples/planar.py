from simpleoptics.waveguide import Waveguide
from simpleoptics.simulators.planar import *

## Dimensions
# the planar waveguide doesn't have a width, 
# nevertheless it is implicitly set to 10 μm,
# which can be changed if necessary

height = 0.22              # [μm]

## Materials
# can be defined as strings from the available ones in the /epsilon_data/
# or in the form of 'n = value' or 'epsr = value'
# if the substrate is not set it is implicitly equal to the cladding
substrate = 'sio2'
core =      'si'
cladding =  'sio2'

## Calculation ranges
# The choice is between wavelengths, frequency and V-number
# with V-number variable materials are not possible 
# (because the normalisation is impossible)
units = 'wavelength'       # [μm]
start = 1.3
stop = 1.9
points = 101

## Setting the simulation
# creating a waveguide (substrate can be simply omitted)
wg1 = Waveguide(substrate=substrate, core=core, cladding=cladding,
                height=height)

# creating a simulation
sim = Simulation_planar(waveguide=wg1,units=units,
                        start=start, stop=stop, points=points,
                        polarisation='TE', modenumber=0)

sim.simulate(wg1)

# available output parameters
V = wg1.V
beta = wg1.beta
ng = wg1.ng

# all parameters can be called on a certain freq, wavelength or V
neff_1550 = wg1.neff(wavelength=1.55)
