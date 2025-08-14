# Vesteria Crit Roll Simulator
 ![Image Alt](https://github.com/Kev-KW/Vesteria-Cursed-Scroll-Simulator/blob/68cf6d0ec49d3474b9eea93bf504311da11bd318/assets/uwuScroll.png)

This Python script simulates cursing for cc% in *Vesteria* to reach a **desired critical chance**. It calculates the total cost in gold required to achieve a target CC, taking into account items, scrolls, undo scrolls, holy items, resets, and Lmods.

**WARNING!** going above 40 desired cc is almost guaranteed to freeze the program! Be sure to keep # of runs at **one**  to ensure the program doesn't crash or go indefinitely for very high cc. 

---

## Features

- Simulates item rolling until a desired critical chance is reached.
- Tracks costs for all actions:
  - Items
  - Scrolls
  - Undo scrolls
  - Holy items
  - Resets
  - Lmods
- Supports thresholds for:
  - Undo scroll usage
  - Lmod usage
- Randomized rolls simulate real in-game mechanics with success, failure, and explosion chances.

---
## Disclaimer

The GUI application provides only the **estimated cost** of rolling items to reach the desired critical chance. It does **not display detailed in-game mechanics, slot-by-slot results, or item-specific statistics**.  

Additionally, take results with a **heavy grain of salt**. Values used here are from the wiki and may not **reflect** the in-game behavior. Since the program only takes critical chance into account, many other variables are not considered such as `mdi%`, `abr%`, `atk`, and `+stats`.



## How to run
1. **Required packages and version used**

   Copy and paste the required packages into your **terminal**

   - Install Pillow for Python (cross-platform)
     - `pip install Pillow`

   - For Linux users: install Tkinter support
     - `sudo apt-get install python3-tk`

   - Python Version used (Not necessary): `3.11.5`
     
3. **Adjustable Costs**  
   At the top of the Calculator.py, you can change the cost of items to the current game economy:
   ```python
   itemCost = 10
   scrollCost = 0.5
   undoCost = 100
   holyCost = 5
   resetCost = 2
   lModCost = 50

4. **Execute Program**

   Once you've adjusted the prices of items, simply run `ParameterExecutable.py` in your IDE. Again, 45+ cc will take longer than usual runtime per run (Will appear to have crashed)

## Simulation Function

The core function is `calculate(critDesired, undoThreshold, modifierThreshold)`:

- `critDesired` → Target critical chance for the item.
- `undoThreshold` → Threshold to decide when to use undo scrolls.
- `modifierThreshold` → Threshold to decide when to use Lmods.

The function:

- Rolls items slot by slot.
- Tracks crit rolls (5-20), Bad rolls (-1), and Failed/Remaining Rolls (0)
- Uses undo, holy items, resets, and Lmods based on thresholds.
- Stops when the desired critical chance is reached.
- Returns the total gold cost.


---

## Roll Mechanics

- Each item has 7 roll slots.
- Rolls are categorized as:
  - **Exploded** → The item is destroyed.
  - **Failed** → Roll did not add stats or removed a slot.
  - **Successful** → Adds to critical chance.
- Critical chance per roll is calculated using `critCreation()`:
  - 0–80 → +5 CC
  - 81–128 → +10 CC
  - Otherwise → 0 CC
- Thresholds dynamically affect failure chances (`failBlow` and `failDestroy`) and Lmod usage.
- Remaining/failed attempts will not be `replenished` if a desired cc is achieved
  - For example, with a desired cc of 25, roles can be shown as:
  - [-1, -1, 10, 5, 10, 0, 0]

---

## Statistics Output

`printSummary()` displays:

- Number of items used
- Scrolls used
- Undos used
- Holys used
- Resets used
- Lmods used
- Total cost in gold and platinum

## Contributers
- Me :>
  - Gimmie upvote and gold in-game!!!  (PlitZap, Kev)
![Image Alt](https://github.com/Kev-KW/Vesteria-Cursed-Scroll-Simulator/blob/fa887e64422f6e50cba8fa1938db06c3b524806c/assets/Stylized_uwu_emoticon.svg.png)
