# Agent-model-on-numeric-cogition

## General functions
1. Genetic algorithm (GA.py)
2. CTRNN model (CTRNN.py)
3. Agent and stimuli (agent_stimuli_classes.py)

## Parameters
1. Task parameter: between-circle distance, between-stimuli distance, stimuli radius, stimuli speed, agent speed
2. CTRNN parameter: connection weight, bias, time step, size
3. GA parameter: population, mutation rate, ellite proportion, generation
4. Evaluation: performance score

## Task breakdown
1. Numerosity attention model: catch stimuli with numerosity one/ four (week 8-?)
   ### catching four only:

  ```
# Task 1: Numerosity attention model: catch stimuli with numerosity four  
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
        for i in range (500):
            external_input[0] = 0
            for circle in sense.stimuli:
                circle.fall(dt)
                external_input[0] += agent.sense(circle)  
            model.update_ext(dt, external_input)          
            agent.forward, agent.backward = model.outputs[3], 0.2
            agent.move()
         
        # evaluate performance
        if test_numerosity == 4:
            performance += (3 - abs(agent.x)) * 10/3
        else:        
            performance += agent.x * 10/3
    performance /= group
        
    return performance 
```
```
# CTRNN parameters
Wrange = 15
Trange = [1,5]
Brange = 20
Irange = 10
size = 4
connections = [[0,0,0,0], [1,1,1,1], [1,1,1,1], [0,1,1,0]]
dt = 1 / 20
```
   ![image](https://github.com/LingSyrina/Agent-model-on-numeric-cogition/assets/91287479/a23f33e5-bc83-444e-935c-e007f4120378)
   ![image](https://github.com/LingSyrina/Agent-model-on-numeric-cogition/assets/91287479/0056f0e0-4659-42e2-8aa0-134330eba90b)
   ![image](https://github.com/LingSyrina/Agent-model-on-numeric-cogition/assets/91287479/cc6b2b01-6734-409a-bac1-d2a14b5f2ed3)
   ![image](https://github.com/LingSyrina/Agent-model-on-numeric-cogition/assets/91287479/c63c4525-90f3-4598-a679-52f59acb1a38)

   The best agent 9.942863389521605

``` 
genotype = [1.0, 0.1769446829359531, 0.7959684434739188, -0.9748291983756711, 1.0, 1.0, 1.0, 1.0, 1.0, 0.15951948892146817, 0.4853213322363402, -0.6261728781681241, 0.9163094085847041, -0.20495644714324457, 0.6825172238502526, 0.885020798139199, 0.5567977346711089, -0.7600290995248266, 1.0, 0.2929440687091288, -0.02925772979481145, -1.0, -0.46278905045095897, -0.17847913520200626, 0.7200951660447612, -0.07198926116002308, 0.2529261914583789, 0.22742120209367778]
```

![image](https://github.com/LingSyrina/Agent-model-on-numeric-cogition/assets/91287479/99e96018-5317-40df-aa6e-c5527ef19ec2)
![image](https://github.com/LingSyrina/Agent-model-on-numeric-cogition/assets/91287479/68be4f56-edbc-4f16-b9b7-6f7ab2fee6b6)
![image](https://github.com/LingSyrina/Agent-model-on-numeric-cogition/assets/91287479/927fd9b5-d5a5-4ef9-9486-8cc0555e90f3)
![image](https://github.com/LingSyrina/Agent-model-on-numeric-cogition/assets/91287479/b35faee3-678c-42c2-8bc5-9e27dc4c3b39)

   A different agent: 9.70790337272025 (cannot be generalized)
``` 
genotype = [-1.0, -0.028922415577894434, -1.0, 1.0, 1.0, 0.08552476586533511, -0.5876591805766169, 1.0, -0.010146998132529783, -0.25171376566166875, 0.35141624323987364, -1.0, -0.2630219669573748, -1.0, -0.9460212234343062, 0.008287068448029941, 0.1506312010190205, 1.0, 0.6587592310987282, 1.0, 0.11647697513138666, -1.0, -1.0, 0.3400064283499096, -0.8875480537976772, -0.89308206045686, 1.0, 1.0]
```

3. Numerosity attention model: catch stimuli with numerosity two/ three

4. Habituation model: Catch stimuli with the same numerosity (1 stimuli group per phase)

5. Habituation model: Catch stimuli with the familiar numerosity (2 + 1 stimuli group)

6. Comparison model: 1 + 1 design

7. Comparison model: 2 + 1 design

8. Subtraction model: 2 + 1 design
