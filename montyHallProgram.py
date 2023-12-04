import math
from math import comb
from math import factorial
import random
import time
import matplotlib.pyplot as plt

def montyHall(total, pick, win, open, switch, atLeastOne):

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
    if atLeastOne:
        if len(picked.intersection(winners)) > 0:
            return 1
        else:
            return 0
    else:
        winnerCounter = len(picked.intersection(winners))
        return winnerCounter

def main():
    start = time.time()
    total = 20
    pick = 7
    win = 4
    open = 3
    switch = total - pick - open
    runs = 100000
    simulationNoSwitch = 0
    simulationSwitch = 0
    simulationNoSwitchAtLeastOne = 0
    simulationSwitchAtLeastOne = 0
    probabilitiesNoSwitch = []
    probabilitiesSwitch = []
    probabilityNoSwitchAtLeastOne = []
    probabilitySwitchAtLeastOne = []
    for i in range(1, runs + 1):
        simulationNoSwitch += montyHall(total, pick, win, open, False, False)
        simulationSwitch += montyHall(total, pick, win, open, True, False)
        probabilitiesNoSwitch.append(simulationNoSwitch / i / pick)
        probabilitiesSwitch.append(simulationSwitch / i / switch)
        simulationNoSwitchAtLeastOne += montyHall(total, pick, win, open, False, True)
        simulationSwitchAtLeastOne += montyHall(total, pick, win, open, True, True)
        probabilityNoSwitchAtLeastOne.append(simulationNoSwitchAtLeastOne / i)
        probabilitySwitchAtLeastOne.append(simulationSwitchAtLeastOne - 0.06 / i)


    #For at least one probability
    simulationNoSwitchAtLeastOne = simulationNoSwitchAtLeastOne / runs
    simulationSwitchAtLeastOne = simulationSwitchAtLeastOne / runs
    #For normal probablility
    simulationNoSwitch = simulationNoSwitch / pick / runs
    simulationSwitch = simulationSwitch / switch / runs
    print("Simulation's probability with no switching: " + str(simulationNoSwitch))
    print("Simulation's probability with switching: " + str(simulationSwitch))
    trueNoSwitch = win / total
    trueSwitch = ((total-pick)/total)*(win/(total-pick-open))
    print("True probability with no switching: " + str(trueNoSwitch))
    print("True probability with switching: " + str(trueSwitch))
    trueNoSwitchAtLeastOne = 1 - factorial(total - pick) / factorial(total - win - pick) * factorial(total - win) / factorial(total)

    #switch formula
    switchSum = 0
    switchSum = 0
    switchProduct = 0
    for i in range(pick):
        switchProduct = comb(pick, i)
        #times
        switchProduct *= factorial(total - pick) / factorial(total)
        #times
        totalWinJ = total - win
        for j in range(1, pick - i):
            totalWinJ *= (total - win - j)
        switchProduct *= totalWinJ
        #times
        winJ = win
        for j in range(1, i):
            winJ *= (win - j)
        switchProduct *= winJ
        #times
        swij = (switch - win + i) / (switch)
        for j in range(1, pick):
            swij *= (switch - win + i - j) / (switch - j)
        switchProduct *= swij
        switchSum += switchProduct
    trueSwitchAtLeastOne = 1 - switchSum


    print("\n")
    print("Simulation's probability with no switching and at least one door winning " + str(simulationNoSwitchAtLeastOne))
    print("Simulation's probability with switching and at least one door winning " + str(simulationSwitchAtLeastOne))
    print("True probability with no switching and at least one door winning " + str(trueNoSwitchAtLeastOne))
    print("True probability with switching and at least one door winning " + str(trueSwitchAtLeastOne))
    end = time.time()
    graph(probabilitiesNoSwitch, trueNoSwitch, runs, "Probability when Not Switching")
    graph(probabilitiesSwitch, trueSwitch, runs, "Probability when Switching")
    graph(probabilityNoSwitchAtLeastOne, trueNoSwitchAtLeastOne, runs, "Probability when Not Switching of at Least One Door Winning")
    graph(probabilitySwitchAtLeastOne, trueSwitchAtLeastOne, runs, "Probability when Switching of at Least One Door Winning")
    print("Time taken: " + str(end - start))

def graph(probabilities, trueValue, simulations, title):
    #takes probabilities vector and makes a graph of how probability changes over the simulations
    x = []
    trueValueVector = []
    for i in range(1, simulations + 1):
        x.append(i)
        trueValueVector.append(trueValue)
    plt.plot(x, probabilities)
    plt.plot(x, trueValueVector)
    plt.title(title)
    plt.ylabel('Probability')
    plt.xlabel('Simulations')
    ax = plt.gca()
    ax.set_ylim([0, 1])
    plt.show()

main()