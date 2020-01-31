"""
The main GIU window for selecting students

Author: Jimmy Lam
Last Modified: 1/18/20
"""

import tkinter as tk
import time

class GUI:
    def __init__(self, winTitle: str):
        self.title = winTitle
        self.mainWindow = tk.Tk()
        self.text = tk.Text(self.mainWindow, height=1, width=60, font=('Courier', 16))

        self.mainWindow.title(self.title)  # set window title (grey bar at top)

    def leftKey(self, event):
        print("Left key pressed")

    def rightKey(self, event):
        print("Right key pressed")

    def upKey(self, event):
        print("Up key pressed")

    def downKey(self, event):
        print("Down key pressed")

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

class ErrorBox(GUI):
    def __init__(self, winTitle: str):
        super().__init__(winTitle)
        #self.text = tk.

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

    print('Removing Lucas in 1 second1...')
    time.sleep(1)

    names = "{}   {}   {}   {}".format(name1, name2, name4, name5)

    highlightBegin = len(name1) + len(name2) + 6
    highlightEnd = highlightBegin + len(name4)
    gui.update(names, highlightBegin, highlightEnd)

    print("\n\033[38;5;220m--- End of test. Close the cold calling window to exit ---\033[0m")
    gui.mainWindow.mainloop()


def main():
    #testArrowKeys()
    testScreenUpdate()

if __name__ == '__main__':
    main()

"""
Sources:
- examples: https://www.python-course.eu/tkinter_text_widget.php
- font size edit: https://stackoverflow.com/questions/30685308/how-do-i-change-the-text-size-in-a-label-widget-python-tkinter
- highlight name: https://www.tutorialspoint.com/python/tk_text.htm
- read-only window: https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only
- key input: https://stackoverflow.com/questions/19895877/tkinter-cant-bind-arrow-key-events
"""

