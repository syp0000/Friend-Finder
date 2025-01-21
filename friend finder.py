#------tkinter libraries-----------#    
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#-------SQLite libraries--------#
import sqlite3 
from sqlite3 import Error

#---------------subroutines for statistics-----------
def Bubble(aScore,aRank): #order the ranked data for comparision
    global size
    L = size
    SWAP = True #have we swapped
    while L > 0 and SWAP == True: # exit if no swaps
        SWAP = False
        for n in range(size-1): #loop through the items
            if aScore[n] < aScore[n+1]: #swap adjacent items
                TEMP_SCORE = aScore[n]
                TEMP_RANK = aRank[n]
                aScore[n] = aScore[n+1]
                aRank[n] = aRank[n+1]                
                aScore[n+1] = TEMP_SCORE
                aRank[n+1] = TEMP_RANK                
                SWAP = True #swap has been made
        L -= 1 #reduce L by 1
    return aRank
#end procedure

def rank(): #order the choices by rank
    global size
    score1 = [0 for n in range(size)] #first set of scores
    score2 = [0 for n in range(size)] #second set of scores
    for n in range(size):
        score1[n] = student1_scores[n] #get contents of the listbox
        score2[n] = student2_scores[n]
        rank1[n] = n+1 #list 0 to 7 next to the score.
        rank2[n] = n+1
    #sort the rank
    Bubble(score1, rank1) #call the Bubble subroutine
    Bubble(score2, rank2)
    correlation() #call the correlation
    print(rank)
    
def correlation(): #comparison between two students
    global size #use 6 and don't create a new local variable
    #----------------------------------
    sigma = 0
    diff = [0 for i in range(size)]
    for i in range(size):
        diff[i] = rank1[i] - rank2[i]
        diff[i] = diff[i] ** 2
        sigma += diff[i]
    total = 1 - ((size * sigma) / (size * ((size**2) - 1)))
    total = total * 100
    total = round(total,2)
    #-----------------------------------
    if total >= 90:
        lbl_compareresult.config(text = "The perfect choice for a buddy: " + str(total))
    elif total >= 50:
        lbl_compareresult.config(text = "A reasonable choice for a buddy: " + str(total))
    elif total >= 30:
        lbl_compareresult.config(text = "Not the best choice for a buddy: " + str(total))
    elif total >= -50:
        lbl_compareresult.config(text = "A poor choice for a buddy " + str(total))
    else:
        lbl_compareresult.config(text = "The worst choice for a buddy "+ str(total))    
#------------end of statistics subroutines--------------
#-------------------------------------------------------


#---------------subroutines to show and hide frames-------------
def student():
    frm_question.grid_forget()
    frm_compare.grid_forget()
    frm_student.grid(row = 1, column = 0)

def question():
    frm_student.grid_forget()
    frm_compare.grid_forget()
    frm_question.grid(row = 1, column = 0)

def compare():
    frm_student.grid_forget()
    frm_question.grid_forget()
    frm_compare.grid(row =1, column = 0)
#--------------- end of subroutines to show and hide frames-------------
   
        
#--------connection to Event DB---------#
def create_connection(database):
    conn = sqlite3.connect(database) 
    return conn
#-----------end of database connections--------#

#-----------Login -----------------
def checkLogin(conn): #query the database
    username = txt_username.get()
    password = txt_password.get()
    cursor = conn.cursor()
    query = """SELECT Users.Password FROM Users
    WHERE Users.Username = '""" + username + "'"
    cursor.execute(query)
    result = cursor.fetchall() #return array
    dbPassword = "" #initialise
    if result: #if password returned
        dbPassword = str(result[0]) #choose first password
        dbPassword = dbPassword.replace("('", "") #remove characters
        dbPassword = dbPassword.replace("',)", "")
    if dbPassword == password and password != "": #passwords match
        frm_Login.pack_forget() #hide login
        frm_Image.pack_forget() #hide image
        frm_Main.pack() #open main window
        conn1.close() #close connection
#------end of Login Check--------------------#
    
