import random
import keyboard


itemCount = 0
itemCost = 15
scrollCount = 0
scrollCost = .5
undoCount = 0
undoCost = 100
holyCount = 0
holyCost = 5
resetCount = 0
resetCost = 2


critAmount = 0

currentRollSlot = 0
failedRollSlot = 6
itemRolls = [0,0,0,0,0,0,0]
critRoll = False


def calculate(critDesired,undoBool):
    global itemCount
    global scrollCount
    global undoCount
    global holyCount
    global resetCount
    
    global critAmount
    
    global currentRollSlot
    global failedRollSlot
    global critRoll
    
    while True: 
        if keyboard.is_pressed("q"):
            printSummary()
            break
        
        # Key Index: 
        # 5, 10, 15, 20 represent crit roll
        # -1 represents failed Roll
        # -2 represents bad Roll
        
        while True:
            if(not(critRoll)):
                checkCritRoll()
            
            successRoll = random.randint(1,100)
            
            # Check whether all 7 slots have been used
            if(currentRollSlot > 6): break
            
            # EXPLOSION
            if(successRoll <= 20):
                itemCount += 1
                break
            
            # Failed roll, we will now see whether to use holy/reset/do nothing
            elif (successRoll <= 40):
                if(critRoll): 
                    # Uses holy for failed slot when no space left
                    if(currentRollSlot == failedRollSlot):
                        
                        # Checks whether we should be wasting holies to achieve desired crit
                        if(currentRollSlot == 6):
                            checkerCrit = 0
                            for i in range(0,6):
                                if(itemRolls[i] > 0):
                                    checkerCrit += itemRolls[i]
                                    
                            if(checkerCrit >= (critDesired - 10)):
                                holyCost += 1
                                if(failedRollSlot != 6):
                                    failedRollSlot += 1
                                    
                            else: break
                        
                        holyCost += 1
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
                
                if(firstRoll + secondRoll < 0):
                    # If there is a crit roll on it already, undo will be used
                    if(critRoll):
                        if(currentRollSlot == 6):
                            checkerCrit = 0
                            for i in range(0,6):
                                if(itemRolls[i] > 0):
                                    checkerCrit += itemRolls[i]
                            # Does not waste undo if last role isn't within 10 cc        
                            if(checkerCrit < (critDesired - 10)):
                                resetCount += 1
                                break
                            
                        undoCount += 1
                    else:
                        # Bad roll remains on item.
                        itemRolls[currentRollSlot] = -2
                        currentRollSlot += 1
                        if(currentRollSlot > 6):
                            resetCost += 1
                            break
                else:
                    itemRolls[currentRollSlot] = firstRoll + secondRoll
                    currentRollSlot += 1
        if(currentRollSlot == 7):
            for i in range(0,6):
                if(itemRolls[i] > 0):
                    critAmount += itemRolls[i]
            print(f"This item completed with {critAmount}cc!")
            if(critAmount >= critDesired):
                printSummary()
                break
        else:
            print(f"Item blew or resetted!")
            itemCount = 0
            scrollCount = 0
            undoCount = 0
            holyCount = 0
            resetCount = 0
            critAmount = 0
            
            currentRollSlot = 0
            failedRollSlot = 6
            critRoll = 0
            
        
        
            
            
                        
                    
                
          
                
                
            
            
            
def checkCritRoll():
    for i in range(0,6):
        if(itemRolls[i] > 0):
            global critRoll
            critRoll = True

def critCreation(randomGenerated):
    if (randomGenerated <= 80):
        return 5
    elif (randomGenerated <= 128):
        return 10
    else:
        return 0
            
def resetStats():
    for i in range(0,len(itemRolls)):
        itemRolls[i] = 0
    global currentRollSlot
    global critRoll
    currentRollSlot = 0
    critRoll = False
    
def printSummary():
    print(f"Items used: {itemCount}     || {itemCount * itemCost}g")
    print(f"Cursed used: {scrollCount}  || {scrollCount * scrollCost}g")
    print(f"Undos used: {undoCount}     || {undoCount * undoCost}g")
    print(f"Holys used: {holyCount}     ||  {holyCount * holyCost}g")
    print(f"Resets used: {resetCount}   ||  {resetCount * resetCost}g")
    print(f"The total cost was {itemCount * itemCost + scrollCount * scrollCost + undoCount * undoCost + holyCount* holyCount + resetCount * resetCost}")
