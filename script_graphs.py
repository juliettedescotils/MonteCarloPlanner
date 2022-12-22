# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:29:52 2022

@author: Juliette & Bastien
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#on lit le fichier csv
data = pd.read_csv('results.csv', on_bad_lines='skip')
data


#on crée un vecteur pour chaque courbeà tracer
times_MRW_blocks=[]
steps_MRW_blocks=[]
times_HSP_blocks=[]
steps_HSP_blocks=[]
blocksProblems=[]
times_MRW_logistics=[]
steps_MRW_logistics=[]
times_HSP_logistics=[]
steps_HSP_logistics=[]
logisticsProblems=[]
times_MRW_depots=[]
steps_MRW_depots=[]
times_HSP_depots=[]
steps_HSP_depots=[]
depotsProblems=[]
times_MRW_gripper=[]
steps_MRW_gripper=[]
times_HSP_gripper=[]
steps_HSP_gripper=[]
gripperProblems=[]

#on ajoute les valeurs dans chaque vecteur
for i in data.index:
    if data.domain[i] == 'blocks':
        times_MRW_blocks.append(data.MRW_time_spent[i])
        steps_MRW_blocks.append(data.MRW_plan_length[i])
        times_HSP_blocks.append(data.HSP_time_spent[i])
        steps_HSP_blocks.append(data.HSP_plan_length[i])
        blocksProblems.append(str(data.n_problem[i]))
    if data.domain[i] == 'logistics':
        times_MRW_logistics.append(data.MRW_time_spent[i])
        steps_MRW_logistics.append(data.MRW_plan_length[i])
        times_HSP_logistics.append(data.HSP_time_spent[i])
        steps_HSP_logistics.append(data.HSP_plan_length[i])
        logisticsProblems.append(str(data.n_problem[i]))
    if data.domain[i] == 'depots':
        times_MRW_depots.append(data.MRW_time_spent[i])
        steps_MRW_depots.append(data.MRW_plan_length[i])
        times_HSP_depots.append(data.HSP_time_spent[i])
        steps_HSP_depots.append(data.HSP_plan_length[i])
        depotsProblems.append(str(data.n_problem[i]))
    if data.domain[i] == 'gripper':
        times_MRW_gripper.append(data.MRW_time_spent[i])
        steps_MRW_gripper.append(data.MRW_plan_length[i])
        times_HSP_gripper.append(data.HSP_time_spent[i])
        steps_HSP_gripper.append(data.HSP_plan_length[i])
        gripperProblems.append(str(data.n_problem[i]))








#On génère les 8 graphiques en triant les vecteur pour que la performance du planner HSP soit croissante
sortedTimesBlocks=sorted(zip(times_HSP_blocks, times_MRW_blocks, blocksProblems))
times_HSP_blocks = [x for x,_,_ in sortedTimesBlocks]
times_MRW_blocks = [x for _,x,_ in sortedTimesBlocks]
blocksProblems = [x for _,_,x in sortedTimesBlocks]
plt.figure(1)
pltTimes = plt.xlabel("Problem number"), plt.ylabel("Resolution time"), plt.title("Resolution time of MRW and HSP planners in blocksworld")
pltTimes = plt.plot(blocksProblems, times_MRW_blocks, label = "MRW"), plt.plot(blocksProblems, times_HSP_blocks, label = "HSP"), plt.legend()
plt.savefig("graphRuntimeBlocks.png") #on enregistre l'image

sortedStepsBlocks = sorted(zip(steps_HSP_blocks, steps_MRW_blocks, blocksProblems))
steps_HSP_blocks = [x for x,_,_ in sortedStepsBlocks]
steps_MRW_blocks = [x for _,x,_ in sortedStepsBlocks]
blocksProblems = [x for _,_,x in sortedStepsBlocks]
plt.figure(2)
pltSteps = plt.xlabel("Problem number"), plt.ylabel("Number of steps to resolve"), plt.title("Number of steps needed by MRW and HSP planners to resolve problem in blocksworld")
pltSteps = plt.plot(blocksProblems, steps_MRW_blocks, label = "MRW"), plt.plot(blocksProblems, steps_HSP_blocks, label = "HSP"), plt.legend()
plt.savefig("graphNumberOfStepsBlocks.png") #on enregistre l'image




