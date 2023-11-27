import math
import random
import time
import matplotlib.pyplot as plt

def montyHall(total, pick, win, open, switch):

    #gets vector of picked doors
    picked = []
    for i in range(pick):
        check = True
        while check:
            randomPick = random.randint(1, total)
            if randomPick not in picked:
                picked.append(randomPick)
                check = False
    picked.sort()

    #gets vector of winner doors
    winners = []
    for i in range(win):
        check = True
        while check:
            randomPick = random.randint(1, total)
            if randomPick not in winners:
                winners.append(randomPick)
                check = False
    winners.sort()

    #gets vector of opened doors
    opened = []
    for i in range(open):
        check = True
        while check:
            randomPick = random.randint(1, total)
            if randomPick not in opened + picked + winners:
                opened.append(randomPick)
                check = False
    opened.sort()

    #switches if true
    if switch:
        for i in range(total + 1):
            if i in picked:
                picked.remove(i)
            elif i not in opened:
                picked.append(i)
        picked.sort()
    
    #decides winner or loser
    picked = set(picked)
    winners = set(winners)
    if len(picked.intersection(winners)) > 0:
        return 1
    else:
        return 0

def main():
    start = time.time()
    total = 3
    pick = 1
    win = 1
    open = 1
    runs = 1000
    simulationNoSwitch = 0
    simulationSwitch = 0
    switch = False
    probabilitiesNoSwitch = []
    probabilitiesSwitch = []
    for i in range(1, runs + 1):
        simulationNoSwitch += montyHall(total, pick, win, open, False)
        simulationSwitch += montyHall(total, pick, win, open, True)
        probabilitiesNoSwitch.append(simulationNoSwitch / i)
        probabilitiesSwitch.append(simulationSwitch / i)
    simulationNoSwitch = simulationNoSwitch / runs
    simulationSwitch = simulationSwitch / runs
    print("Simulation's probability with no switching: " + str(simulationNoSwitch))
    print("Simulation's probability with switching: " + str(simulationSwitch))
    trueNoSwitch = 1 - (math.factorial(total - win) * math.factorial(total - pick)) / (math.factorial(total) * math.factorial(total - win - pick))
    trueSwitch = 0
    print("True probability with no switching: " + str(trueNoSwitch))
    print("True probability with switching: " + str(trueSwitch))
    end = time.time()
    graph(probabilitiesNoSwitch, trueNoSwitch)
    graph(probabilitiesSwitch, trueSwitch)
    print("Time taken: " + str(end - start))

def graph(probabilities, trueValue):
    #takes probabilities vector and makes a graph of how probability changes over the simulations
    plt.plot(probabilities)
    plt.plot(trueValue)
    plt.ylabel('Probability')
    plt.xlabel('Simulations')
    ax = plt.gca()
    ax.set_ylim([0, 1])
    plt.show()

main()