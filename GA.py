#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

class GA():
    def __init__(self,pop,genesize):
        self.pop = pop
        self.gene = np.random.random((self.pop,genesize))
        self.size = genesize 
   
    def MBG (self,perf,bestp,best,REC,MUT): # microbial search: compare two elements, mutate the loser
        
        # find two indexes
        dem = self.pop/2
        a = int(self.pop * np.random.uniform(0,1))
        b = (a + 1 + int(dem * np.random.uniform(0,1))) % self.pop
        
        # compare
        perf1 = perf(self.gene[a])
        perf2 = perf(self.gene[b])
        if perf1 > perf2: 
            w=a
            l=b
            p = perf1
        else:
            w=b
            l=a
            p = perf2
        
        # print the best agent so far
        if p > bestp:
            bestp = p
            best = self.gene[w]
            besty = best.tolist() 
            print('The best agent',bestp,besty)

        # crossover and mutate
        for j in range (self.size):
            if REC > np.random.uniform(0,1): 
                self.gene[l,j]= self.gene[w,j]
            if MUT > np.random.uniform(0,1): 
                self.gene[l,j] += np.random.normal(0,1)
        for i in range(self.size):
            self.gene[:,i] = np.clip(self.gene[:,i],-1,1)
        return self, bestp, best

    def run (self,perf,grt,REC,MUT): # Simulation: initialisation, each generation do MBG n times   
        best_p = np.zeros(grt)
        best_w = np.zeros((grt,self.size))
        bestp = 0
        best = np.zeros(self.size)
        for n in range(grt): 
            for i in range(int(pop)): 
                gp, bestp, best = self.MBG(perf,bestp,best,REC,MUT)
            best_p[n] = bestp
            best_w[n] = best
        x = np.arange(0,grt,1)
        plt.plot(x,best_p)
        plt.show()
        return best_p,best_w

# Sample run

# def fitness(genotype):
#     return np.mean(genotype)

# # parameters    
# perf = fitness
# pop = 10
# genesize = 2
# grt = 6
# REC = 0.3
# MUT = 0.1

# run = GA(pop,genesize)
# run.run(perf,grt,REC,MUT)   

