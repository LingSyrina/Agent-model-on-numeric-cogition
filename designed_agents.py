
import math
import matplotlib.pyplot as plt

# Global parameters
test = 3
chase_sp = 150
ini_agent, ini_circle, r, speed, number, distance = (3,0),(0,10),1,5, 3, 5
# agent(ini_agent, ini_circle, r, speed, number, distance)

def sense(pos_agent, pos_circle, r):
    
    # Agent's position & Circle's position
    agent_x, agent_y = pos_agent
    circle_x, circle_y = pos_circle
    
    # Sensor's field of view angle in degrees
    sensor_fov = 60 * (math.pi / 180)
    
    # Calculate the horizental distance d
    d = abs(agent_x - circle_x)
    c = math.atan(sensor_fov) *  d
    
    # Check if the circle is within the sensor's range
    if c - r/math.cos(sensor_fov) <= circle_y <= c + r/math.cos(sensor_fov):
        deviation = (circle_y - c)/(r/math.cos(sensor_fov)) * math.pi/2
        activity = math.cos(deviation) * 2 * r  # approximation of the activation (smoothed function based on the overlap size)
    else:
        activity = 0 
    return (activity)

def fall(speed, dt, ini_x, ini_y): 
    return (ini_x, ini_y - dt * speed) if ini_y - dt * speed >= 0 else (-100,-100)

# habituation agent: inertia and activation required (two memory system)
def agent(ini_agent, ini_circle, r, speed, number, distance):
    
    ini_x, ini_y = ini_circle
    agent_x, agent_y = ini_agent
    
    # this is the sensing stage
    memory = 0
    for i in range(200):
        dt = i/50
        activity = 0
        for n in range(number):
            pos_circle = fall(speed, dt, ini_x, ini_y + n * distance)
            activity += sense(ini_agent, pos_circle, r)
        memory += (1 if activity > 0 else 0)
    
    # this is the catching stage: catch it if the number is the same
    x, y, z = [], [], []
    inertia = 0
    for i in range(250): 
        dt = i/50
        activity = 0
        for n in range(test):
            pos_circle = fall(speed, dt, ini_x, ini_y + n * distance)
            activity += sense((agent_x, agent_y), pos_circle, r)
        if activity > 0:
            memory -= 1
            inertia = 0
        else: 
            inertia += 0.1
        if memory == 0 and inertia >= 1 and agent_x > 0 : 
            agent_x -= chase_sp * 1/50
        if memory < 0 and inertia < 1 and agent_x < 3: 
            agent_x += chase_sp * 1/50 
        x.append(dt)
        y.append(activity)
        z.append(agent_x)       
    
    plt.plot(x, y)
    plt.plot(x,z)
    
