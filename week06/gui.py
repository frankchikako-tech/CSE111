import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import random

def main():
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.master.title("Dice")
    frm_main.pack(padx=3, pady=3,fill=tk.BOTH, expand=True)
    setup_main(frm_main)
    frm_main.mainloop()

def setup_main(frm_main):
    lbl_sides= Label(frm_main, text="Enter the Number of sides on the dice (2-20)")
    lbl_sides.grid(row=0, column=0, padx=3, pady=3)
    ent_sides = IntEntry(frm_main, width=5, lower_bound=2, upper_bound=20)
    ent_sides.grid(row=0, column=1)
    lbl_counts = Label(frm_main, text="Enter the Number of dice to roll(1-10)")
    lbl_counts.grid(row=1, column=0)
    ent_counts = IntEntry(frm_main, width=2, lower_bound=1, upper_bound=10)
    ent_counts.grid(row=1, column=1)
    btn_roll = Button(frm_main, text="Roll it")
    btn_roll.grid(row=2, column=0)
    lbl_rolls = Label(frm_main, text="")
    lbl_rolls.grid(row=3, column=0)
    def roll_dice(sides, counts):
        sum = 0
        roll_text = ""
        for i in range(counts):
            dice_roll = random.randint(1, sides)
            sum += dice_roll
            roll_text += f"{dice_roll} "
        roll_text += f"Total: {sum}" 
        return roll_text
    

    def roll_action():
        sides = ent_sides.get()
        counts = ent_counts.get()
        lbltext = roll_dice(sides, counts)
        lbl_rolls.config(text=lbltext)
      
    btn_roll.config(command=roll_action)




















if __name__ == "__main__":
    main()