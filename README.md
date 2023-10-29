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
   ![image](https://github.com/LingSyrina/Agent-model-on-numeric-cogition/assets/91287479/883ce17a-dccc-42c6-a59e-5da468b9c161)
   ![image](https://github.com/LingSyrina/Agent-model-on-numeric-cogition/assets/91287479/59c255ef-0a4f-4a1d-98f6-5d29f03ea6e9)
   ![image](https://github.com/LingSyrina/Agent-model-on-numeric-cogition/assets/91287479/3b45d706-3507-4b42-8d7a-d657bb4ef6af)
   ![image](https://github.com/LingSyrina/Agent-model-on-numeric-cogition/assets/91287479/89ba1c6b-8d92-4e0f-aa97-1dc703817c61)

   The best agent 9.874825714494465

``` 
genotype = [1.0, 0.1769446829359531, 0.7959684434739188, -0.9748291983756711, 1.0, 1.0, 1.0, 1.0, 1.0, 0.15951948892146817, 0.4853213322363402, -0.6261728781681241, 0.9163094085847041, -0.20495644714324457, 0.6825172238502526, 0.885020798139199, 0.5567977346711089, -0.7600290995248266, 1.0, 0.2929440687091288, -0.02925772979481145, -1.0, -0.46278905045095897, -0.17847913520200626, 0.7200951660447612, -0.07198926116002308, 0.2529261914583789, 0.22742120209367778]

# CTRNN parameters
Wrange = 15
Trange = [1,5]
Brange = 20
Irange = 10
size = 4
connections = [[0,0,0,0], [1,1,1,1], [1,1,1,1], [0,1,1,0]]
dt = 1 / 20
```  

3. Numerosity attention model: catch stimuli with numerosity two/ three

4. Habituation model: Catch stimuli with the same numerosity (1 stimuli group per phase)

5. Habituation model: Catch stimuli with the familiar numerosity (2 + 1 stimuli group)

6. Comparison model: 1 + 1 design

7. Comparison model: 2 + 1 design

8. Subtraction model: 2 + 1 design
