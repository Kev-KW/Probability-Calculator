# This simulation disregards any other stats rolled. Therefore, any "Good" stats besides crit roll will be ignored/undo'd
import Calculator

itemName = "Wooden Stick"

totalCost = 0
totalRuns = 10

desiredCritChance = 25
undoThreshHold = 10
modifierThreshold = 10

for i in range(0,totalRuns):
    print(f"Trial {i}\n-----------------------------------")
    resultCost = Calculator.calculate(desiredCritChance, undoThreshHold, modifierThreshold)
    totalCost += resultCost

print(f"The average to obtain {desiredCritChance}cc with a sample size of {totalRuns} is {totalCost/totalRuns/1000}p")