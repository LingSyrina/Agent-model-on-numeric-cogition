import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

class CTRNN():
    '''CTRNN has a number of SENSOR, MOTOR, INTER neurons, 
    each neuron has parameters (weights, time constants, biases, inputs),
    (1) initial states are defined in init;
    (2) states are updated in update;
    (3) parameters are passed from GA to update'''
    
    def __init__(self,size,Connections):
        
        # morphology of this CTRNN
        self.size = size
        self.connections = Connections # the neurons connected to neuron_i: 1 for connected, 0 for not 
        
        # Parameters of this CTRNN: default fully connected
        self.W = np.random.random(size=(self.size**2))
        self.T = np.random.random(size=(self.size))
        self.B = np.random.random(size=(self.size))
        self.I = np.random.random(size=(self.size))
        
        # Initial State of CTRNN
        self.inputs = np.zeros(self.size)
        self.outputs = np.zeros(self.size)
    
    def receive_parameters(self,Parameters,Wrange,Trange,Brange,Irange): # receive weights from GA (set range)       
        W = self.size**2
        self.W = np.dot(Parameters[0:W],Wrange) 
        self.T = abs(np.dot(Parameters[W:W+self.size],Trange[1]))+Trange[0]
        self.B = np.dot(Parameters[W+self.size:W+self.size*2],Brange) 
        self.I = np.dot(Parameters[W+self.size*2:W+self.size*3],Irange)   
    
    def get_outputs(self): # calculate the initial outputs        
        for i in range(self.size):
            self.outputs[i] = sigmoid(self.inputs[i] + self.B[i])
            
    def get_weights(self,index): # set weights for each neuron        
        total_con = len(self.connections[0])       
        W = self.W[index*total_con:index*total_con + total_con]       
        return W
       
    def get_state(self,index,dt): # calculate the states for each neuron for each dt
        W = self.get_weights(index)  
        weighed_inputs = 0
        for i in range(self.size):
            weighed_inputs += W[i] * self.outputs[i] * self.connections[index][i]        
        delta = (1/self.T[index]) * (-self.inputs[index] + weighed_inputs + self.I[index])
        self.inputs[index] +=  delta * dt
    
    def get_state_ext (self,index,dt,external_input): # calculate the states for each neuron for each dt
        W = self.get_weights(index)  
        weighed_inputs = 0
        for i in range(self.size):
            weighed_inputs += W[i] * self.outputs[i] * self.connections[index][i]        
        delta = (1/self.T[index]) * (-self.inputs[index] + weighed_inputs + self.I[index]* external_input[index])
        self.inputs[index] +=  delta * dt
    
    def update (self,dt): # update all neurons per dt  
        for i in range(self.size):
            # update its current state
            self.get_state(i,dt)
            #  update its output
            self.outputs[i] = sigmoid(self.inputs[i] + self.B[i])
            
    def update_ext (self,dt,external_input): # update all neurons per dt  
        for i in range(self.size):
            # update its current state
            self.get_state_ext(i,dt,external_input)
            #  update its output
            self.outputs[i] = sigmoid(self.inputs[i] + self.B[i])

# sample CTRNN: oscillator
# dt = 0.1
# time = np.arange(0,50,dt)
# o1 = np.zeros((len(time)))
# o2 = np.zeros((len(time)))
# i = 0

# a = CTRNN(2,[[1,1],[1,1]])
# a.receive_parameters([4.5, 1, -1, 4.5,1,1,-2.75,-1.75,0,0],1,[1,0],1,1)
# for t in time:
#     a.update(dt)
#     o1[i] = a.outputs[0]
#     o2[i] = a.outputs[1]
#     i +=1
    
# plt.plot(time,o1)
# plt.plot(time,o2)
