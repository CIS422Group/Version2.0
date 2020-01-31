"""
functions to read student data from a file into the queue, and write the queue back out to a file

"""

from objects import Student, Queue

studentQ = Queue()

def readFile(filepath, delimiter="    "):

    try:
        with open(filepath, "r") as f:
            next(f)     # skip first line of roster file (comments)
            for i, line in enumerate(f):
                elements = line.split(delimiter)

                try:
                    fname = str(elements[0])
                    lname = str(elements[1])
                    uoID = int(elements[2])
                    email = str(elements[3])
                    phonetic = str(elements[4])
                    reveal = bool(elements[5])

                    # create student object
                    studentQ.enqueue(Student(fname, lname, uoID, email, phonetic, reveal))

                except (ValueError, IndexError):
                    print(f"Line {i} of roster file is formatted incorrectly")
                    quit()

    except FileNotFoundError:
        print("File Does not exist")
        quit()

def overwriteFile(filepath, delimiter="    "):
    try:
        with open(filepath, "r") as f:
            comment = f.readline()

    except FileNotFoundError:
        print("File Does not exist")
        quit()

    try:
        # Overwrite roster file, but preserve the first line
        with open(filepath, "w") as f:
            f.write(comment)
            while len(studentQ.q) > 0:
                student = studentQ.dequeue()    # FIXME: requires dequeue to return the student that was popped, or a peak function
                line = f"{student.fname}{delimiter}{student.lname}{delimiter}{student.uoID}{delimiter}{student.email}{delimiter}{student.phonetic}{delimiter}{student.reveal}\n"
                f.write(line)

    except FileNotFoundError:
        print("File Does not exist")
        quit()

# example, reads students into queue, then reads them back out (random selection and sorting would occur between these steps)
readFile("sample_data.txt", ",")
studentQ.printQ()
overwriteFile("sample_data.txt")
# overwriteFile("sample_data.txt", delimiter=",")

    