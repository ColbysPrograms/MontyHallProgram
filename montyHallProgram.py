import math
import random
import time

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
        for i in range(total):
            if i in picked:
                picked.remove(i)
            elif i not in opened:
                picked.append(i)
        picked.sort()
    
    #decides winner or loser
    picked = set(picked)
    winners = set(winners)
    if picked.intersection(winners):
        return 1
    else:
        return 0

def main():
    start = time.time()
    total = 80
    pick = 1
    win = 5
    open = 9
    runs = 100000
    totalWinsNoSwitch = 0
    totalWinsSwitch = 0
    switch = False
    for i in range(runs):
        totalWinsNoSwitch += montyHall(total, pick, win, open, False)
        totalWinsSwitch += montyHall(total, pick, win, open, True)
    resultNoSwitch = totalWinsNoSwitch / runs
    resultSwitch = totalWinsSwitch / runs
    print("Result without switching: " + str(resultNoSwitch))
    print("Result with switching: " + str(resultSwitch))
    end = time.time()
    print(end - start)

main()