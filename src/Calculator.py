import random

# Change Values in adjustment to current economy
# Values are weighed in Gold
itemCost = 15
scrollCost = .5
undoCost = 100
holyCost = 5
resetCost = 2
lModCost = 50

# DO NOT CHANGE
globalItemRolls = 0
currentRollSlot = 0
failedRollSlot = 6
itemRolls = [0,0,0,0,0,0,0]

critRoll = False
BLEWW = False
modThreshholdBool = False

# What crit percentage before the use of undos (Ensures you don't spam undos on a 5cc item bruh)

# Critical Chance desired, Undo scroll threshhold, and Lmod threshhold
def calculate(critDesired, undoThreshHold, modifierThreshold):
    
    """
    Simulates rolling items until the desired critical chance is achieved.

    Parameters:
        critDesired (int): Target critical chance percentage to reach.
        undoThreshold (int): Threshhold before undo is used
        LmodThreshold (int): Threshold before Lmod is used
    Returns:
        list: The itemRolls array plus total cost at the end.
    """
    # DO NOT CHANGE
    global itemCount, scrollCount, undoCount, holyCount, resetCount, lModCount
    global critAmount, currentRollSlot, failedRollSlot, itemRolls
    global critRoll, BLEWW, modThreshholdBool, failDestroy, failBlow
    global globalItemRolls, checkerCrit
    itemCount = 0
    scrollCount = 0
    undoCount = 0
    holyCount = 0
    resetCount = 0
    lModCount = 0
    critAmount = 0

    currentRollSlot = 0
    failedRollSlot = 6
    itemRolls = [0,0,0,0,0,0,0]
    critRoll = False
    BLEWW = False
    modThreshholdBool = False
    checkerCrit = 0

    failDestroy = 20
    failBlow = 40

    while True: 
        
        # Reset iteration variables
        currentRollSlot = 0
        failedRollSlot = 6
        critAmount = 0
        checkerCrit = 0
        itemRolls = [0,0,0,0,0,0,0]
        critRoll = False
        BLEWW = False 
        modThreshholdBool = False
        failDestroy = 20
        failBlow = 40
        
        while True:
            # Dynamically track critRoll
            if not critRoll:
                critRoll = checkerCrit > 0
            
            if not modThreshholdBool:
                if checkerCrit >= modifierThreshold:
                    failBlow /= 2
                    failDestroy /= 2
                    lModCount += 1
                    modThreshholdBool = True
            
            successRoll = random.randint(1,100)
            scrollCount += 1
            
            
            
            # EXPLOSION
            if successRoll <= failDestroy:
                BLEWW = True
                itemCount += 1
                break
            
            # Failed roll
            elif successRoll <= failBlow:
                if critRoll: 
                    # No slots remaining, checks to see whether using a holy is worth it
                    if currentRollSlot == failedRollSlot:
                        
                        if currentRollSlot == 6:
                            if checkerCrit >= (critDesired - 10): # MUST BE WITHIN 10 CC TO BE SALVAGABLE
                                holyCount += 1
                                if failedRollSlot != 6:
                                    failedRollSlot += 1
                            else: 
                                BLEWW = True
                                break
                            
                        holyCount += 1
                        if failedRollSlot != 6:
                            failedRollSlot += 1
                            
                    else: 
                        failedRollSlot -= 1
                        
                elif failedRollSlot == 0:
                    BLEWW = True
                    resetCount += 1
                    break
                
                else:
                    failedRollSlot -= 1
                continue
                
            # Successful CC roll
            else:
                firstRoll = critCreation(random.randint(0,10000))
                secondRoll = critCreation(random.randint(0,10000))
                totalRoll = firstRoll + secondRoll
                
                if totalRoll == 0:
                    if critRoll:
                        if currentRollSlot == 6:
                            if checkerCrit < (critDesired - 10):
                                resetCount += 1
                                BLEWW = True
                                break
                        if checkerCrit >= undoThreshHold:       
                            undoCount += 1
                    else:
                        itemRolls[currentRollSlot] = -1
                        currentRollSlot += 1
                        if currentRollSlot > 6:
                            resetCount += 1
                            BLEWW = True
                            break
                else:
                    # CC roll, assigns to first most available slot
                    itemRolls[currentRollSlot] = totalRoll
                    currentRollSlot += 1
                    checkerCrit += totalRoll
                    if totalRoll > 0:
                        critRoll = True
            
            # Stop early if goal met
            if checkerCrit >= critDesired or currentRollSlot > 6:
                break
      
                    
        if not BLEWW:
            for i in range(7):
                if itemRolls[i] > 0:
                    critAmount += itemRolls[i]
            
            if critAmount >= critDesired:
                maxSum = printSummary(critDesired, undoThreshHold, modifierThreshold)
                itemRolls.append(maxSum)
                return itemRolls
        
        globalItemRolls += 1
        

def critCreation(randomGenerated):
    if randomGenerated <= 80:
        return 5
    elif randomGenerated <= 128:
        return 10
    else:
        return 0
            
    
def printSummary(critCC, undoThreshHold, modifierThreshold):
    totalSum = itemCount * itemCost + scrollCount * scrollCost + undoCount * undoCost + holyCount * holyCost + resetCount * resetCost + lModCost*lModCount
    global itemRolls
    print(f"Statistics to obtain a {critCC}cc item ({', '.join(map(str, itemRolls))})")
    print(f"Parameters: Undo Scroll Threshhold {undoThreshHold}cc || Lmod threshhold {modifierThreshold}cc")

    print(f"{'Items used:':<12} {itemCount:<9} || {itemCount * itemCost:>9}g")
    print(f"{'Cursed used:':<12} {scrollCount:<9} || {scrollCount * scrollCost:>9}g")
    print(f"{'Undos used:':<12} {undoCount:<9} || {undoCount * undoCost:>9}g")
    print(f"{'Holys used:':<12} {holyCount:<9} || {holyCount * holyCost:>9}g")
    print(f"{'Resets used:':<12} {resetCount:<9} || {resetCount * resetCost:>9}g")
    print(f"{'Lmods used:':<12} {lModCount:<9} || {lModCount * lModCost:>9}g")
    print(f"{'Total cost:':<12} {int(totalSum):<9} || {totalSum/1000:>9}p\n")
    
    return totalSum
