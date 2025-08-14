import tkinter as tk
import Calculator
import os
from PIL import Image, ImageTk

def run_simulation():
    try:
        desiredCrit = int(entry_crit.get())
        undoThreshold = int(entry_undo.get())
        modifierThreshold = int(entry_mod.get())
        totalRuns = int(entry_runs.get())
        if desiredCrit < 0 or undoThreshold < 0 or modifierThreshold < 0 or totalRuns < 0:
            raise ValueError('')
        warning_label.config(text="45+ cc and WILL throttle program at any # of runs")
    except ValueError:
        warning_label.config(text="⚠ Please enter valid integers!")
        return
    
    totalCost = 0
    output_text.delete("1.0", tk.END)
    
    for i in range(totalRuns):
        output_text.insert(tk.END, f"Trial {i+1}\n----------------------\n")
        print(f"Trial {i+1}")
        resultCost = Calculator.calculate(desiredCrit, undoThreshold, modifierThreshold)
        totalCost += resultCost[7]
        output_text.insert(tk.END, f"Cost: {resultCost[7]/1000}p\n")
        output_text.insert(tk.END, "Item Stats: " + ", ".join(str(resultCost[i]) for i in range(7)) + "\n\n")
        output_text.update()
    
    avgCost = totalCost / totalRuns / 1000
    output_text.insert(tk.END, f"Average cost for {desiredCrit}cc: {avgCost}p\n")
    if(avgCost < 100):
        output_text.insert(tk.END, f"So cheap!")
    else:
        output_text.insert(tk.END, f"Goodluck affording that gang X_X")
        
#Main
root = tk.Tk()
root.title("Vesteria Crit Roll Simulation. Made by PlitZap")

#Peak icon bruh
icon_path = os.path.join("assets", "Cursed_scroll_new.png")
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon)

bg_color = "#2e1a3b"
fg_color = "#d74c4c"
entry_bg = "#3b2450"
entry_fg = "#d74c4c"
root.configure(bg=bg_color)


input_frame = tk.Frame(root, bg=bg_color)
input_frame.pack(pady=15)

tk.Label(input_frame, text="Desired Crit Chance:", bg=bg_color, fg=fg_color).grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_crit = tk.Entry(input_frame, bg=entry_bg, fg=entry_fg, insertbackground=fg_color)
entry_crit.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
entry_crit.insert(0, "10")

tk.Label(input_frame, text="Undo Threshold:", bg=bg_color, fg=fg_color).grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_undo = tk.Entry(input_frame, bg=entry_bg, fg=entry_fg, insertbackground=fg_color)
entry_undo.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
entry_undo.insert(0, "10")

tk.Label(input_frame, text="Modifier Threshold:", bg=bg_color, fg=fg_color).grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_mod = tk.Entry(input_frame, bg=entry_bg, fg=entry_fg, insertbackground=fg_color)
entry_mod.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
entry_mod.insert(0, "10")

tk.Label(input_frame, text="Number of Runs:", bg=bg_color, fg=fg_color).grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_runs = tk.Entry(input_frame, bg=entry_bg, fg=entry_fg, insertbackground=fg_color)
entry_runs.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
entry_runs.insert(0, "10")

tk.Button(input_frame, text="Run Simulation", command=run_simulation, bg="#4b2a6e", fg=fg_color).grid(row=4, column=0, columnspan=2, pady=10)

#Big nono
warning_label = tk.Label(root, text="45+ cc and WILL throttle program at any # of runs", bg=bg_color, fg="#ff5555", font=("Arial", 10))
warning_label.pack(pady=(0, 5))

#Chad frame
text_frame = tk.Frame(root, width=500, height=400, bg=bg_color)
text_frame.pack(pady=20)
text_frame.pack_propagate(False)

#Chad summoned
image_path = os.path.join("assets", "Chad_Vesteria.png")
img = Image.open(image_path)
img = img.resize((int(img.width*0.7), int(img.height*0.7)), Image.Resampling.LANCZOS)
if img.mode != "RGBA":
    img = img.convert("RGBA")
alpha = img.split()[3]
alpha = alpha.point(lambda p: int(p * 0.05))
img.putalpha(alpha)
tk_img = ImageTk.PhotoImage(img)
bg_label = tk.Label(text_frame, image=tk_img, bg=bg_color)
bg_label.place(relx=0.5, rely=0.5, anchor="center")

#Scroll bar
container = tk.Frame(text_frame, bg="#3b2450")
container.place(relx=0.5, rely=0.5, anchor="center")

scrollbar = tk.Scrollbar(container)
scrollbar.pack(side="right", fill="y")

output_text = tk.Text(
    container, height=20, width=50, bg="#3b2450", fg=fg_color,
    insertbackground=fg_color, yscrollcommand=scrollbar.set
)
output_text.pack(side="left", fill="both")

scrollbar.config(command=output_text.yview)


root.resizable(False, False)
root.bind("<F11>", lambda e: None)
root.bind("<Escape>", lambda e: None)

root.mainloop()
