""" D104
    File: tkinter_stopwatch_skeleton.py """

import tkinter as tk
import time

def starttime(event):
    global start
    start = time.time()
    lbl_output["text"] = ""

def endtime(event):
    global end
    end = time.time()
    lbl_output["text"] = f"{end-start:.2} seconds"

# initialize the global variables
start = 0
end = 0
# create the window
root = tk.Tk()
root.title("Stopwatch")
# create the title label
lbl_title = tk.Label(root, text="Simple Stopwatch", 
                     font=("Arial 20 bold"))
# create the label for display the time duration 
# between clicking start and end
lbl_output = tk.Label(root, text="", 
                      font=("Arial 20 normal"))
lbl_instruction = tk.Label(root, text='Click "Start" to start the timer.\n'+
                                      'Click "End" to end the timer.',
                                      font=("Arial 14 normal"))

# TODO: 
# step1: create the "Start" button
# step2: create the "End" button
# step3: bind starttime to button click event of btn_start
# step3: bind endtime to button click event of btn_end
btn_start = tk.Button(root, text="Start")
btn_end = tk.Button(root, text="End")
btn_start.bind("<Button-1>", starttime)
btn_end.bind("<Button-1>", endtime)


# Organize the widgets
lbl_title.grid(row=0, columnspan=2, padx=10, pady=10)
lbl_instruction.grid(row=1, columnspan=2, padx=10, pady=10)
btn_start.grid(row=2, column=0, padx=10, pady=10)
btn_end.grid(row=2, column=1, padx=10, pady=10)
lbl_output.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()