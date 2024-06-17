# Planet class and its subclasses, which represent the planets in the game. Each planet has a position, gravity, radius, and texture. 
# The Planet class has a method to check for collisions with the ball. 
# Real gravitational pulls for each planet
# Originally size proportions were real but mercury was too small and Jupiter too big 

class Planet():
    def __init__(self, position, gravity, radius, texture): 
        self.position = position
        self.gravity = gravity
        self.radius = radius
        self.texture = texture

    def set_position(self, position):
        self.position = position

    def has_collision(self, ball_position, ball_radius): # Check if the ball has collided with the planet
        distance = (self.position[0] - ball_position[0])**2 + (self.position[1] - ball_position[1])**2
        return distance < (self.radius + ball_radius)**2
    
    
class Mercury(Planet):
    def __init__(self, position):
        super().__init__(position, 3.7, 35, "Assets/textures/planets/mercury.png") 

class Venus(Planet):
    def __init__(self, position):
        super().__init__(position, 8.9, 45, "Assets/textures/planets/venus.png")

class Earth(Planet):
    def __init__(self, position):
        super().__init__(position, 9.8, 50, "Assets/textures/planets/earth.png")

class Mars(Planet):
    def __init__(self, position):
        super().__init__(position, 3.7, 40, "Assets/textures/planets/mars.png")

class Jupiter(Planet):
    def __init__(self, position):
        super().__init__(position, 23.1, 80, "Assets/textures/planets/jupiter.png")

class Saturn(Planet):
    def __init__(self, position):
        super().__init__(position, 9.0, 70, "Assets/textures/planets/saturn.png")

class Uranus(Planet):
    def __init__(self, position):
        super().__init__(position, 8.7, 75, "Assets/textures/planets/uranus.png")

class Neptune(Planet):
    def __init__(self, position):
        super().__init__(position, 11.0, 65, "Assets/textures/planets/neptune.png")


PLANET_LIST = [Mercury((0,0)), Venus((0,0)), Earth((0,0)), Mars((0,0)), Jupiter((0,0)), Saturn((0,0)), Uranus((0,0)), Neptune((0,0))] # List of all planets in the game
