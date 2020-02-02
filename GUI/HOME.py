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

def inputFile(delimiter = None):
    global ROSTERPATH

    filepath = filedialog.askopenfilename(initialdir="./..", title="Select File")
    if filepath == '':
        return

    if filepath[-4:] != '.txt':
        GUI.displayError('file type error', 'Unable to open file', 'File must be a text file')

    ROSTERPATH = filepath

    try:
        with open(filepath, "r") as f:
            next(f)     # skip first line of roster file (comments)
            for i, line in enumerate(f):

                elements = line.strip().split(delimiter)

                print(elements)

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

def openDaily(): # Opens the daily log file
    val = os.system("open ./../dailyLogFile.txt")
    if val == 256:
        title = 'File Not Found'
        heading = 'Unable to open Daily Log File'
        msg = 'Please press "Export to Logs" to \ngenerate the file'
        GUI.displayError(title, heading, msg)

def openSummary(): # Opens the summary log file
    val = os.system("open ./../SummaryPerformanceFile.txt")
    if val == 256:
        title = 'File Not Found'
        heading = 'Unable to open Performance File'
        msg = 'Please press "Export to Logs" to \ngenerate the file'
        GUI.displayError(title, heading, msg)

def exitProgram():
    window = GUI.getUserViewWindow()  # USER_VIEW_WINDOW global var must be set right after creating window
    errorWin = GUI.getErrorWindow()
    if window is not None:
        window.closeWindow()
    if errorWin is not None:
        errorWin.closeBox()
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
root.protocol("WM_DELETE_WINDOW", exitProgram)  # calls closeWindow() if user clicks red 'x'

pane = tk.Frame(root, bg = '#0486ff', bd=30)
pane.pack(fill = tk.BOTH, expand = True)

button_font = tkinter.font.Font(family="Helvetica",size=20,weight="bold")
label_font = tkinter.font.Font(family="Helvetica",size=25,weight="bold")

#Progress bar will show how many student out of the roster have been chosen.
'''progress = ttk.Progressbar(pane, orient=tk.HORIZONTAL, length=496)
progress['value'] = 25
progress.pack(side=tk.BOTTOM)'''

label = tk.Label(pane, text="HOME MENU", bg='#0486ff')
label['font'] = label_font
label.grid(row=0, column=0)

user_view = tk.Button(pane, pady=8, width=15, text="User View", highlightbackground='#0486ff', command=switch_view)
# user_view.pack(side=tk.LEFT) 
user_view['font'] = button_font
user_view.grid(row=1, column=0)

input_roster = tk.Button(pane, pady=8, width=15, text="Input a Roster", highlightbackground='#0486ff', command=inputFile)
# input_roster.pack(side=tk.LEFT)
input_roster['font'] = button_font
input_roster.grid(row=2, column=0)

export_calls = tk.Button(pane, pady=8, width=15, text="Export to Logs", highlightbackground='#0486ff', command=exports)
# export_calls.pack(side=tk.LEFT) 
export_calls['font'] = button_font
export_calls.grid(row=3, column=0)

daily_log = tk.Button(pane, pady=8, width=15, text="Daily Log File", highlightbackground='#0486ff', command=openDaily)
# daily_log.pack(side=tk.BOTTOM) 
daily_log['font'] = button_font
daily_log.grid(row=4, column=0)

summary_performance = tk.Button(pane, pady=8, width=15, text="Performance File", highlightbackground='#0486ff', command=openSummary)
# summary_performance.pack(side=tk.BOTTOM) 
summary_performance['font'] = button_font
summary_performance.grid(row=5, column=0)

exit_menu = tk.Button(pane, pady=8, width=15, text="Exit Program", highlightbackground='#0486ff', fg='red', command=exitProgram)
# exit_menu.pack(side=tk.BOTTOM)
exit_menu['font'] = button_font
exit_menu.grid(row=6, column=0)

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














