from vpython import sphere, vector, rate, color
import numpy as np

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
AU = 1.496e11    # Astronomical unit in meters
DAY = 24*3600    # One day in seconds

# Planet data: (name, mass (kg), distance from Sun (AU), radius (m), color)
planets = [
    ("Mercury", 3.30e23, 0.39, 2.44e6, color.gray(0.5)),
    ("Venus", 4.87e24, 0.72, 6.05e6, color.yellow),
    ("Earth", 5.97e24, 1.00, 6.37e6, color.blue),
    ("Mars", 0.642e24, 1.52, 3.39e6, color.red),
    ("Jupiter", 1898e24, 5.20, 69.91e6, color.orange),
    ("Saturn", 568e24, 9.58, 58.23e6, color.yellow),
    ("Uranus", 86.8e24, 19.2, 25.36e6, color.cyan),
    ("Neptune", 102e24, 30.1, 24.62e6, color.blue)
]

# Create the Sun
sun = sphere(pos=vector(0, 0, 0), radius=6.96e8 * 10, color=color.orange, emissive=True)

# Create planet spheres
planet_objs = []
for name, mass, distance, radius, col in planets:
    pos = vector(distance * AU, 0, 0)
    planet = sphere(pos=pos, radius=radius * 200, color=col, make_trail=True, retain=100)
    planet.velocity = vector(0, np.sqrt(G * 1.989e30 / (distance * AU)), 0)  # Orbital velocity
    planet.mass = mass
    planet_objs.append(planet)

# Simulation loop
dt = 0.01 * DAY  # Time step in seconds
while True:
    rate(200)  # Frame rate

    for planet in planet_objs:
        # Calculate gravitational force from Sun
        r = planet.pos - sun.pos
        force = -G * 1.989e30 * planet.mass / r.mag2 * r.hat

        # Update velocity and position
        planet.velocity += force / planet.mass * dt
        planet.pos += planet.velocity * dt
