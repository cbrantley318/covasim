import covasim as cv

# Approach 1: Specify parameters when creating the Sim object
pars = dict(
    pop_size = 60000,    # Number of people in the simulation
    n_days = 50,         # Number of days to simulate
    pop_infected = 4,   # Number of initial infections
)
sim = cv.Sim(pars)
sim.run()

# note: best bet is to increase the number of days to as much as possible.