def readFiles(): #subroutine to read the file
    textfile = open("Questions.txt", "r") #open file to read
    for item in textfile:
        activity.append(item) #add the text file items to an array
        
def queryResults(ID,student): #--------retrieve rows from profile------------
    global conn2, size

    #run SQL query 
    cursor = conn2.cursor()   
    query = "SELECT Answer FROM ProfileTBL WHERE StudentID = '" + ID + "';"
    cursor.execute(query) #READ the data from the file
    results = cursor.fetchall()
    #place the results in a listbox
    if student == 1:
        try:
            for n in range(size):
                temp = str(results[n])
                temp = temp[1:2]
                student1_scores[n] = int(temp)
                lst_student1.insert(n,results[n])
        except: #failed
            pass
    elif student == 2:
        try:
            for n in range(size):
                temp = str(results[n])
                temp = temp[1:2]
                student2_scores[n] = int(temp)
                lst_student2.insert(n,results[n])
        except: #failed attempt
            pass
            
def on_field_change(index, value, op): #--------combobox on_change-----
    #Extract StudentID
    temp_str = cbo_Student1.get()
    temp_int = temp_str.find(",")
    temp_str = temp_str[1:temp_int-1] #remove first '
    
    queryResults(temp_str, 0)

def on_grade_change(index, value, op): #--------compare grade combobox-----
    #whenever I chose something excute the function
    #Extract StudentID
    temp_str = cbo_Student1.get()
    temp_int = temp_str.find(",")
    temp_str = temp_str[1:temp_int-1] #remove first '
    
    queryResults(temp_str, 0)

def on_filter_change(index, value, op):
    global conn2
    temp_str = cbo_grade_C.get()
    populateCombo(conn2, temp_str)

def on_Q_filter_change(index, value, op):
    global conn2
    temp_str = cbo_grade_Q.get()
    populateCombo(conn2, temp_str)

def on_student1_change(index, value, op): #--------combobox on_change-----
    #Extract StudentID
    temp_str = cbo_Student1.get()
    temp_int = temp_str.find(",")
    temp_str = temp_str[1:temp_int-1] #remove first '
    queryResults(temp_str, 1)

def on_student2_change(index, value, op): #--------combobox on_change-----
    #Extract StudentID
    temp_str = cbo_Student2.get()
    temp_int = temp_str.find(",")
    temp_str = temp_str[1:temp_int-1] #remove first '
    #call the subroutine to show the list
    queryResults(temp_str, 2)

#-----------Save Student details-----------------
def addStudent(conn):#insert the database
    try:
        cursor = conn.cursor()

        studentID = ent_ID.get()
        firstname = ent_fName.get()
        surname = ent_sName.get()
        nationality = ent_Nation.get()
        grade = ent_Grade.get()
        #check if the primary key is entered
        if len(studentID) > 0: #ID is not blank
            if studentID.isnumeric(): #ID is a number
                query = """INSERT INTO StudentTBL
                (Studentid,Firstname,Surname,Nationality,Grade) VALUES
                ( '""" +studentID+ "', '"+firstname+ "', '"+surname+ "', '"+nationality+ "','"+grade+ "');"
                cursor.execute(query)
                conn.commit()
            else:
                messagebox.showwarning(title="Error", message="StudentID is a number")
        else:
            messagebox.showwarning(title="Error", message="StudentID is a required field")
        #clear entry boxes
        ent_ID.delete(0,END)
        ent_fName.delete(0,END)
        ent_sName.delete(0,END)
        ent_Nation.delete(0,END)
        ent_Grade.delete(0,END)
    except:
        pass
#------end ofSave Student Details--------------------#

#--------Delete Student details------------------
def deleteStudent(conn):

    cursor = conn.cursor()
    studentID = ent_ID.get()

    if len(studentID)>0:
        if studentID.isnumeric():
            query = "DELETE FROM StudentTBL WHERE studentid = '" + studentID + "';"
            cursor.execute(query)
            conn.commit()
        else:
            messagebox.showwarning(title="Error", message="StudentID is a number")
    else:
        messagebox.showwarning(title="Error", message="StudentID does not exist")
    #clear entry boxes
    ent_ID.delete(0,END)
    ent_fName.delete(0,END)
    ent_sName.delete(0,END)
    ent_Nation.delete(0,END)
    ent_Grade.delete(0,END)

