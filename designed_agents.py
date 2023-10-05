
import math
import matplotlib.pyplot as plt

class Circle:
    def __init__(self, x, y, radius, speed):
        self.x, self.y, self.radius, self.speed = x, y, radius, speed
        
    def fall(self, dt):
        self.y = self.y - dt * self.speed if self.y - dt * self.speed >= 0 else -100

class Agent:
    def __init__(self, x, y):
        self.x, self.y, self.memory, self.inertia = x, y, 0, 0

    def sense(self, circle):
        d, r, fov = abs(self.x - circle.x), circle.radius, math.radians(60)
        c = math.atan(fov) * d
        if c - r / math.cos(fov) <= circle.y <= c + r / math.cos(fov):
            deviation = (circle.y - c) / (r / math.cos(fov)) * math.pi / 2
            return math.cos(deviation) * 2 * r
        return 0
            
    def recall(self, activity):
        self.memory -= 1 if activity > 0 else 0
    
    def time(self, activity): 
        self.inertia = 0 if activity > 0 else (self.inertia + 0.1 if activity == 0 else self.inertia)
        
    def update_memory(self, activity):
        self.memory += 1 if activity > 0 else 0

    def update_position(self, chase_sp, dt):
        if self.memory == 0 and self.inertia >= 1 and 0 < self.x <= 3:
            self.x -= chase_sp * dt
        if self.memory < 0 and 0 <= self.x < 3:
            self.x += chase_sp * dt
        

def dehabituation(agent, circles, test):
    x, y, z = [], [], []
    
    for i in range(200):
        dt = 1 / 50
        activity = 0
        for circle in circles:
            circle.fall(dt)
            activity += agent.sense(circle)
        agent.update_memory(activity)
    
    circles = [Circle(*pos, r, speed) for pos in ini_circles] # modify
    for i in range(250):
        dt = 1 / 50
        activity = 0
        for circle in circles:
            circle.fall(dt)
            activity += agent.sense(circle)
        agent.time(activity)
        agent.recall(activity)
        agent.update_position(chase_sp, 1 / 50)
        x.append(i)
        y.append(activity)
        z.append(agent.x)

    plt.plot(x, y)
    plt.plot(x, z)

# Global parameters
test, chase_sp, ini_agent = 3, 150, (3, 0)
ini_circles = [(0, 10), (0, 15), (0, 20)]
r, speed, distance = 1, 5, 5

# Create agent and circles
agent = Agent(*ini_agent)
circles = [Circle(*pos, r, speed) for pos in ini_circles]

# Call agent_behavior with agent and circles
dehabituation(agent, circles, test)

# Display the plot
plt.show()
    
