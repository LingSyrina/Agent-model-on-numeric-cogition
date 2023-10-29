#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:21:01 2023

@author: leasyrin
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import sys
# import pathos

sys.path.append('/Users/leasyrin/Desktop/CTRNN')
import agent_stimuli_class as asc
import CTRNN_Ling as CTRNN
# from stochsearch import EvolSearch
import GA
          
# Task 1: Numerosity attention model: catch stimuli with numerosity one/ four  
def attention(genotype): 
    
    # Initialisation
    external_input = np.zeros(size)
    group = 1
    performance = 0
    
    # averaging through a group of agents
    for n in range(group):
        
        # Setting CTRNN agent and stimuli
        model = CTRNN.CTRNN(size, connections)
        model.receive_parameters(genotype, Wrange, Trange, Brange, Irange)
        agent = asc.Agent(*ini_agent)
        
        test_numerosity = random.randint(1, 3) if random.randint(0, 1) == 0 else 4
        sense = asc.Stimuli(ini_pos, radius, [test_numerosity], distance, space, speed)
        
        # catching stage        
        # visualization
        x, y, z, o = [], [], [], []        
        for i in range (300):
            external_input[0] = 0
            for circle in sense.stimuli:
                circle.fall(dt)
                external_input[0] += agent.sense(circle)  
                # external_input[0] += 0   
            model.update_ext(dt, external_input) 
            # model.update(dt)          
            agent.forward, agent.backward = model.outputs[3], 0.3
            agent.move()
            
            # visualization
            x.append(i)
            y.append(agent.x)
            # y.append(model.outputs[2])
            z.append(external_input[0])  
            o.append(model.outputs[1])
            # print(model.outputs)
        # visualization
        plt.plot(x, y)
        plt.plot(x, z) 
        # plt.plot(x, o) 
        # print(o)
         
        # evaluate performance
        if test_numerosity == 4:
            performance += (3 - abs(agent.x)) * 10/3
        else:        
            performance += agent.x * 10/3
            
        print(model.W, model.T, model.B, model.I, connections[1])
        # print(performance, agent.x, catch_numerosity, test_numerosity )
    performance /= group
        
    return performance 


# CTRNN parameters for task 1
Wrange = 15
Trange = [1,5]
Brange = 20
Irange = 10
size = 4
connections = [[0,0,0,0], [1,1,1,1], [1,1,1,1], [0,1,1,0]]
genotype = [1.0, 0.1769446829359531, 0.7959684434739188, -0.9748291983756711, 1.0, 1.0, 1.0, 1.0, 1.0, 0.15951948892146817, 0.4853213322363402, -0.6261728781681241, 0.9163094085847041, -0.20495644714324457, 0.6825172238502526, 0.885020798139199, 0.5567977346711089, -0.7600290995248266, 1.0, 0.2929440687091288, -0.02925772979481145, -1.0, -0.46278905045095897, -0.17847913520200626, 0.7200951660447612, -0.07198926116002308, 0.2529261914583789, 0.22742120209367778]
dt = 1 / 20   



                 
# Task 1: Habituation (input genotype, renders performance)
def habituation(genotype): 
    
    # Initialisation
    external_input = np.zeros(size)
    group = 1
    performance = 0
    
    # averaging through a group of agents
    for n in range(group):
        
        # Setting CTRNN agent and stimuli
        model = CTRNN.CTRNN(size, connections)
        model.receive_parameters(genotype, Wrange, Trange, Brange, Irange)
        agent = asc.Agent(*ini_agent)
        
        test_numerosity = [random.randint(1, 4) for _ in range(2)]
        sense = asc.Stimuli(ini_pos, radius, test_numerosity, distance, space, speed)
        catch_numerosity = random.randint(1, 4)
        catch = asc.Stimuli(ini_pos, radius, [catch_numerosity], distance, space, speed)
        
        # sensing stage
        for i in range (400):
            external_input[0] = 0
            for circle in sense.stimuli:
                circle.fall(dt)
                external_input[0] += agent.sense(circle)   
            model.update_ext(dt, external_input)
            print(model.outputs)
        # visualization
        x, y, z = [], [], []   
        
        # catching stage
        external_input[0] = 0
        for i in range (300):
            external_input[0] = 0
            for circle in catch.stimuli:
                circle.fall(dt)
                external_input[0] += agent.sense(circle)   
            model.update_ext(dt, external_input)                      
            agent.forward, agent.backward = model.outputs[3], model.outputs[4]
            agent.move()
            
            # print(model.outputs)
            # visualization
            x.append(i)
            y.append(agent.x)
            z.append(external_input[0])            
        # visualization
        plt.plot(x, y)
        plt.plot(x, z) 
         
        # evaluate performance
        if catch_numerosity in test_numerosity:
            performance += (3 - abs(agent.x)) * 10/3
        else:        
            performance += agent.x * 10/3
            
        # print(performance, agent.x, catch_numerosity, test_numerosity )
    performance /= group
        
    return performance
 
        
