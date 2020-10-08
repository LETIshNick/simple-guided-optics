from simpleoptics.waveguide import Waveguide
from simpleoptics.simulators.planar import *

# dimensions
# the planar waveguide doesn't have a withs, 
# but it is set implicitly set nevertheless to 10 μm

height = 0.22              # [μm]

# materials
# can be defined as strings from the available ones in /epsilon_data/ folder
# or for the consnant values 'n = value' or 'epsr = value'
 # if the substrate is not set it is implicitly equal to the cladding
substrate = 'sio2'
core =      'si'
cladding =  'sio2'

# substrate = 'n = 1.444'
# core =    'n = 3.4'
# cladding ='n = 1.444'

# ranges
# The choice is between wavelengths, frequency and V-number
# with V-number variable materials are not possible (because the normalisation is impossible)
units = 'wavelength'       # [μm]
start = 1.3
stop = 1.9
points = 11

## Setting the simulation
# creating a waveguide
wg1 = Waveguide(substrate=substrate, core=core, cladding=cladding,
                height=height)

# creating a simulation
sim = Simulation_planar(waveguide=wg1,units=units,
                        start=start, stop=stop, points=points,
                        polarisation='TE', modenumber=0)

sim.simulate(wg1)

# available parameters
V = wg1.V
beta = wg1.beta
ng = wg1.ng
neff = wg1.neff