#-------end of Delete Student Details-------------------#

###-------refresh tkinter------------#
##def refresh(self):
##    try:
##        self.destroy()
##        self.__init__()
##    except:
##        pass
###------end of refresh tkinter--------------#

#----------delete existing choices---------------
#if you have a student who completes the questions more than once, delete
def deleteAnswers(conn,ID):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM ProfileTBL WHERE StudentID = '" + ID + "';"
        cursor.execute(query)
        conn.commit()
    except:
        pass

def clearCompare():
    lst_student1.delete(0,'end')
    lst_student2.delete(0,'end')
    cbo_Student2.delete(0,'end')
    cbo_Student1.delete(0,'end')
#------------------Save student's choices ------------
def saveChoices(conn):
    global size #number of questions
    cursor = conn.cursor()
    try:
        #get student ID from combobox
        temp_ID = cbo_Student0.get()
        temp_int = temp_ID.find(",")
        temp_ID = temp_ID[1:temp_int-1] #remove first '
        deleteAnswers(conn,temp_ID) #call delete to remove existing answers
        #loop through all of the items
        for n in range(size):
            temp_num = ent1[n].get() # get the entry from textbox
            temp_num = int(temp_num)
            if temp_num >= 1 and temp_num <=10: #check for an entry
                query = """INSERT INTO ProfileTBL (StudentID, Answer)
                    VALUES ('"""+temp_ID +"','" +str(temp_num)+"');"
                cursor.execute(query)
                conn.commit()
            else:
                break
        #clear text boxes
        cbo_Student0.delete(0,END)
        for n in range(size):
            ent1[n].delete(0,END)
    except:
        pass
#------end of saveChoices--------------------#

def populateCombo(conn,value): #retrieve students
    arr_students = []
    cursor = conn.cursor()
    try:
        query = "SELECT StudentID, Firstname, Surname, Grade FROM StudentTBL WHERE Grade = " + value + " ORDER BY Grade, Surname Asc;"
        cursor.execute(query) #READ the data from the file
        results = cursor.fetchall()

        #place all of the items retrieved from the Category table into an array
        for NUM in range(len(results)):
            temp = str(results[NUM])
            temp = temp.replace('(','') #remove extra brackets from array
            temp = temp.replace(')','')
            arr_students.append(temp)
        cursor.close()
        # add the students into the combobox
        cbo_Student0.config(values = arr_students)
        cbo_Student1.config(values = arr_students)
        cbo_Student2.config(values = arr_students)
    except:
        pass
#------------MAIN CODE-------------------------#
    
#------------Display window------------#
root = Tk()
style = ttk.Style(root) #select the style
style.theme_use('classic')
root.title("Friend Finder") #Title in the window
root.geometry("800x800+250+150") #size and placement
root.configure(background = '#DDDDDD') #grey

#----------public variables----------#
activity = [] #dynamic array
readFiles() #read the activities
size = len(activity) #number of items
score = (1,2,3,4,5,6,7,8,9,10) #dropdown values
student1_scores = [0 for n in range(size)]
student2_scores = [0 for n in range(size)]
rank1 = [0 for n in range(size)] #fixed array
rank2 = [0 for n in range(size)] #fixed array
ent1 = [] #dynamic array
ent2 = [] #dynamic array
#---------------------------------

#create connection to test.db
if __name__ == '__main__': #start
    conn1 = create_connection("LoginDB.db")  #create connection to login database
    conn2 = create_connection("Student.db")

