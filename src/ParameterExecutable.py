import tkinter as tk
from tkinter import messagebox
import Calculator
import os
from PIL import Image, ImageTk

def run_simulation():
    try:
        desiredCrit = int(entry_crit.get())
        undoThreshold = int(entry_undo.get())
        modifierThreshold = int(entry_mod.get())
        totalRuns = int(entry_runs.get())
        warning_label.config(text="Higher cc and runs will severely throttle program")
    except ValueError:
        warning_label.config(text="⚠ Please enter valid integers!")
        return
    
    totalCost = 0
    output_text.delete("1.0", tk.END)
    
    for i in range(totalRuns):
        output_text.insert(tk.END, f"Trial {i+1}\n----------------------\n")
        resultCost = Calculator.calculate(desiredCrit, undoThreshold, modifierThreshold)
        totalCost += resultCost
        output_text.insert(tk.END, f"Cost: {resultCost}\n\n")
        output_text.update()
    
    avgCost = totalCost / totalRuns / 1000
    output_text.insert(tk.END, f"Average cost for {desiredCrit}cc: {avgCost}p\n")

# Main window
root = tk.Tk()
root.title("Vesteria Crit Roll Simulation")

# Set icon
icon_path = os.path.join("assets", "Cursed_scroll_new.png")
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon)

# Colors
bg_color = "#2e1a3b"
fg_color = "#d74c4c"
entry_bg = "#3b2450"
entry_fg = "#d74c4c"
root.configure(bg=bg_color)

# Input frame for centering
input_frame = tk.Frame(root, bg=bg_color)
input_frame.pack(pady=15)  # move down a little, centered horizontally

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

# Warning label
warning_label = tk.Label(root, text="", bg=bg_color, fg="#ff5555", font=("Arial", 10))
warning_label.pack(pady=(0, 5))

# Frame for text + stationary image
text_frame = tk.Frame(root, width=500, height=400, bg=bg_color)
text_frame.pack(pady=20)
text_frame.pack_propagate(False)

# Load and process image
image_path = os.path.join("assets", "Chad_Vesteria.png")
img = Image.open(image_path)
img = img.resize((int(img.width*0.7), int(img.height*0.7)), Image.Resampling.LANCZOS)
if img.mode != "RGBA":
    img = img.convert("RGBA")
alpha = img.split()[3]
alpha = alpha.point(lambda p: int(p * 0.05))
img.putalpha(alpha)
tk_img = ImageTk.PhotoImage(img)

# Place stationary image behind text
bg_label = tk.Label(text_frame, image=tk_img, bg=bg_color)
bg_label.place(relx=0.5, rely=0.5, anchor="center")

# Text widget on top of image
output_text = tk.Text(text_frame, height=20, width=50, bg="#3b2450", fg=fg_color, insertbackground=fg_color)
output_text.place(relx=0.5, rely=0.5, anchor="center")

# Keep reference
text_frame.image_ref = tk_img

# Lock window size
root.resizable(False, False)
root.bind("<F11>", lambda e: None)
root.bind("<Escape>", lambda e: None)

root.mainloop()
