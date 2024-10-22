## Overview:
- Objective: Simulate the orbits of planets around the Sun using basic Newtonian mechanics.
- Requirements: Python with vpython library for 3D graphics and numpy for numerical computations.
- Concept: Each planet is treated as a point mass orbiting the Sun, following elliptical orbits defined by Kepler's laws.

## Requirements:
1. Python Installed: Make sure Python is installed.
2. Install Required Libraries: Install vpython and numpy using:
```bash
pip install vpython numpy
```
## Explanation:
1. Constants and Planet Data:
- The gravitational constant (G), astronomical unit (AU), and a day in seconds (DAY) are defined.
- Each planet's data includes name, mass, distance from the Sun (in AU), radius, and color.
2. Creating the Sun and Planets:

- A 3D sphere is created for the Sun.
- Each planet is also represented as a sphere with a trail for its orbit.

3. Simulation Loop:
- The script continuously updates the position and velocity of each planet based on gravitational attraction toward the Sun.
- The rate() function controls the animation speed.
## Laboratory Requirements:
- **Experiment with Parameters:** Modify orbital parameters, initial velocities, or time steps to see how the simulation changes.
- **Extend the Simulation:** You could add moons, tilt planetary axes, or model more complex gravitational interactions.
