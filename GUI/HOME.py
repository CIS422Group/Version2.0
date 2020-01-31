'''
Author: Lucas Hyatt
Last Modified: 1/30/20
'''


'''======================================Imports=========================================='''
import tkinter as tk
from tkinter import filedialog, Text
import tkinter.ttk as ttk
import tkinter.font
import os
import GUI
import sys
from datetime import datetime

# Needed for importing files a level up
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from objects import Student, classQueue


'''======================================Functions=========================================='''

# def switch_view():
#     GUI.testcontrol()

STUDENTQUEUE = classQueue()
ROSTERPATH = "" # This is the global roster path, set by inputFile. Might want to change it later

def switch_view():
    if not GUI.userViewOpen():  # prevent 2 user view windows from opening simultaneously
        GUI.testcontrol(ROSTERPATH, STUDENTQUEUE)

def inputFile(delimiter = "    "):
    global ROSTERPATH

    filepath = filedialog.askopenfilename(initialdir="./..", title="Select File")
    if filepath == '':
        return

    ROSTERPATH = filepath

    try:
        with open(filepath, "r") as f:
            next(f)     # skip first line of roster file (comments)
            for i, line in enumerate(f):
                elements = line.strip().split(delimiter)

                try:
                    fname = str(elements[0])
                    lname = str(elements[1])
                    uoID = int(elements[2])
                    email = str(elements[3])
                    phonetic = str(elements[4])
                    # reveal = bool(elements[5])
                    reveal = 0

                    if len(elements) >= 9:
                        
                        numCalled = int(elements[6])
                        numFlags = int(elements[7])
                        dates = list("".join(elements[8:]).replace("[", "").replace("]", "").split())

                        # Sort Dates Chronologically
                        dates = [datetime.strptime(date, "%d/%m/%y") for date in dates]
                        dates.sort(key = lambda date: date)
                        dates = [date.strftime("%d/%m/%y") for date in dates]
                        dates = '['  + ' '.join(dates) + ']'
                        
                    else:
                        numCalled = 0
                        numFlags = 0
                        dates = []

                    # Create Student object, Insert into Queue
                    STUDENTQUEUE.enqueue(Student(fname, lname, uoID, email, phonetic, reveal, numCalled, numFlags, dates))

                except (ValueError, IndexError):
                    print("Line {} of roster file is formatted incorrectly".format(i+1))

                    # display error box
                    title = 'Value/Index Error'
                    heading = 'Unable to open file'
                    msg = 'Line {} is formatted incorrectly'.format(i+1)
                    GUI.displayError(title, heading, msg)
                    return

    except FileNotFoundError:
        print('File Can\'t Be Opened')

        # display error box
        title = 'File Can\'t Be Opened'
        heading = 'Unable to open file'
        msg = 'File Can\'t Be Opened'
        GUI.displayError(title, heading, msg)
        return
    except:
        print('File Can\'t Be Opened')

        # display error box
        title = 'File Can\'t Be Opened'
        heading = 'Unable to open file'
        msg = 'File Can\'t Be Opened'
        GUI.displayError(title, heading, msg)
        return

    # FIXME: these calls are temporary
    STUDENTQUEUE.printQ()
    # writeSummaryPerformanceFile()
    # overwriteRosterFile(ROSTERPATH, STUDENTQUEUE)


def writeSummaryPerformanceFile():

    filepath = "../SummaryPerformanceFile.txt"
    header = "Summary Performance File for the Cold-Call-Assist program. Number-of-Times-Called    Number-of-Flags    First-Name    Last-Name    UO-ID    Email    Phonetic-Spelling    Reveal-Code    List-of-Dates\n"

    try:
        with open(filepath, "w") as f:
            f.write(header)

            for student in STUDENTQUEUE.queue:
                line = student.summaryPerformance()
                f.write(line)

    except FileNotFoundError:
        print('File Can\'t Be Opened')

        # display error box
        title = 'File Can\'t Be Opened'
        heading = 'Unable to open file'
        msg = 'File Can\'t Be Opened'
        GUI.displayError(title, heading, msg)
        return
    except:
        print('File Can\'t Be Opened')

        # display error box
        title = 'File Can\'t Be Opened'
        heading = 'Unable to open file'
        msg = 'File Can\'t Be Opened'
        GUI.displayError(title, heading, msg)
        return

