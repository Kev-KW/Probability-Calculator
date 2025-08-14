import random
import keyboard

globalItemRolls = 0

itemCost = 10
scrollCost = .5
undoCost = 100
holyCost = 5
resetCost = 2
lModCost = 50

critAmount = 0

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
        int: The total cost in gold for reaching the target.
    """
    global itemCount, scrollCount, undoCount, holyCount, resetCount, lModCount
    global critAmount, currentRollSlot, failedRollSlot, itemRolls
    global critRoll, BLEWW, modThreshholdBool, failDestroy, failBlow
    global globalItemRolls
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

    failDestroy = 20
    failBlow = 40
    while True: 
         
        # Key Index: 
        # 5, 10, 15, 20 represent crit roll
        # 0 Represents Unused
        # -1 represents bad Roll
        
        while True:
            # Dynamically track critRoll
            critRoll = any(roll > 0 for roll in itemRolls[:currentRollSlot])
            
            if(modThreshholdBool == False):
                checkerCrit = 0
                for i in range(0,7):
                    if(itemRolls[i] > 0):
                        checkerCrit += itemRolls[i]
                        
                if checkerCrit >= modifierThreshold:
                    failBlow /= 2
                    failDestroy /= 2
                    lModCount += 1
                    modThreshholdBool = True
            successRoll = random.randint(1,100)
            scrollCount += 1
            
            # Check whether all 7 slots have been used
            if(currentRollSlot > 6): break
            
            # EXPLOSION
            if(successRoll <= failDestroy):
                BLEWW = True
                itemCount += 1
                break
            
            # Failed roll, we will now see whether to use holy/reset/do nothing
            elif (successRoll <= failBlow):
                if(critRoll): 
                    # Uses holy for failed slot when no space left
                    if(currentRollSlot == failedRollSlot):
                        
                        # Checks whether we should be wasting holies to achieve desired crit
                        if(currentRollSlot == 6):
                            checkerCrit = 0
                            for i in range(0,7):
                                if(itemRolls[i] > 0):
                                    checkerCrit += itemRolls[i]
                                    
                            if(checkerCrit >= (critDesired - 10)):
                                holyCount += 1
                                if(failedRollSlot != 6):
                                    failedRollSlot += 1
                                
                            else: break
                        
                        holyCount += 1
                        if(failedRollSlot != 6):
                            failedRollSlot += 1
                    else: continue
                # No crit roll in all 7 slots
                elif(failedRollSlot == 0):
                    resetCount += 1
                    break
                else:
                    # No action, just a failed slot
                    failedRollSlot -= 1
                    
                
                
                
            # Successful roll, now add stats 
            else:
                firstRoll = critCreation(random.randint(0,10000))
                secondRoll = critCreation(random.randint(0,10000))
                totalRoll = firstRoll + secondRoll
                
                if(totalRoll == 0):
                    # If there is a crit roll on it already, undo will be used
                    if(critRoll):
                        checkerCrit = 0
                        if(currentRollSlot == 6):
                            for i in range(0,7):
                                if(itemRolls[i] > 0):
                                    checkerCrit += itemRolls[i]
                            # Does not waste undo if last role isn't within 10 cc        
                            if(checkerCrit < (critDesired - 10)):
                                resetCount += 1
                                break
                        if (checkerCrit >= undoThreshHold):       
                            undoCount += 1
                            
                    else:
                        # Bad roll remains on item.
                        itemRolls[currentRollSlot] = -1
                        currentRollSlot += 1
                        if(currentRollSlot > 6):
                            resetCount += 1

                            break
                else:
                    # Positive roll, assign it immediately
                    itemRolls[currentRollSlot] = totalRoll
                    currentRollSlot += 1
            
            # Update checkerCrit and stop early if goal met
            checkerCrit = sum(roll for roll in itemRolls if roll > 0)
            if checkerCrit >= critDesired:
                break
                    
        if(BLEWW != True):
            for i in range(0,7):
                if(itemRolls[i] > 0):
                    critAmount += itemRolls[i]
                        
            # if(critAmount > 0):
                
            #     print(f"This item completed with {critAmount}cc!")
            
            # Prints and returns information
            if(critAmount >= critDesired):
                maxSum = printSummary(critDesired, undoThreshHold, modifierThreshold)
                return maxSum
            
        # else:
        #     print(f"THIS ITEM BLEW UP!!!!")
        
        currentRollSlot = 0
        failedRollSlot = 6
        critAmount = 0
        itemRolls = [0,0,0,0,0,0,0]
        
        failDestroy = 20
        failBlow = 40
        critRoll = False
        BLEWW = False 
        modThreshholdBool = False
        
        globalItemRolls += 1
        
                    
            
def checkCritRoll():
    global critRoll
    for i in range(0,6):
        if(itemRolls[i] > 0):
            critRoll = True

def critCreation(randomGenerated):
    if (randomGenerated <= 80):
        return 5
    elif (randomGenerated <= 128):
        return 10
    else:
        return 0
            
def resetStats():
    global currentRollSlot
    global critRoll
    currentRollSlot = 0
    critRoll = False
    
def printSummary(critCC, undoThreshHold, modifierThreshold):
    totalSum = itemCount * itemCost + scrollCount * scrollCost + undoCount * undoCost + holyCount * holyCost + resetCount * resetCost + lModCost*lModCount
    global itemRolls
    print(f"Statistics to obtain a {critCC}cc item ({', '.join(map(str, itemRolls))})")
    print(f"Parameters: Undo Scroll Threshhold {undoThreshHold}cc || Lmod threshhold {modifierThreshold}cc")

    print(f"{'Items used:':<15} {itemCount:<9} || {itemCount * itemCost:>7}g")
    print(f"{'Cursed used:':<15} {scrollCount:<9} || {scrollCount * scrollCost:>7}g")
    print(f"{'Undos used:':<15} {undoCount:<9} || {undoCount * undoCost:>7}g")
    print(f"{'Holys used:':<15} {holyCount:<9} || {holyCount * holyCost:>7}g")
    print(f"{'Resets used:':<15} {resetCount:<9} || {resetCount * resetCost:>7}g")
    print(f"{'Lmods used:':<15} {lModCount:<9} || {lModCount * lModCost:>7}g")
    print(f"{'Total cost:':<15} {totalSum:<9} || {totalSum/1000:>7}p\n")
    
    return totalSum
