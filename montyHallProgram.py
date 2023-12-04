import math
from math import comb
from math import factorial
import random
import time
#import matplotlib.pyplot as plt

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
    probabilitiesNoSwitch = []
    probabilitiesSwitch = []
    for i in range(1, runs + 1):
        simulationNoSwitch += montyHall(total, pick, win, open, False)
        simulationSwitch += montyHall(total, pick, win, open, True)
        probabilitiesNoSwitch.append(simulationNoSwitch / i)
        probabilitiesSwitch.append(simulationSwitch / i)
    #For normal probablility
    simulationNoSwitch = simulationNoSwitch / runs / pick
    simulationSwitch = simulationSwitch / runs / switch
    #For at least one probability
    simulationNoSwitchAtLeastOne = simulationNoSwitch / runs
    simulationSwitchAtLeastOne = simulationSwitch / runs
    print("Simulation's probability with no switching: " + str(simulationNoSwitch))
    print("Simulation's probability with switching: " + str(simulationSwitch))
    trueNoSwitch = win / total
    trueSwitch = ((total-pick)/total)*(win/(total-pick-open))
    #switch formula
    switchSum = 0
    switchProduct = 0



    # for i in range(pick):
    #     switchProduct = comb(pick, i)
    #     #times
    #     switchProduct *= factorial(total - pick) / factorial(total)
    #     #times
    #     for j in range(pick - i - 1):
    #         if j == 0:
    #             totalWinJ = total - win
    #         else:
    #             totalWinJ *= (total - win - j)
    #     switchProduct *= totalWinJ
    #     #times
    #     for j in range(i - 1):
    #         if j == 0:
    #             winJ = win
    #         else:
    #             winJ *= (win - j)
    #     switchProduct *= winJ
    #     #times
    #     for j in range(pick - 1):
    #         if j == 0:
    #             swij = (switch - win + i - j) / (switch - j)
    #         else:
    #             swij *= (switch - win + i - j) / (switch - j)
    #     switchProduct *= swij
    #     switchSum += switchProduct
    # trueSwitch = 1 - switchSum


    print("True probability with no switching: " + str(trueNoSwitch))
    print("True probability with switching: " + str(trueSwitch))
    end = time.time()
    #graph(probabilitiesNoSwitch, trueNoSwitch, runs)
    #graph(probabilitiesSwitch, trueSwitch, runs)
    print("Time taken: " + str(end - start))

# def graph(probabilities, trueValue, simulations):
#     #takes probabilities vector and makes a graph of how probability changes over the simulations
#     x = []
#     trueValueVector = []
#     for i in range(1, simulations + 1):
#         x.append(i)
#         trueValueVector.append(trueValue)
#     plt.plot(x, probabilities)
#     plt.plot(x, trueValueVector)
#     plt.ylabel('Probability')
#     plt.xlabel('Simulations')
#     ax = plt.gca()
#     ax.set_ylim([0, 1])
#     plt.show()

main()