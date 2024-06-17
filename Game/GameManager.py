import random
import Game.planet as planet
import math 
import pygame

# Constants
BALL_RADIUS = 10
HOLE_RADIUS = 40

class GameManager:
    # Manages the game state, including the ball, hole, and planets.
    # Handles game initialization, updates, and game state transitions.

    def __init__(self, width, height):
        # Initializes the GameManager with the given screen width and height.
        self.ball_position = (0, 0)
        self.ball_velocity = (0, 0)
        self.hole_position = (0, 0)
        self.planets = []
        self.state = 0  # 0 = waiting, 1 = running, 2 = win, 3 = lose
        self.Difficulty = 0
        self.time = 0
        self.width = width
        self.height = height
    
    def _generate_planets(self):
        # Generates planets based on the difficulty level. 
        # Places planets randomly within specific zones on the screen to avoid overlap.
        
        num_planets = self.Difficulty + 1  # Number of planets to generate based on difficulty
        planet_list = planet.PLANET_LIST.copy()
        zone_width = self.width // 5  # Divide the screen into 5 zones (zone 0 = start, zone 4 = hole)
        zones = [1, 2, 3]

        # Select and place planets in random zones
        for i in range(num_planets):
            random_planet = random.choice(planet_list)
            planet_list.remove(random_planet)
            self.planets.append(random_planet)

            random_zone = random.choice(zones)
            zones.remove(random_zone)

            # Randomly place the planet in the selected zone
            planet_min_x = random_zone * zone_width + random_planet.radius
            planet_max_x = (random_zone + 1) * zone_width - random_planet.radius
            planet_min_y = random_planet.radius
            planet_max_y = self.height - random_planet.radius
            planet_x = random.randint(planet_min_x, planet_max_x)
            planet_y = random.randint(planet_min_y, planet_max_y)
            random_planet.set_position((planet_x, planet_y))

    def start(self):
        # Starts a new game by resetting the game state, placing the ball and hole, and generating planets.
        
        self.state = 0
        self.time = 0
        self.planets = []

        # Place ball at the left border in the middle
        self.ball_position = (BALL_RADIUS + 20, self.height // 2)
        self.ball_velocity = (0, 0)

        # Randomly place the hole
        hole_min_x = 4 * self.width // 5
        hole_max_x = self.width - HOLE_RADIUS
        hole_min_y = HOLE_RADIUS
        hole_max_y = self.height - HOLE_RADIUS
        random_x = random.randint(hole_min_x, hole_max_x)
        random_y = random.randint(hole_min_y, hole_max_y)
        self.hole_position = (random_x, random_y)

        # Generate planets
        self._generate_planets()

    def set_velocity(self, velocity):
        # Sets the velocity of the ball and starts the game.
        
        self.ball_velocity = velocity
        self.state = 1

    def set_difficulty(self, Difficulty):
        # Sets the difficulty level of the game.
        
        self.Difficulty = Difficulty

    def update(self, dt):
        # Updates the game state. Moves the ball, checks for collisions,
        # updates game time, and determines win/loss conditions.
        
        if self.state != 1:
            return
        
        self.time += dt
        if self.time > 20000:
            self.state = 3  # Game over due to time limit
            return
                
        # Update the ball position
        self.ball_position = (
            self.ball_position[0] + self.ball_velocity[0] * dt,
            self.ball_position[1] + self.ball_velocity[1] * dt
        )
        
        hit = pygame.mixer.Sound("Assets/Sound/hit.mp3")

        for p in self.planets:
            dx = p.position[0] - self.ball_position[0]
            dy = p.position[1] - self.ball_position[1]
            distance_squared = dx**2 + dy**2
            distance = math.sqrt(distance_squared)
            g = (p.gravity * 6.5) / distance_squared
            # Acceleration in x direction
            ax = g * dx / distance
            # Acceleration in y direction
            ay = g * dy / distance
            self.ball_velocity = (
                self.ball_velocity[0] + ax * dt,
                self.ball_velocity[1] + ay * dt
            )

            # Check for collision with the planet
            collision = p.has_collision(self.ball_position, BALL_RADIUS)
            if collision:
                hit.play()
                self.state = 3  # Game over due to collision
                break

        walls = pygame.mixer.Sound("Assets/Sound/shoot.mp3")
        walls.set_volume(0.5)
        # Check for collision with the walls
        if self.ball_position[0] - BALL_RADIUS < 0:
            walls.play()
            self.ball_velocity = (-self.ball_velocity[0], self.ball_velocity[1])
            self.ball_position = (BALL_RADIUS, self.ball_position[1])
        if self.ball_position[0] + BALL_RADIUS > self.width:
            walls.play()
            self.ball_velocity = (-self.ball_velocity[0], self.ball_velocity[1])
            self.ball_position = (self.width - BALL_RADIUS, self.ball_position[1])
        if self.ball_position[1] - BALL_RADIUS < 0:
            walls.play()
            self.ball_velocity = (self.ball_velocity[0], -self.ball_velocity[1])
            self.ball_position = (self.ball_position[0], BALL_RADIUS)
        if self.ball_position[1] + BALL_RADIUS > self.height:
            walls.play()
            self.ball_velocity = (self.ball_velocity[0], -self.ball_velocity[1])
            self.ball_position = (self.ball_position[0], self.height - BALL_RADIUS)

        victory = pygame.mixer.Sound("Assets/Sound/xp_orb.mp3")
        # Check for victory
        distance = (
            (self.hole_position[0] - self.ball_position[0])**2 +
            (self.hole_position[1] - self.ball_position[1])**2
        )
        if distance < (HOLE_RADIUS + BALL_RADIUS)**2:
            victory.play()
            self.state = 2  # Victory