# Global parameters
ini_agent = (3, 0)
ini_pos = (0, 10)
radius, speed, distance, space = 1, 5, 5, 15

# CTRNN parameters for task 1
Wrange = 15
Trange = [1,5]
Brange = 20
Irange = 10
size = 4
connections = [[0,0,0,0], [1,1,1,1], [1,1,1,1], [0,1,1,0]]
genotype = [1.0, 0.1769446829359531, 0.7959684434739188, -0.9748291983756711, 1.0, 1.0, 1.0, 1.0, 1.0, 0.15951948892146817, 0.4853213322363402, -0.6261728781681241, 0.9163094085847041, -0.20495644714324457, 0.6825172238502526, 0.885020798139199, 0.5567977346711089, -0.7600290995248266, 1.0, 0.2929440687091288, -0.02925772979481145, -1.0, -0.46278905045095897, -0.17847913520200626, 0.7200951660447612, -0.07198926116002308, 0.2529261914583789, 0.22742120209367778]

dt = 1 / 20   
# W = genotype[0]
# τ = genotype[1]
# θ = genotype[2]
# I = genotype[3]

# GA parameters
perf = attention
pop = 20
genesize = size * ((size+3))
grt = 50
REC = 0.3
MUT = 0.1


run = GA.GA(pop,genesize)
run.run(perf,grt,REC,MUT)

# # Redirect stdout to a file
# output_file_path = "output.txt"
# sys.stdout = open(output_file_path, "w")

# # defining the parameters for the evolutionary search
# evol_params = {
#     # 'num_processes' : 40, # (optional) number of proccesses for multiprocessing.Pool
#     'pop_size' : 100,    # population size
#     'genotype_size': size * ((size+3)), # dimensionality of solution
#     'fitness_function': habituation, # custom function defined to evaluate fitness of a solution
#     'elitist_fraction': 0.04, # fraction of population retained as is between generations
#     'mutation_variance': 0.1, # mutation noise added to offspring.
# }                           

# # create evolutionary search object
# es = EvolSearch(evol_params)

# # keep searching till a stopping condition is reached
# best_fit = []
# mean_fit = []
# num_gen = 0
# max_num_gens = 100
# desired_fitness = 0.95
# while es.get_best_individual_fitness() < desired_fitness and num_gen < max_num_gens:
# # while num_gen < max_num_gens:
#     print('Gen #'+str(num_gen)+' Best Fitness = '+str(es.get_best_individual_fitness()))
#     es.step_generation()
#     best_fit.append(es.get_best_individual_fitness())
#     mean_fit.append(es.get_mean_fitness())
#     num_gen += 1

# # print results
# print('Max fitness of population = ',es.get_best_individual_fitness())
# print('Best individual in population = ',es.get_best_individual())

# # plot results
# plt.figure()
# plt.plot(best_fit)
# plt.plot(mean_fit)
# plt.xlabel('Generations')
# plt.ylabel('Fitness')
# plt.legend(['best fitness', 'avg. fitness'])
# plt.show()

# Close the output file
sys.stdout.close()

# Restore stdout to the console
sys.stdout = sys.__stdout__ 