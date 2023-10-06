import math
import matplotlib.pyplot as plt
             
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
        self.x, self.y, self.memory, self.inertia = x, y, 0, 0
        self.LTM = []

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
        
    def update_LTM(self):
        if self.inertia >= 1 and self.memory != 0:
            self.LTM.append(self.memory)
            self.memory = 0  

    def forward(self, chase_sp, dt):
        if 0 < self.x <= 3:
            self.x -= chase_sp * dt
    
    def backward(self, chase_sp, dt):
        if 0 < self.x <= 3:
            self.x += chase_sp * dt
            
    def update_position(self, chase_sp, dt):
        if self.memory == 0 and self.inertia >= 1 and 0 < self.x <= 3:
            self.x -= chase_sp * dt
        if self.memory < 0 and 0 <= self.x < 3:
            self.x += chase_sp * dt
                
# addition & habituation with one circle sequence
def addition(agent, test):
    x, y, z = [], [], []
    
    sense = Stimuli(ini_pos, radius, [1,2], distance, space, speed)
    for i in range(400): 
        dt = 1 / 50
        activity = 0
        for circle in sense.stimuli:
            circle.fall(dt)
            activity += agent.sense(circle)        
        # mechanism
        agent.update_memory(activity)
        
    catch = Stimuli(ini_pos, radius, [3], distance, space, speed)
    for i in range(300):
        dt = 1 / 50
        activity = 0
        for circle in catch.stimuli:
            circle.fall(dt)
            activity += agent.sense(circle)       
        # mechanism
        agent.time(activity)
        agent.recall(activity)
        agent.update_position(chase_sp, 1 / 50)
        
        # visualization
        x.append(i)
        y.append(activity)
        z.append(agent.x)

    plt.plot(x, y)
    plt.plot(x, z)

# habituation with two circle sequences
def habituation(agent, test):  
    x, y, z = [], [], []
    
    sense = Stimuli(ini_pos, radius, [2,3], distance, space, speed)
    for i in range(400): 
        dt = 1 / 50
        activity = 0
        for circle in sense.stimuli:
            circle.fall(dt)
            activity += agent.sense(circle)        
        # mechanism
        agent.time(activity)
        agent.update_memory(activity)
        agent.update_LTM()        
        
    catch = Stimuli(ini_pos, radius, [2], distance, space, speed)
    agent.inertia = 0
    for i in range(300):
        dt = 1 / 50
        activity = 0
        for circle in catch.stimuli:
            circle.fall(dt)
            activity += agent.sense(circle)       
        # mechanism
        agent.time(activity)
        agent.update_memory(activity)
        if (agent.memory in agent.LTM)  and agent.inertia >= 1:
            agent.forward(chase_sp, dt)
        
        # visualization
        x.append(i)
        y.append(activity)
        z.append(agent.x)

    plt.plot(x, y)
    plt.plot(x, z)
    
# comparison
def comparison(agent, test):
    x, y, z = [], [], []
    
    sense = Stimuli(ini_pos, radius, [2,3], distance, space, speed)
    for i in range(400): 
        dt = 1 / 50
        activity = 0
        for circle in sense.stimuli:
            circle.fall(dt)
            activity += agent.sense(circle)        
        # mechanism
        agent.time(activity)
        agent.update_memory(activity)
        agent.update_LTM()        
        
    catch = Stimuli(ini_pos, radius, [4], distance, space, speed)
    agent.inertia = 0
    for i in range(300):
        dt = 1 / 50
        activity = 0
        for circle in catch.stimuli:
            circle.fall(dt)
            activity += agent.sense(circle)       
        # mechanism
        agent.time(activity)
        agent.update_memory(activity)
        if agent.memory >= max(agent.LTM)  and agent.inertia >= 1:
            agent.forward(chase_sp, dt)
        
        # visualization
        x.append(i)
        y.append(activity)
        z.append(agent.x)

    plt.plot(x, y)
    plt.plot(x, z)

# subtraction
def subtraction(agent, test):
    x, y, z = [], [], []
    
    sense = Stimuli(ini_pos, radius, [1,3], distance, space, speed)
    for i in range(400): 
        dt = 1 / 50
        activity = 0
        for circle in sense.stimuli:
            circle.fall(dt)
            activity += agent.sense(circle)        
        # mechanism
        agent.time(activity)
        agent.update_memory(activity)
        agent.update_LTM()        
        
    catch = Stimuli(ini_pos, radius, [2], distance, space, speed)
    agent.inertia = 0
    for i in range(300):
        dt = 1 / 50
        activity = 0
        for circle in catch.stimuli:
            circle.fall(dt)
            activity += agent.sense(circle)       
        # mechanism
        agent.time(activity)
        agent.update_memory(activity)
        if agent.memory == (agent.LTM[1] - agent.LTM[0]) and agent.inertia >= 1:
            agent.forward(chase_sp, dt)
        
        # visualization
        x.append(i)
        y.append(activity)
        z.append(agent.x)

    plt.plot(x, y)
    plt.plot(x, z)


# Global parameters
test, chase_sp, ini_agent = 3, 150, (3, 0)
ini_pos = (0, 10)
radius, speed, distance, space = 1, 5, 5, 15

# Create agent
agent = Agent(*ini_agent)

# Call agent_behavior with agent
subtraction(agent, test)

# Display the plot
plt.show()
    
