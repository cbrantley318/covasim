
import covasim as cv

# Create a simulation
sim = cv.Sim(
    pop_size=10000,          # Population size
    start_day='2020-03-01',  # Start day of the simulation
    end_day='2020-06-01',    # End day of the simulation
    beta=0.015,              # Transmission rate
    interventions=[          # Include interventions
        cv.change_beta(days=['2020-04-01'], changes=[0.5]),  # Reduce transmission by 50% after April 1
    ]
)

# Run the simulation
sim.run()
