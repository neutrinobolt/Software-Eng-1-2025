#!usr/bin/env/python3

"""UI for Session creation. Contains:
- Input box for total session time
- Input box for # divisions
- Input box for Study/break ratio
- Text box stating Current Study/break segment lenghts
- Cancel button
- Input box for youtube link
- Start button"""

import tkinter as tk

class Session_create():
    def __init__(self):
        self.window = tk.Tk()

        # input boxes for timing

        self.session_label = tk.Label(self.window, text="enter the total length of your study session:")
        self.session_label.pack()
        self.session_time = tk.Entry(self.window)
        self.session_time.pack()

        self.div_label = tk.Label(self.window, text="Enter the number of breaks you want to have:")
        self.div_label.pack()
        self.divisions = tk.Entry(self.window)
        self.divisions.pack()

        self.rat_label = tk.Label(self.window, text="Enter the ratio of study to break time you want:")
        self.rat_label.pack()
        self.ratio = tk.Entry(self.window)
        self.ratio.pack()

        # self.segment_calc = tk.Label(self.window, text="Study length: 0 Break length: 0")
        # self.segment_calc.pack()

        self.study_label = tk.Label(self.window, text="Enter the link for your study music:")
        self.study_label.pack()
        self.study_link = tk.Entry(self.window)
        self.study_link.pack()

        self.break_label = tk.Label(self.window, text="Enter the link for your break music:")
        self.break_label.pack()
        self.break_link = tk.Entry(self.window)
        self.break_link.pack()

        self.start_btn = tk.Button(self.window, text="Start", command=self.start)
        self.start_btn.pack()

        self.cancel_btn = tk.Button(self.window, text="Cancel", command=self.cancel)
        self.cancel_btn.pack()

        self.bad_input = tk.Label(self.window, text="Error, bad input. Check to make sure all values are correct.")
    
    #button funcs
    def start(self):
        """Check for adequate inputs
        Calculate time data
        Push time data to txt file connected to primary ui
        Check input link validity
        Push adequate link to txt file"""

        #Check and clean time input. Only ints acceptable
        try:
            total_time = int(self.session_time.get()) * 60
        except ValueError:
            self.session_time.delete(0, tk.END)
            self.bad_input.pack()
            return
        try:
            divisions = int(self.divisions.get())
        except ValueError:
            self.divisions.delete(0, tk.END)
            self.bad_input.pack()
            return
        try:
            ratio = int(self.ratio.get())
        except ValueError:
            self.ratio.delete(0, tk.END)
            self.bad_input.pack()
            return
        
        #calc study and break times
        section_time = total_time / divisions
        break_time = int(section_time / (ratio + 1))
        study_time = break_time * ratio

        #Add later: link cleaner

        #Push time input to txt
        with open("time_data.txt", mode="w", encoding="utf-8") as outfile:
            out_string = str(total_time) + "," + str(break_time) + "," + str(study_time)
            outfile.write(out_string)

        #Add later: Push link to txt
        with open("study_link.txt", mode = "w", encoding="utf-8") as break_file:
            out_string = self.study_link.get()
            if out_string == "":
                break_file.write("none")
            else:
                break_file.write(out_string)
        
        with open("break_link.txt", mode = "w", encoding="utf-8") as break_file:
            out_string = self.break_link.get()
            if out_string == "":
                break_file.write("none")
            else:
                break_file.write(out_string)

        #Close this window
        self.window.destroy()
        self.window.quit()

    def cancel(self):
        """Close creator window w/o creating anything"""
        self.window.destroy()
        self.window.quit
