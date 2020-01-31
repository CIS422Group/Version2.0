"""
The main GIU window for selecting students V1.O

Author: Jimmy Lam
Last Modified: 1/23/20

Author: Yin Jin
Last Modified: 1/28/20

"""

import tkinter as tk
import time

from backend.objects import Student, classQueue
from backend.control import *
# from backend.io import *

class GUI:
    def __init__(self, winTitle: str):
        self.title = winTitle
        self.mainWindow = tk.Tk()
        self.text = tk.Text(self.mainWindow, height=1, width=60, font=('Courier', 16))

        self.mainWindow.title(self.title)  # set window title (grey bar at top)
        self.mainWindow.attributes("-topmost", True)  # keep the window in front of all other windows

        # for backend
        self.Roster = initRoster()              # creat a golable Roster which is a quene of a Student object
        self.onDeck = initDeck(self.Roster)     # 4 student object on deck, current_Index will be the index 
        self.current_Index = 0                  # the picked student's index in onDeck queue
        self.flagQ = classQueue()               # a list of student been flag 


    def leftKey(self, event):
        # print("Left key pressed")
        self.current_Index = left(self.current_Index, self.onDeck, self.Roster)
        names, highlightBegin, highlightEnd = OnDeckString(self.current_Index, self.onDeck)
        # print(names, highlightBegin, highlightEnd)
        self.update(names, highlightBegin, highlightEnd)

    def rightKey(self, event):
        # print("Right key pressed")
        self.current_Index = right(self.current_Index, self.onDeck, self.Roster)
        names, highlightBegin, highlightEnd = OnDeckString(self.current_Index, self.onDeck)
        # print(names, highlightBegin, highlightEnd)
        self.update(names, highlightBegin, highlightEnd)

    def upKey(self, event):
        # print("Up key pressed")
        self.current_Index = up(self.current_Index, self.onDeck, self.Roster, self.flagQ)
        names, highlightBegin, highlightEnd = OnDeckString(self.current_Index, self.onDeck)
        # print(names, highlightBegin, highlightEnd)
        self.update(names, highlightBegin, highlightEnd)

    def downKey(self, event):
        # print("Down key pressed")
        self.current_Index = down(self.current_Index, self.onDeck, self.Roster)
        names, highlightBegin, highlightEnd = OnDeckString(self.current_Index, self.onDeck)
        # print(names, highlightBegin, highlightEnd)
        self.update(names, highlightBegin, highlightEnd)

    def update(self, inText: str, highlightStart: int, highlightEnd: int, highlightColor='green'):
        """ Prints the names given in <inText> to the GUI screen.
        highlightStart is the starting index of the highlighting
        and highlightEnd is the ending index.
        """
        self.text.pack()
        self.text.configure(state='normal')  # reset state in order to change the names
        self.text.delete('1.0', tk.END)      # clear names
        self.text.insert('1.0', inText)      # write text to GUI

        # now add highlighting
        self.text.tag_add('tag1', '1.{}'.format(highlightStart), '1.{}'.format(highlightEnd))
        self.text.tag_config('tag1', background=highlightColor)
        self.text.configure(state='disabled')  # prevents user from clicking and editing the text
        self.mainWindow.update()