#--------------create frames--------------------
frm_Image = ttk.Frame(root)
frm_Image.pack()
frm_Login = ttk.Frame(root)
frm_Login.pack()
frm_Main = ttk.Frame(root)
# These frames will appear inside the Main frame
frm_buttons = ttk.Frame(frm_Main) # buttons
frm_buttons.grid(row = 0, column = 0)
frm_question = ttk.Frame(frm_Main) # questions
frm_student = ttk.Frame(frm_Main) # student frame
frm_compare = ttk.Frame(frm_Main)

#----------widgets for Login Frame-----------------------#
imgFriend = PhotoImage(file = "friend.png") #png or gif
lblImage = ttk.Label(frm_Image, image = imgFriend)
lblImage.pack()
lbl_username = ttk.Label(frm_Login, text = "Username ")
lbl_username.grid(row = 1, column = 0)
lbl_password = ttk.Label(frm_Login, text = "Password ")
lbl_password.grid(row = 2, column = 0)    
txt_username = ttk.Entry(frm_Login, width = 20)
txt_username.grid(row = 1, column = 1)
txt_password = ttk.Entry(frm_Login, show = "*",width = 20)
txt_password.grid(row = 2, column = 1)
btn_submit = ttk.Button(frm_Login, text = "Submit",
                        command = lambda: checkLogin(conn1))
btn_submit.grid(row = 3, column = 0, columnspan = 3)

#----------widgets for Main buttons Frame-----------------------#
btn_student = ttk.Button(frm_buttons, text = "Student",command = student)
btn_student.grid(row = 0, column = 0)
btn_question = ttk.Button(frm_buttons, text = "Question",command = question)
btn_question.grid(row = 0, column = 1)
btn_compare = ttk.Button(frm_buttons, text = "Compare", command = compare)
btn_compare.grid(row = 0, column = 3)

#----------widgets for student Frame-----------------------#
lbl_ID = ttk.Label(frm_student, text = "Student ID")
lbl_ID.grid(row = 0, column = 0)
ent_ID = ttk.Entry(frm_student, width = 20)
ent_ID.grid(row = 0, column = 1)
lbl_fName = ttk.Label(frm_student, text = "Firstname")
lbl_fName.grid(row = 1, column = 0)
ent_fName = ttk.Entry(frm_student, width = 20)
ent_fName.grid(row = 1, column = 1)
lbl_sName = ttk.Label(frm_student, text = "Surname")
lbl_sName.grid(row = 2, column = 0)
ent_sName = ttk.Entry(frm_student, width = 20)
ent_sName.grid(row = 2, column = 1)
lbl_Nation = ttk.Label(frm_student, text = "Nationality")
lbl_Nation.grid(row = 3, column = 0)
ent_Nation = ttk.Entry(frm_student, width = 20)
ent_Nation.grid(row = 3, column = 1)
lbl_Grade = ttk.Label(frm_student, text = "Grade")
lbl_Grade.grid(row = 4, column = 0)
ent_Grade = ttk.Entry(frm_student, width = 10)
ent_Grade.grid(row = 4, column = 1)
btn_addStudent = ttk.Button(frm_student, text = "Add Student", command = lambda: addStudent(conn2))
btn_addStudent.grid(row = 5, column = 0, columnspan=2)
btn_deleteStudent = ttk.Button(frm_student, text = "Delete Student", command = lambda: deleteStudent(conn2))
btn_deleteStudent.grid(row = 6, column =0, columnspan =2)
##btn_student_refresh = ttk.Button(frm_student, text = "Refresh", command = lambda: refresh(conn2))
##btn_student_refresh.grid(row =7, column =0, columnspan =2)

#----------widgets for compare Frame-----------------------#
lbl_Instr = ttk.Label(frm_compare, text = "Select two students to compare")
lbl_Instr.grid(row = 0, column = 0, columnspan = 2)
btn_compare_refresh = ttk.Button(frm_compare, text = "Refresh", command = clearCompare)
btn_compare_refresh.grid(row =5, column =1, columnspan =2)

