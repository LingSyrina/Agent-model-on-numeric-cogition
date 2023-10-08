class Circle:    
    def __init__(self, x, y, radius, speed):
        self.x, self.y, self.radius, self.speed = x, y, radius, speed

    def fall(self, dt):
        self.y = self.y - dt * self.speed if self.y - dt * self.speed >= 0 else -100

class Stimuli:
    '''ini_pos, radius, distance, space and speed are global parameters, numerosity is a local parameter'''
    def __init__(self, ini_pos, radius, numerosity, distance, space, speed):
        self.stimuli = []
        x, y = ini_pos
        m = 0
        for n in numerosity:
            stimulus = [Circle(x, y + i * distance + m * space, radius, speed) for i in range(n)]
            m += 1 
            self.stimuli.extend(stimulus)
            
class Agent:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.forward, self.backward = 0, 0

    def sense(self, circle):
        d, r, fov = abs(self.x - circle.x), circle.radius, math.radians(60)
        c = math.atan(fov) * d
        if c - r / math.cos(fov) <= circle.y <= c + r / math.cos(fov):
            deviation = (circle.y - c) / (r / math.cos(fov)) * math.pi / 2
            return math.cos(deviation) * 2 * r
        return 0
            
    def move(self):
        move_distance = (self.forward - self.backward) * 3
        if 0 <= self.x - move_distance <= 3:
            self.x -= move_distance
