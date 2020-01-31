"""
this file is just a pseudocode for the background of project
mainly inlude 
data structure for 
	main object students which contain all the information that a student may need for the cold call system
	list (linklist or quene) which is a list of student object, which mainly use for choosing the student on the deck

"""

# global variable 
char splitChar  #req: 4.5
int N = 30 		# 0<N<100 ,fist N% of list will be use for choosing, will be used in ording dunction.



class student:
	# basic information 
	String first Name
	String last Name
	int uoID 
	String email

	# use for 
	phoneticSpelling #audio source file req: 3_C_2
	photo			 #photo source file req

	# init as 0, accumulating through the term, 
	# will be use for summary of class participation at the end of term
	# req: 3_D 
	int NumCalled	# number of times called throughout the term	 
	int NumFlage	# 0 is no flage, 1 is flage for 
	list LiDates = [] #dates they answered the questions.

	def printStudent():
		# use for testing, anything that make sence

	def diplay():
		# will by called by UI
		# see req 4.3

	def summaryPerformance():
		# see req 3_D_3
		# return a formated string

	def review():
		# will be called by output file function feedback()
		# see req: 3_B_3
		# return a formated string

	def setPhoneticSpelling(audioFIlE):
		# will be called by the UI

	def getFlage():
		# will be called by output file function feedback()

	def setFlage():
		# will be called by ording function



class classMembers:
	# theis will be easier to do in the linklist, 
	# but it can be any thing as long as the following function can be implements


	def init():
		# anything needed to implement following qusetion
		# it will be great if there is length for the quene, nut not necessary
		list li

	# basic functions
	def addOne():
		# add one student object into the list

	def removeByIndex(int i):
		# Removes Student sd at index i from the list
		# all the students after index i on the list will be shift to the left (base on the req: 4.1)
		# return the removed Student sd

	def insertOne(Student sd, int i):
		# Inserts student at index i to The List
		# python have a built in method for list.insert() may be just use it?

	def isEmpty():
		# return true or false

	def combine(classMembers newlist):
		# combine two list randomly
		# req: 3_c_1, I am not sure about this part, we can discuss


# global functions

# I/O
# according req: 3_B, 3_C, 3_D, 4.3, 4.4, 6.1 and 6.2


# we need two file, (according to 3_C-E, )
# 1. the import file
# 2. actually data storage call it sourcefile
# importData() and initClassMembers() is necessary given what he ask us to do

# we need a global classMembers according to req: 6.1
classMembers roster

def importData(File importfile):
	# req: 3_E_4-5, 4.4 
	# this dunction take a input of file, loop though the file
	# then init and return a classMembers (a built in list of Student) roster
	# rewrite to the data storage file sourcefile
	# this function will be calling when the UI is import File
	# report error if given file is not formate correctly (req: 4.4)

def initClassMembers(File sourcefile):
	# this dunction take a input of file, loop though the file
	# then init and return a classMembers (a built in list of Student)
	# this function will be calling when the application is Startup

def update(classMembers roster):
	# write the update data back to data storage file sourcefile
	# will be calling by UI, when evey time 6.2

	

def feedback():
	# req: 3_B
	# this part should coordinate with UI, we can wait and learn this one first
	# according to the flag, sent different email.
	# can call Student.review() or Student.getFlage()



def PerformanceReport():
	# see req: 3_D
	# you can call function Student.summaryPerformance()
	# creat and write a summary Report.



# random or ordering
def ording(classMembers li):
	# try to come up with algorithm that is fair for every students in the class
	# a few requirments that this function will meet
		# the order is random, 
			# if Student A and Student B is on the deck on the same time,
			# then next time A is on deck, B has very less chance on deck
		# cold down time: m = 10% of class size
			# if Student A is called, then there is a guarantee then next m candidates will not be Student A
		# to be fair, last student will randomly replace the position of last students

	# Or something different (discuss later) 

	return a list of Student objects that will be on the disk










