class _MessageBox:
    def __init__(self, title: str, heading: str, msg: str):
        self.title = title
        self.heading = heading
        self.msg = msg
        self.canvasWidth = 450
        self.canvasHeight = 170
        self.root = tk.Tk()

        self.iconFile = None

    def closeBox(self):
        self.root.destroy()

    def display(self):

        if self.iconFile is None:
            raise NotImplementedError("cannot use _MessageBox to create a message. Use a child class instead.")

        self.root.title(self.title)
        canvas = tk.Canvas(self.root, height=self.canvasHeight, width=self.canvasWidth,
                           bg='#D3D3D3', highlightthickness=0)

        # center the window on the screen
        width = self.root.winfo_screenwidth()  # width of mac screen (pixels)
        height = self.root.winfo_screenheight()  # height of mac screen (pixels)
        x = (width // 2) - (self.canvasWidth // 2)
        y = (height // 2) - (self.canvasHeight // 2)
        self.root.geometry("{}x{}+{}+{}".format(self.canvasWidth, self.canvasHeight, x, y))

        # force the window to be in front of all other windows
        self.root.attributes("-topmost", True)

        image = tk.PhotoImage(master=canvas, file=self.iconFile)  # file MUST be .gif
        canvas.create_image(60, 50, image=image)

        # print error message
        # (pixels to right from left edge, pixels down, ...)
        canvas.create_text(120, 30, text=self.heading, anchor='w', font=('Calibri', 20, 'bold'))
        canvas.create_text(120, 50, text=self.msg, anchor='nw', font=('Calibri', 16))

        ok = tk.Button(canvas, text="OK", width=10, height=2, highlightbackground='#D3D3D3', command=self.closeBox)
        ok.place(x=175, y=100)
        # ok.configure(foreground='blue')

        canvas.pack()
        self.root.mainloop()

class ErrorBox(_MessageBox):
    def __init__(self, title: str, heading: str, msg: str):
        super().__init__(title, heading, msg)
        self.iconFile = 'error_icon.gif'

class WarningBox(_MessageBox):
    def __init__(self, title: str, heading: str, msg: str):
        super().__init__(title, heading, msg)
        self.iconFile = 'warning_icon.gif'

def displayError(title: str, heading: str, msg: str):
    ErrorBox(title, heading, msg).display()

def displayWarning(title: str, heading: str, msg: str):
    WarningBox(title, heading, msg).display()

def testArrowKeys():
    """ Opens the GUI with 4 names, and the window remains unchanged.
    A message displays whenever an arrow key is pressed.
    """
    name1 = "Maura McCabe"
    name2 = "Jimmy Lam"
    name3 = "Lucas Hyatt"
    name4 = "Yin Jin"
    name5 = 'Noah Tigner'

    gui = GUI('Students on deck')

    print('--- Starting GUI test ---')

    names = "{}   {}   {}   {}".format(name1, name2, name3, name4)

    highlightBegin = len(name1) + 3
    highlightEnd = highlightBegin + len(name2)
    gui.update(names, highlightBegin, highlightEnd)

    # support for arrow key presses, bind() takes in function to use like pthread_create()

    gui.mainWindow.bind("<Left>", gui.leftKey)
    gui.mainWindow.bind("<Right>", gui.rightKey)
    gui.mainWindow.bind("<Up>", gui.upKey)
    gui.mainWindow.bind("<Down>", gui.downKey)

    print("\033[38;5;220mClick on the cold call window. After pressing an arrow key,",
          "\na message should be displayed. Close the cold call window to end the program.",
          "\nNote: the names and highlighting should not update for this test.\033[0m")

    gui.mainWindow.mainloop()  # blocks until the window is closed

def testScreenUpdate():
    """ Updates the names and highlighting."""
    name1 = "Maura McCabe"
    name2 = "Jimmy Lam"
    name3 = "Lucas Hyatt"
    name4 = "Yin Jin"
    name5 = 'Noah Tigner'

    gui = GUI('Students on deck')
    names = "{}   {}   {}   {}".format(name1, name2, name3, name4)

    highlightBegin = len(name1) + 3
    highlightEnd = highlightBegin + len(name2)
    gui.update(names, highlightBegin, highlightEnd)

    print('\nHighlighting moving to the right in 1 second...')
    time.sleep(1)

    highlightBegin = len(name1) + len(name2) + 6
    highlightEnd = highlightBegin + len(name3)
    gui.update(names, highlightBegin, highlightEnd)

    print('Removing Lucas in 1 second...')
    time.sleep(1)

    names = "{}   {}   {}   {}".format(name1, name2, name4, name5)

    highlightBegin = len(name1) + len(name2) + 6
    highlightEnd = highlightBegin + len(name4)
    gui.update(names, highlightBegin, highlightEnd)

    print("\n\033[38;5;220m--- End of test. Close the cold calling window to exit ---\033[0m")
    gui.mainWindow.mainloop()

def testcontrol():
    print('--- Starting control test ---')

    gui = GUI('Students on deck')

    names, highlightBegin, highlightEnd = OnDeckString(gui.current_Index, gui.onDeck)
    print(names)

    gui.update(names, highlightBegin, highlightEnd)

    # support for arrow key presses, bind() takes in function to use like pthread_create()
    gui.mainWindow.bind("<Left>", gui.leftKey)
    gui.mainWindow.bind("<Right>", gui.rightKey)
    gui.mainWindow.bind("<Up>", gui.upKey)
    gui.mainWindow.bind("<Down>", gui.downKey)

    print("\033[38;5;220mClick on the cold call window. After pressing an arrow key,",
          "\na message should be displayed. Close the cold call window to end the program.",
          "\nNote: the names and highlighting should not update for this test.\033[0m")

    gui.mainWindow.mainloop()



def main():
    #testArrowKeys()
    # testScreenUpdate()
    testcontrol()
    
    #displayError("Error test", "Error", "this is a test")
    #displayWarning("Warning test", "Warning", "this is a test")

if __name__ == '__main__':
    main()

"""
Sources:
- examples: https://www.python-course.eu/tkinter_text_widget.php
- font size edit: https://stackoverflow.com/questions/30685308/how-do-i-change-the-text-size-in-a-label-widget-python-tkinter
- highlight name: https://www.tutorialspoint.com/python/tk_text.htm
- read-only window: https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only
- key input: https://stackoverflow.com/questions/19895877/tkinter-cant-bind-arrow-key-events
- centering a window: https://www.youtube.com/watch?v=gjU3Lx8XMS8
- keep window in foreground: https://stackoverflow.com/questions/1892339/how-to-make-a-tkinter-window-jump-to-the-front
- insert image to canvas: https://stackoverflow.com/questions/43009527/how-to-insert-an-image-in-a-canvas-item
- remove border from window: https://stackoverflow.com/questions/4310489/how-do-i-remove-the-light-grey-border-around-my-canvas-widget
- remove button border: https://stackoverflow.com/questions/27084321/tkinter-leaving-borders-around-widgets
"""