sortedTimesLogistics=sorted(zip(times_HSP_logistics, times_MRW_logistics, logisticsProblems))
times_HSP_logistics = [x for x,_,_ in sortedTimesLogistics]
times_MRW_logistics = [x for _,x,_ in sortedTimesLogistics]
logisticsProblems = [x for _,_,x in sortedTimesLogistics]
plt.figure(3)
pltTimes = plt.xlabel("Problem number"), plt.ylabel("Resolution time"), plt.title("Resolution time of MRW and HSP planners in logistics")
pltTimes = plt.plot(logisticsProblems, times_MRW_logistics, label = "MRW"), plt.plot(logisticsProblems, times_HSP_logistics, label = "HSP"), plt.legend()
plt.savefig("graphRuntimeLogistics.png") 

sortedStepsLogistics = sorted(zip(steps_HSP_logistics, steps_MRW_logistics, logisticsProblems))
steps_HSP_logistics = [x for x,_,_ in sortedStepsLogistics]
steps_MRW_logistics = [x for _,x,_ in sortedStepsLogistics]
logisticsProblems = [x for _,_,x in sortedStepsLogistics]
plt.figure(4)
pltSteps = plt.xlabel("Problem number"), plt.ylabel("Number of steps to resolve"), plt.title("Number of steps needed by MRW and HSP planners to resolve problem with logistics")
pltSteps = plt.plot(logisticsProblems, steps_MRW_logistics, label = "MRW"), plt.plot(logisticsProblems, steps_HSP_logistics, label = "HSP"), plt.legend()
plt.savefig("graphNumberOfStepsLogistics.png") 



sortedTimesDepots=sorted(zip(times_HSP_depots, times_MRW_depots, depotsProblems))
times_HSP_depots = [x for x,_,_ in sortedTimesDepots]
times_MRW_depots = [x for _,x,_ in sortedTimesDepots]
depotsProblems = [x for _,_,x in sortedTimesDepots]
plt.figure(5)
pltTimes = plt.xlabel("Problem number"), plt.ylabel("Resolution time"), plt.title("Resolution time of MRW and HSP planners in depots")
pltTimes = plt.plot(depotsProblems, times_MRW_depots, label = "MRW"), plt.plot(depotsProblems, times_HSP_depots, label = "HSP"), plt.legend()
plt.savefig("graphRuntimeDepots.png")

sortedStepsDepots = sorted(zip(steps_HSP_depots, steps_MRW_depots, depotsProblems))
steps_HSP_depots = [x for x,_,_ in sortedStepsDepots]
steps_MRW_depots = [x for _,x,_ in sortedStepsDepots]
depotsProblems = [x for _,_,x in sortedStepsDepots]
plt.figure(6)
pltSteps = plt.xlabel("Problem number"), plt.ylabel("Number of steps to resolve"), plt.title("Number of steps needed by MRW and HSP planners to resolve problem with depots")
pltSteps = plt.plot(depotsProblems, steps_MRW_depots, label = "MRW"), plt.plot(depotsProblems, steps_HSP_depots, label = "HSP"), plt.legend()
plt.savefig("graphNumberOfStepsDepots.png") 



sortedTimesGripper=sorted(zip(times_HSP_gripper, times_MRW_gripper, gripperProblems))
times_HSP_gripper = [x for x,_,_ in sortedTimesGripper]
times_MRW_gripper = [x for _,x,_ in sortedTimesGripper]
gripperProblems = [x for _,_,x in sortedTimesGripper]
plt.figure(7)
pltTimes = plt.xlabel("Problem number"), plt.ylabel("Resolution time"), plt.title("Resolution time of MRW and HSP planners in gripper")
pltTimes = plt.plot(gripperProblems, times_MRW_gripper, label = "MRW"), plt.plot(gripperProblems, times_HSP_gripper, label = "HSP"), plt.legend()
plt.savefig("graphRuntimeGripper.png") 


sortedStepsGripper = sorted(zip(steps_HSP_gripper, steps_MRW_gripper, gripperProblems))
steps_HSP_gripper = [x for x,_,_ in sortedStepsGripper]
steps_MRW_gripper = [x for _,x,_ in sortedStepsGripper]
gripperProblems = [x for _,_,x in sortedStepsGripper]
plt.figure(8)
pltSteps = plt.xlabel("Problem number"), plt.ylabel("Number of steps to resolve"), plt.title("Number of steps needed by MRW and HSP planners to resolve problem with gripper")
pltSteps = plt.plot(gripperProblems, steps_MRW_gripper, label = "MRW"), plt.plot(gripperProblems, steps_HSP_logistics, label = "HSP"), plt.legend()
plt.savefig("graphNumberOfStepsGripper.png") 




