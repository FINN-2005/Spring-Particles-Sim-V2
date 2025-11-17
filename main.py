from pygame_template import *

class Particle(Sprite):
    def __init__(self, pos, fixed = False, *groups):
        super().__init__(*groups)

        self.pos = V2(pos)
        self.fixed = fixed
        self.velocity = V2()
        self.force = V2()

    def draw(self, screen):
        pygame.draw.circle(screen, Color.gray60, self.pos, 10)
        pygame.draw.circle(screen, Color.black, self.pos, 10, 2)
    
    def update(self, dt):
        if not self.fixed:
            self.velocity += self.force * dt
            self.velocity *= 0.998
            self.pos += self.velocity * dt
        self.force = V2()

    def apply_force(self, force:V2):
        self.force += force

    def ground_pound(self, level: int | float):
        if self.pos.y + 10 >= level:
            self.pos.y = level - 10
            self.velocity.y = 0



class Spring(Sprite):
    def __init__(self, a: Particle, b: Particle, k = 1, *groups):
        super().__init__(*groups)

        self.a = a
        self.b = b
        self.k = k
        self.rest_len = (a.pos - b.pos).length()

    def update(self, dt):
        delta = self.a.pos - self.b.pos
        dist = delta.length()
        if dist == 0: return
        direction = delta.normalize()
        displacement = dist - self.rest_len
        force = -self.k * displacement * direction
        damping = 0.01
        relative_velocity = self.a.velocity - self.b.velocity
        damping_force = damping * relative_velocity.dot(direction) * direction
        force -= damping_force
        if not self.a.fixed: self.a.force += force
        if not self.b.fixed: self.b.force -= force

    def draw(self, screen):
        pygame.draw.line(screen, Color.white, self.a.pos, self.b.pos, 1)



class run(APP):
    def setup(self):
        self.particles = Group()
        self.springs = Group()

        self.grid_width = 16
        self.grid_height = 9
 
        for y in range(self.grid_height):
            for x in range(self.grid_width): Particle((x * 50 + APP.HW - 300, y * 50 + 100), False, self.particles)
 
        particles = list(self.particles)
        spring_levels = [
            ([(1, 0), (0, 1)], 0.2),   # structural
            ([(1, 1), (-1, 1)], 0.17),  # shear
            ([(2, 0), (0, 2)], 0.125)    # bend
        ]
        for i, p in enumerate(particles):
            x = i % self.grid_width
            y = i // self.grid_width
            for connections, k in spring_levels:
                    for dx, dy in connections:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < self.grid_width and 0 <= ny < self.grid_height:
                            neighbor_index = ny * self.grid_width + nx
                            if i < neighbor_index:
                                Spring(p, particles[neighbor_index], k, self.springs)
    
    def update(self):
        self.particles.apply_force(V2(0,0.1))       # gravity
        self.springs.update(self.dt)
        self.particles.update(self.dt)
        self.particles.ground_pound(700)

    def draw(self):
        self.springs.draw()
        self.particles.draw()

run()