def writeLogFile():

    if len(STUDENTQUEUE.queue) == 0:
        print("No data to log")

        # display error box
        title = 'No Data'
        heading = 'No data to log'
        msg = ''
        GUI.displayError(title, heading, msg)
        return

    filepath = "../dailyLogFile.txt"
    date = datetime.now().strftime("%d/%m/%y %H:%M")
    header = "Log File. Last Modified " + date + "\n"

    try:
        with open(filepath, "w") as f:
            f.write(header)

            for student in STUDENTQUEUE.queue:
                if student.reveal:
                    line = "X    {} {} <{}>\n".format(student.fname, student.lname, student.email)
                    f.write(line)

    except FileNotFoundError:
        print('File Can\'t Be Opened')

        # display error box
        title = 'File Can\'t Be Opened'
        heading = 'Unable to open file'
        msg = 'File Can\'t Be Opened'
        GUI.displayError(title, heading, msg)
        return
    except:
        print('File Can\'t Be Opened')

        # display error box
        title = 'File Can\'t Be Opened'
        heading = 'Unable to open file'
        msg = 'File Can\'t Be Opened'
        GUI.displayError(title, heading, msg)
        return

def exports():
    writeSummaryPerformanceFile()
    writeLogFile()

def exitProgram():
    window = GUI.getUserViewWindow()  # USER_VIEW_WINDOW global var must be set right after creating window
    if window is not None:
        window.closeWindow()
    root.destroy()

'''======================================GUI=========================================='''

'''
Color Scheme:

red = #ff0443
blue = #0486ff
yellow = #ffde04
'''

root = tk.Tk() #Establishes structure for app window
root.resizable(False, False)
root.title("Cold Call System")
root.attributes("-topmost", True)  # open window in front


pane = tk.Frame(root, bg = '#0486ff', bd=30)
pane.pack(fill = tk.BOTH, expand = True)

button_font = tkinter.font.Font(family="Helvetica",size=20,weight="bold")

#Progress bar will show how many student out of the roster have been chosen.
'''progress = ttk.Progressbar(pane, orient=tk.HORIZONTAL, length=496)
progress['value'] = 25
progress.pack(side=tk.BOTTOM)'''

user_view = tk.Button(pane, pady=8, text="User View", highlightbackground='#0486ff', command=switch_view)
user_view.pack(side=tk.LEFT) 
user_view['font'] = button_font

input_roster = tk.Button(pane, pady=8, text="Input Roster", highlightbackground='#0486ff', command=inputFile)
input_roster.pack(side=tk.LEFT)
input_roster['font'] = button_font

export_calls = tk.Button(pane, pady=8, text="Export to Log", highlightbackground='#0486ff', command=exports)
export_calls.pack(side=tk.LEFT) 
export_calls['font'] = button_font

exit_menu = tk.Button(pane, pady=8, text="Quit", highlightbackground='#0486ff', command=exitProgram)
exit_menu.pack(side=tk.LEFT) 
exit_menu['font'] = button_font

# Main Loop
root.attributes("-topmost", False)  # allow window to go behind other windows
root.mainloop()
exit()

'''
Sources: 
https://stackoverflow.com/questions/31128780/tkinter-how-to-make-a-button-center-itself
https://www.geeksforgeeks.org/python-pack-method-in-tkinter/
https://www.youtube.com/watch?v=u4ykDbciXa8&feature=youtu.be
https://www.youtube.com/watch?v=qC3FYdpJI5Y&feature=youtu.be
https://stackoverflow.com/questions/110923/how-do-i-close-a-tkinter-window
https://www.tutorialspoint.com/python/tk_place.htm
'''














