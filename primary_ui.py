#!usr/bin/env/python3

"""UI for main page. Contains:
    - Available sessions
    - Button to open session editor
    - Button to open profile/settings
    - Progress bar for current session and segment
    - Pause button
    """

import time
import requests
import tkinter as tk
import tkinter.ttk as ttk
import session_creator as sc
import player

TEST_SESS_LENGTH = 60
TEST_DIVISIONS = 4
TEST_RATIO = 2

class MainView ():
    def __init__(self):

        # Set up window
        self.window = tk.Tk()

        # Buttons

        # Fill in premade sessions
        #Get data
        save_data = requests.get("http://localhost:3000/studysessions", timeout= 10)
        data_json = save_data.json()
        for session in data_json:
            sess_btn = tk.Button(self.window, text=session['name'], command= lambda: self.sess_play(session["full_dur"],
                                                                                                     session["break_dur"],
                                                                                                     session["study_dur"],
                                                                                                     session["study_link"],
                                                                                                     session["break_link"]))
            sess_btn.pack()

        self.sess_creator = tk.Button(self.window, text="Create new session", command=self.sess_create)
        self.sess_creator.pack()

        #Progress bars: Segment progress and session progress

        self.segment_progress = ttk.Progressbar(self.window, orient = "horizontal",
                                                length=100, mode="determinate")
        self.segment_progress.pack()

        self.session_progress = ttk.Progressbar(self.window, orient = "horizontal",
                                                length=100, mode="determinate")
        self.session_progress.pack()

        #session variables



    # Button function

    def sess_play(self, sess_length, break_length, study_length, study_link, break_link):
        # Write links to files
        with open("study_link.txt", mode="w", encoding="utf-8") as study_in:
            study_in.write(study_link)
        
        with open("break_link.txt", mode="w", encoding="utf-8") as break_in:
            break_in.write(break_link)

        current_segment_time = 0
        is_break = False

        # Start time
        print("starting session...") #debug
        player.play_yt("study_link.txt")
        for second in range(0, sess_length + 1):
            #update session progress
            self.session_progress['value'] = (second / sess_length) * 100
            #print("updated session progress.") #debug

            #If segment bar is full, reset and change to opposite segment type
            if self.segment_progress['value'] == 100:
                print("resetting Segment progress...") #debug
                is_break = not is_break
                print(f'is_break: ', {is_break})
                # Set music
                if not is_break: 
                    # set to study music
                    player.play_yt("study_link.txt")
                else:
                    player.play_yt("break_link.txt")
                current_segment_time = 0

            #Update segment progress
            if not is_break:
                # print("Updating study progress...") #debug
                self.segment_progress['value'] = (current_segment_time / study_length) * 100
            else: 
                # print("Updating break progress...") #debug
                self.segment_progress['value'] = (current_segment_time / break_length) * 100
            #print("Updated segment progress") #debug

            # Increment time 
            self.window.update_idletasks()
            time.sleep(1.0)
            current_segment_time += 1


    def sess_create(self):
        """Open session creator window, run session."""
        s_creator = sc.Session_create()
        s_creator.window.mainloop()

        with open('time_data.txt', mode='r', encoding='utf-8') as infile:
            time_data_str = infile.read()

        time_data_tupl = time_data_str.split(',')
        session_length = int(time_data_tupl[0])
        break_length = int(time_data_tupl[1])
        study_length = int(time_data_tupl[2])
        current_segment_time = 0
        is_break = False

        # Start time
        print("starting session...") #debug
        player.play_yt('study_link.txt')
        for second in range(0, session_length + 1):
            #update session progress
            self.session_progress['value'] = (second / session_length) * 100
            #print("updated session progress.") #debug

            #If segment bar is full, reset and change to opposite segment type
            if self.segment_progress['value'] == 100:
                print("resetting Segment progress...") #debug
                is_break = not is_break
                print(f'is_break: {is_break}')
                # Set music
                if not is_break: 
                    # set to study music
                    player.play_yt("study_link.txt")
                else:
                    player.play_yt("break_link.txt")
                current_segment_time = 0

            #Update segment progress
            if not is_break:
                # print("Updating study progress...") #debug
                self.segment_progress['value'] = (current_segment_time / study_length) * 100
            else: 
                # print("Updating break progress...") #debug
                self.segment_progress['value'] = (current_segment_time / break_length) * 100
            #print("Updated segment progress") #debug

            # Increment time 
            self.window.update_idletasks()
            time.sleep(1.0)
            current_segment_time += 1
