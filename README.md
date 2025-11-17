# Spring-Particles-Sim-V2

A 2D jelly simulation built with particles, springs, and simple physics.

# Description

This project implements a deformable cloth simulation using a grid of particles connected by springs.  
Each particle responds to gravity, spring forces, and damping while optionally colliding with the ground.  
The springs simulate three types of constraints:  
- Structural springs – maintain grid shape  
- Shear springs – stabilize diagonal deformation  
- Bend springs – maintain curvature / stiffness across larger distances  
This is the second version of my mass–spring system, featuring cleaner structure, better stability, and a more realistic cloth effect compared to V1.

# Features

- Particle-based physics simulation
- Hooke’s law spring forces
- Adjustable stiffness for different spring types
- Basic damping for stability
- Ground collision
- Simple Pygame visualization
- Built on my pygame_template engine

# Installation

- clone the repo
- install my [pygame_template](https://github.com/FINN-2005/pygame_template)
  ```bash
  pip install git+https://github.com/FINN-2005/pygame_template.git
  ```

# Usage

- run the script
  ```bash
  python main.py
  ```
