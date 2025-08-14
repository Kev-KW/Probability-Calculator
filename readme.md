# Vesteria Crit Roll Simulator
 ![Image Alt](https://github.com/Kev-KW/Vesteria-Cursed-Scroll-Simulator/blob/e706acbf23accc50eea9860543bc6f0dd8ebec91/assets/Cursed_scroll_new.png)

This Python script simulates rolling items in the game *Vesteria* to reach a desired **critical chance (CC)**. It calculates the total cost in gold required to achieve a target CC, taking into account items, scrolls, undo scrolls, holy items, resets, and Lmods.

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

## Requirements
Copy and paste the required packages into your **terminal**

- Install Pillow for Python (cross-platform)
  - `pip install Pillow`

- For Linux users: install Tkinter support
  - `sudo apt-get install python3-tk`

- Python Version used: `3.11.5`

## How It Works

1. **Adjustable Costs**  
   At the top of the Calculator.py, you can change the cost of each resource according to the current game economy:
   ```python
   itemCost = 10
   scrollCost = 0.5
   undoCost = 100
   holyCost = 5
   resetCost = 2
   lModCost = 50

2. **Execute Program**
   Once you've adjusted the prices of items, simply run ParameterExecutable.py in your IDE

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
  - **Explosion** → The item is destroyed.
  - **Failed roll** → Roll did not add stats.
  - **Successful roll** → Adds to critical chance.
- Critical chance per roll is calculated using `critCreation()`:
  - 0–80 → +5 CC
  - 81–128 → +10 CC
  - Otherwise → 0 CC
- Thresholds dynamically affect failure chances (`failBlow` and `failDestroy`) and Lmod usage.
- Remaining/failed attempts will not be `replenished` if a desired cc is achieved
  - For example, with a desired cc of 25, roles can be shown as:
  - [-2, -2, 10, 5, 10, 0, 0]

---

## Statistics Output

`printSummary()` displays:

- Number of items used
- Scrolls used
- Undos used
- Holys used
- Resets used
- Lmods used
- Total cost in gold (and in thousands for convenience)

## Contributers
- Me :>
  - Gimmie upvote and gold in-game!!!  (PlitZap, Kev)
