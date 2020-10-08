from simpleoptics.waveguide import Waveguide
from simpleoptics.simulators.planar import *

# from matplotlib import pyplot as pp

    # dimensions
height = 0.22              # [μm]

    # materials
# substrate = 'sio2'
core =      'si'
cladding =  'sio2'
# substrate = 'n = 1.444'
# core =    'n = 3.4'
# cladding ='n = 1.444'

    # ranges
units = 'wavelength'       # [μm]
start = 1.3
stop = 1.9
points = 11

        ## Setting the simulation
    # waveguide
# wg1 = Waveguide(substrate=substrate, core=core, cladding=cladding,
#                 height=height)
wg1 = Waveguide(core=core, cladding=cladding,
                height=height)

    # simulation
sim = Simulation_planar(waveguide=wg1,units=units,
                          start=start, stop=stop, points=points,
                          polarisation='TE', modenumber=0)

sim.simulate(wg1)
#
# V = wg1.V
# beta = wg1.beta
#
#         ## Results
# pp.plot(wg1.V, wg1.beta)
# pp.show()