#-------------Frame frmcompare---------------------
cbo_grade_filter = StringVar()
cbo_grade_filter.trace('w', on_filter_change) #call subroutine on change
lbl_gradelevel = ttk.Label(frm_compare, text = "Grade Level", font =("Arial","18"))
lbl_gradelevel.grid(row=1, column =0)
#combobox to display the grade level
cbo_grade_C = ttk.Combobox(frm_compare, textvar = cbo_grade_filter, values = [6,7,8,9,10,11])
cbo_grade_C.grid(row=1, column = 1)
cbo_grade_C.current(0)

str_compare1 = StringVar() #combobox variable
str_compare1.trace('w', on_student1_change) #call subroutine on change
lbl_Student1 = ttk.Label(frm_compare, text = "Student1", font =("Arial","18"))
lbl_Student1.grid(row=2, column = 0)
cbo_Student1 = ttk.Combobox(frm_compare, textvar = str_compare1, values = [])
cbo_Student1.grid(row=3, column = 0)

cbo_compare2 = StringVar() #combobox variable
cbo_compare2.trace('w', on_student2_change) #call subroutine on change
lbl_Student2 = ttk.Label(frm_compare, text = "Student2", font =("Arial","18"))
lbl_Student2.grid(row=2, column = 1)
cbo_Student2 = ttk.Combobox(frm_compare, textvar = cbo_compare2, values = [])
cbo_Student2.grid(row=3, column = 1)

lst_student1 = Listbox(frm_compare) #listbox
lst_student1.grid(row=4, column = 0)
lst_student2 = Listbox(frm_compare) #listbox
lst_student2.grid(row=4, column = 1)

btn_compare = ttk.Button(frm_compare, text = "Compare", command = rank)
btn_compare.grid(row = 5, column = 0, columnspan=2)

lbl_compareresult = ttk.Label(frm_compare, text = "Are you a good choice?", font=("Arial", "18"))
lbl_compareresult.grid(row=6, column = 0, columnspan = 2)

#-------------Question frame---------------------
cbo_var = StringVar() #combobox variable
cbo_var.trace('w', on_field_change) #when changed run subroutine
lbl_cinema = ttk.Label(frm_question, text = "Student details", font=("Arial", "18"))
lbl_cinema.grid(row=1, column = 0)
cbo_Student0 = ttk.Combobox(frm_question, textvar = cbo_var, values = [])
cbo_Student0.grid(row=1, column = 1)
lbl_cinema = ttk.Label(frm_question, text = "Grade", font =("Arial","18"))
lbl_cinema.grid(row=0, column =0)

cbo_compare1 = StringVar() #combobox variable
cbo_compare1.trace('w', on_student1_change)

str_filter = StringVar()
str_filter.trace('w', on_Q_filter_change)
cbo_grade_Q = ttk.Combobox(frm_question, textvar = str_filter, values = [6,7,8,9,10,11])
cbo_grade_Q.grid(row=0, column = 1)
cbo_grade_Q.current(0) #first item

populateCombo(conn2,6) #read students names for grade 6

#----------widgets for Question Frame-----------------------#
lbl_heading = ttk.Label(frm_question,
                        text = "Please score each activity out of 10",
                        font=("Arial", "18"))
lbl_heading.grid(row=2, column=0, columnspan=3)
#-----------entry---------------------
for n in range(size):
    lbl_cinema = ttk.Label(frm_question, text = activity[n],
                           font=("Arial", "18")) #labels
    lbl_cinema.grid(row=n+3, column = 0)
    ent1.append (ttk.Entry(frm_question, width=5)) # entry
    ent1[n].grid(row=n+3, column=1)

btn_saveChoices = ttk.Button(frm_question, text = "Save Choices", command = lambda: saveChoices(conn2))
btn_saveChoices.grid(row = size+3, column = 1, columnspan=3)
##btn_refresh = ttk.Button(frm_question, text = "Refresh", command = lambda: refresh(conn2))
##btn_refresh.grid(row =size+4, column =1, columnspan =3)
lbl_result = ttk.Label(frm_question, text = "", font=("Arial", "18"))
lbl_result.grid(row=size+4, column = 0, columnspan=4)

   
#---------------------------------
