        # Section 1: Setup



# ____________________________________________ SETUP ____________________________________________
    # Importing the necessary libraries
import tkinter as tk
from tkinter import *
from tkinter.ttk  import *
import tkinter.font as TkFont
import csv
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
import random
import time

    # Setting up the screen as a Tkinter Window
screen = Tk()
screen.title("Buddy-Finder")
screen.configure(background='black')

    # Adding Framework for multiple pages
Tabs = Notebook(screen, width=500)
Tabs.pack()

    # Defining Font Styles
headingfontstyle = TkFont.Font(family="MS Open Sans", size=70, weight='bold')
subheadingfontstyle = TkFont.Font(family="MS Open Sans", size=35, weight='bold')
subheadingfontstyle2 = TkFont.Font(family="MS Open Sans", size=60, weight='bold')
subheadingfontstyle3 = TkFont.Font(family="MS Open Sans", size=50, weight='bold')
subheadingfontstyle4 = TkFont.Font(family="MS Open Sans", size=30)
# ____________________________________________ END OF SETUP____________________________________________





# ____________________________________________ HOMEPAGE____________________________________________
    # Setting Up Homepage
Homepage = tk.Frame(Tabs, background='black')
Tabs.add(Homepage, text="Home Page")

    # Adding Text
tk.Label(Homepage, text='Buddy Finder',font=headingfontstyle,
         foreground='white', background='black').pack()

tk.Label(Homepage, text='''Being new to school can be hard, and
we at BuddyFinder want to lessen these
struggles to ensure that all new students
can have a great school experience.''', background='black', foreground='#CCD6DD').pack()

    # Adding the Image
tk.Label(Homepage, bitmap='homepage.png', background='black').pack()
# ____________________________________________ END OF HOMEPAGE____________________________________________





# ____________________________________________ WRITING THE CSV ____________________________________________
    # Listing the possible options for the drop down questions
options = {'1':['American Indian or Alaska Native','Asian','Black or African American','Hispanic or Latino','Native Hawaiian or other Pacific Islander','White','Other'],
           '2':['English','Math','Physics','Chemistry','Biology','Geography','History','Economics','Business Studies','Media','Computer Science','Art','Music','Drama'],
           '5':['Yes','No'],
           '6':['Stay at home', 'Go out with friends','Spend time with family'],
           '9':['Community Service Club', 'Technology Club', 'Science Club', 'Art Club', 'Business Club', 'Eco Club','Model United Nations', 'Debate', 'Tennis Team', 'Soccer Team', 'Volleyball Team', 'Athletics Team','Badminton Team', 'Swimming Team', 'Basketball Team', 'Cricket Team', 'Handball Team'],
           '8':['Politics/Social Issues', 'Sports', 'Art', 'Music', 'Technology', 'Food', 'Gaming', 'Culture', 'Travel','Science'],
           '7':['Math Extended', 'Math Standard', 'Physics', 'Chemistry', 'Biology', 'Economics', 'History', 'Geography','Business Studies', 'Digital Design', 'Media Studies', 'Music', 'Art', 'PHE', 'Product Design', 'French','Spanish', 'Islamic']}

    # Creating a dictionary of all the parameters that need to be saved for new and old students
fieldnames = {'New Student': ['username', 'name', 'password','Question 3','Question 4'],'Pre-existing Student': ['name', 'email','Question 3', 'Question 4']}

    # Adding in each option for drop down menus as seperate field to the fieldname dictionary
for z in ([1, 2, 5, 6, 7, 8, 9]):
    dat = options[str(z)]

    for c in dat:
        (fieldnames['New Student']).append(f'Question {z}_op{c}')
        (fieldnames['Pre-existing Student']).append(f'Question {z}_op{c}')

    # Choosing the correct file to open
mydict = {'newsdata.csv': 'New Student', 'oldsdata.csv': 'Pre-existing Student'}

    # Checking if the files exist already
try:
    f = open('newsdata.csv')
    g = open('oldsdata.csv')

    # If files do not already exist, creating new ones
except FileNotFoundError:
    for data in ['newsdata.csv', 'oldsdata.csv']:
        with open(data, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames[(mydict[data])])
            writer.writeheader()

        # Creating dummy data to the old students file for testing
    names = ['Dylan Brown', 'Bruno Cutler', 'John Stamos', 'Aria Tisch', 'Dudley Malfoy',
             'Lily Sky', 'Amber Hanks','Benedict Cumberbatch','Chris Evans',
             'Henley Evans','Al Gibson','Bobby Joseph','Jessica Night','Martin Oldman',
             'Shanaia Tweed','Walter Freeman','Georgetta Carasco','Joel Bonavita',
             'Fidela Mahlum','Rozella Crose','Allena Howells','Vivien Delker','Clementina Jessee',
             'Hayley Dundon','Margie Bang','Teofila Jasper','Maryann Jeffreys','Katerine Ceron',
             'Milda Fielding','Saundra Boster','Lasonya Rimmer','Raymonde Quinley','Elin Lando',
             'Nicolas Dammann','Sharita Mishler','Chuck Smail','Twanda Laseter','Julieann Perrett',
             'Ebonie Metz','Larhonda Eichler','Barry Laberge','Cornell Tynes','Inga Tonn',
             'Shante Carrozza','Angelia Fair','Ashlee Lindstedt','Candis Gapinski']

        # Generating random inputs for different questions
    for x in names:
        name = x
        email = ((x.replace(' ', '')).lower()) + '@gmail.com'
        q3 = random.randint(1, 5)
        q4 = random.randint(1, 5)
        studentdataentry = {'name': name, 'email': email,'Question 3': q3,
                            'Question 4': q4,}

        for num in (7, 8, 9):
            dat = options[str(num)]

            for item in dat:
                studentdataentry[f'Question {num}_op{item}'] = random.randint(0, 1)

        for num in (1,2,5,6):
            dat = options[str(num)]

            for item in dat:
                studentdataentry[f'Question {num}_op{item}'] = 0
            choice = random.choice(dat)
            studentdataentry[f'Question {num}_op{choice}'] = 1.5



            # Adding all the dummy data to the oldstudents database
        with open('oldsdata.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames['Pre-existing Student'])
            writer.writerow(studentdataentry)
# ____________________________________________ END OF WRITING THE CSV____________________________________________



            # Section 2: Defining Important Functions



# ____________________________________________ QUESTIONNAIRE FUNCTION____________________________________________
    # Defining the function that creates the form
def StudentsQuestionnaire():


#          -------------SETUP-------------
        # Creating a popup on the top level of the screen
    npopup = Toplevel(screen)
    npopup.geometry('553x421')
    npopup.title('Questionnaire')
    npopup.configure(background='black')

        # Adding a scrollbar to the popup winbdow by creating a canvas and frame within it
    def onFrameConfigure(canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))
    ncanvas = tk.Canvas(npopup, background='black')
    nspopup = tk.Frame(ncanvas, background='black')
    nscroll = tk.Scrollbar(npopup, orient="vertical", command=ncanvas.yview)
    ncanvas.configure(yscrollcommand=nscroll.set)
    ncanvas.pack(side="left", fill="both", expand=True)
    nscroll.pack(side=RIGHT, fill=Y)
    ncanvas.create_window((4, 4), window=nspopup, anchor="nw")
    nspopup.bind("<Configure>", lambda event, canvas=ncanvas: onFrameConfigure(canvas))



#          -------------INITIAL DATA-------------
    name = namev.get()
    Old_New = nqonv.get()

        # Deciding the format of form presented based on the type of student
    if Old_New == 'New Student':
        tk.Label(nspopup, text='New Students', font=headingfontstyle, foreground='white', background='black').pack()

            # New Students need to create a unique profile that can be accessed later
        tk.Label(nspopup, text='Create a Username for your Profile!', background='black',foreground='white').pack()
        usernamev = tk.Entry(nspopup, background='grey')
        usernamev.pack()

        tk.Label(nspopup, text='Create a password:', foreground='white', background='black').pack()
        passwordv = tk.Entry(nspopup, background='grey')
        passwordv.pack()

    elif Old_New == 'Pre-existing Student':
        tk.Label(nspopup, text='Old Students', font=headingfontstyle, foreground='white', background='black').pack()

            # Pre-existing students need a medium to be contacted by
        tk.Label(nspopup, text='Enter an email ID for students to contact you at!', foreground='white', background='black').pack()
        emailv = tk.Entry(nspopup, background='grey')
        emailv.pack()

        # Initial variables are saved extracted separately
    def saveinitials():
        global email, password, username
        if Old_New == 'New Student':
            username = usernamev.get()
            password = passwordv.get()

        elif Old_New == 'Pre-existing Student':
            email = emailv.get()

    tk.Button(nspopup, text='Confirm', command=saveinitials).pack()


#          -------------QUESTIONNAIRE-------------
        # This divides the initial data section to the section with actual questions
    tk.Label(nspopup, text='Questionnaire', foreground='white', background='black', font=subheadingfontstyle).pack()

        # Single-Select Drop Down Menu Questions
#Q1
    tk.Label(nspopup, text='What is your ethnicity?', foreground='white', background='black').pack()
    ethnicities= ['Select Answer','American Indian or Alaska Native','Asian','Black or African American','Hispanic or Latino','Native Hawaiian or other Pacific Islander','White','Other']
    nq1v = StringVar(nspopup)
    nq1v.set(ethnicities[0])
    nq1 = OptionMenu(nspopup, nq1v, *ethnicities)
    nq1.pack()
    tk.Label(nspopup, text='', background='black').pack()

#Q2
    tk.Label(nspopup, text='What is your favourite subject?', foreground='white', background='black').pack()
    subjects= ['Select Answer','English','Math','Physics','Chemistry','Biology','Geography','History','Economics','Business Studies','Media','Computer Science','Art','Music','Drama']
    nq2v = StringVar(nspopup)
    nq2v.set(subjects[0])
    nq2 = OptionMenu(nspopup, nq2v, *subjects)
    nq2.pack()
    tk.Label(nspopup, text='', background='black').pack()

        # Numerical Input Slider Questions
#Q3
    tk.Label(nspopup, text='On a scale from 1 to 5, how ambitious are you about school?', foreground='white',background='black').pack()
    nq3 = tk.Scale(nspopup, from_=1, to_=5, tickinterval=1, orient=HORIZONTAL, length=180)
    nq3.pack()
    tk.Label(nspopup, text='', background='black').pack()

#Q4
    tk.Label(nspopup, text='How many languages do you speak?', foreground='white', background='black').pack()
    nq4 = tk.Scale(nspopup, from_=1, to_=6, tickinterval = 1, orient=HORIZONTAL, length=180)
    nq4.pack()
    tk.Label(nspopup, text='', background='black').pack()

        # Single-select Option Questions
#Q5
    tk.Label(nspopup, text='Would you describe yourself as extrovrted?', foreground='white',background='black').pack()
    nq5 = StringVar()
    n5r1 = Radiobutton(nspopup, text='Yes!', value='Yes', variable=nq5).pack()
    n5r2 = Radiobutton(nspopup, text='No', value='No', variable=nq5).pack()
    tk.Label(nspopup, text='', background='black').pack()

#Q6
    tk.Label(nspopup, text='On a Friday night, you are most likely to...?', foreground='white', background='black').pack()
    nq6 = StringVar()
    n6r1 = Radiobutton(nspopup, text='Stay at home', value='Stay at home', variable=nq6).pack()
    n6r2 = Radiobutton(nspopup, text='Go out with friends', value='Go out with friends', variable=nq6).pack()
    n6r3 = Radiobutton(nspopup, text='Spend time with family', value='Spend time with family', variable=nq6).pack()
    tk.Label(nspopup, text='', background='black').pack()

        # Multi-Select Box Questions
#Q7
    tk.Label(nspopup, text='What subjects do you take at school currently?', foreground='white',background='black').pack()
    q7options = ['Math Extended', 'Math Standard','Physics','Chemistry','Biology','Economics','History','Geography','Business Studies','Digital Design','Media Studies','Music','Art','PHE','Product Design','French','Spanish','Islamic']
    nq7 = tk.Listbox(nspopup, selectmode='multiple',height=4)
    nq7.pack()
    for item in q7options: nq7.insert(END, item)
    def nq7f():
        global nq7v
            # Drop Down Menu responses are extracted immediately
        nq7v = ([nq7.get(sel) for sel in nq7.curselection()])

    Button(nspopup, text='Confirm Selection', command=nq7f).pack()
    tk.Label(nspopup, text='', background='black').pack()

#Q8
    tk.Label(nspopup, text='Which of these topics can you carry a conversation about?', foreground='white',background='black').pack()
    q8options = ['Politics/Social Issues', 'Sports', 'Art', 'Music', 'Technology', 'Food', 'Gaming','Culture','Travel','Science']
    nq8 = tk.Listbox(nspopup, selectmode='multiple', height=4)
    nq8.pack()
    for item in q8options: nq8.insert(END, item)

    def nq8f():
        global nq8v
            # Drop Down Menu responses are extracted immediately
        nq8v = ([nq8.get(sel) for sel in nq8.curselection()])

    Button(nspopup, text='Confirm Selection', command=nq8f).pack()
    tk.Label(nspopup, text='', background='black').pack()

#Q9
    dict = {'New Student': 'Which of these in-school organizations would you be interested in joining?', 'Pre-existing Student':'Which of these in-school organizations are you a part of?'}
    tk.Label(nspopup, text=dict[Old_New], foreground='white',background='black').pack()
    q9options =  ['Community Service Club','Technology Club','Science Club','Art Club','Business Club','Eco Club',
            'Model United Nations','Debate','Tennis Team','Soccer Team','Volleyball Team','Athletics Team','Badminton Team','Swimming Team','Basketball Team','Cricket Team','Handball Team']
    nq9 = tk.Listbox(nspopup, selectmode='multiple', height=4)
    nq9.pack()
    for item in q9options: nq9.insert(END, item)

    def nq9f():
        global nq9v
            # Drop Down Menu responses are extracted immediately
        nq9v = ([nq9.get(sel) for sel in nq9.curselection()])

    Button(nspopup, text='Confirm Selection', command=nq9f).pack()
    tk.Label(nspopup, text='', background='black').pack()


#          -------------SAVING THE ANSWERS-------------
        # Defining a function to extract current responses from each user input
    def saveanswers():

            # Defining the scope of the final variable to extend beyond the function
        global studentdataentry, final


            # Extracting the value of each individual question one-by-one
        q1 = nq1v.get()
        q2 = nq2v.get()
        q3 = nq3.get()
        q4 = nq4.get()
        q5 = nq5.get()
        q6 = nq6.get()

        if (q1 == 'Select Answer') or (q2 == 'Select Answer') or (q3 not in ['Yes','No']) or (q4 not in ['Stay at home','Go out with friends','Spend time with familt']):
            tk.Label(nspopup, text ='Oops, you have not answered all the questions. Please try again!', background = 'black', foreground = 'white').pack()

            # Compiling final user input as a dictionary
        if Old_New == 'New Student':
            studentdataentry = {'username': username, 'name': name, 'password': password,
                                'Question 3': q3, 'Question 4': q4}
        elif Old_New == 'Pre-existing Student':
            studentdataentry = {'name': name, 'email': email
                                ,'Question 3': q3, 'Question 4': q4}
        options = {
            '1': ['American Indian or Alaska Native', 'Asian', 'Black or African American', 'Hispanic or Latino',
                  'Native Hawaiian or other Pacific Islander', 'White', 'Other'],
            '2': ['English', 'Math', 'Physics', 'Chemistry', 'Biology', 'Geography', 'History', 'Economics',
                  'Business Studies', 'Media', 'Computer Science', 'Art', 'Music', 'Drama'],
            '5': ['Yes', 'No'],
            '6': ['Stay at home', 'Go out with friends', 'Spend time with family'],
            '9': ['Community Service Club', 'Technology Club', 'Science Club', 'Art Club', 'Business Club',
                  'Eco Club', 'Model United Nations', 'Debate', 'Tennis Team', 'Soccer Team', 'Volleyball Team',
                  'Athletics Team', 'Badminton Team', 'Swimming Team', 'Basketball Team', 'Cricket Team',
                  'Handball Team'],
            '8': ['Politics/Social Issues', 'Sports', 'Art', 'Music', 'Technology', 'Food', 'Gaming', 'Culture',
                  'Travel', 'Science'],
            '7': ['Math Extended', 'Math Standard', 'Physics', 'Chemistry', 'Biology', 'Economics', 'History',
                  'Geography', 'Business Studies', 'Digital Design', 'Media Studies', 'Music', 'Art', 'PHE',
                  'Product Design', 'French', 'Spanish', 'Islamic']}

            # Adding in responses from the drop-down menu questions
        collect = []
        for num in (1,2,5,6):
            if num == 7:
                collect = nq7v
            if num == 8:
                collect = nq8v
            if num == 9:
                collect = nq9v
            if num == 1:
                collect.append(q1)
            if num == 2:
                collect.append(q2)
            if num == 5:
                collect.append(q5)
            if num == 6:
                collect.append(q6)
            dat = options[str(num)]

            for item in dat:
                    # Creating new columns for each possible response with binary data
                if item in collect:
                    studentdataentry[f'Question {num}_op{item}'] = 1.5
                elif item not in collect:
                    studentdataentry[f'Question {num}_op{item}'] = 0

        for num in (7, 8, 9):
            if num == 7:
                collect = nq7v
            if num == 8:
                collect = nq8v
            if num == 9:
                collect = nq9v
            dat = options[str(num)]

            for item in dat:
                    # Creating new columns for each possible response with binary data
                if item in collect:
                    studentdataentry[f'Question {num}_op{item}'] = 1
                elif item not in collect:
                    studentdataentry[f'Question {num}_op{item}'] = 0



            # Opening the correct file based on the type of student
        mydict2 = {'New Student':'newsdata.csv','Pre-existing Student':'oldsdata.csv'}

            # Adding the current row to the file
        with open (mydict2[Old_New], 'a') as file:
            writer = csv.DictWriter(file, fieldnames=(fieldnames[Old_New]))
            writer.writerow(studentdataentry)


            # Confirmation message presented to user if all parts of function are completed
        tk.Label(nspopup, text='', background='black').pack()
        finals = {'New Student':'Your Entry was Submitted! Login to the matches page to see your matches', 'Pre-existing Student':'Your Entry was Submitted! Now sit tight, and wait for new students to contact you!','':''}
        tk.Label(nspopup, text = (finals[Old_New]), background='black',foreground='white').pack()
        tk.Label(nspopup, text='', background='black').pack()

    # Button to extract all current responses
    Button(nspopup, text="Save My Answers!", command=saveanswers).pack()
# ____________________________________________ END OF QUESTIONNAIRE FUNCTION____________________________________________





# ____________________________________________ MATCHING FUNCTION____________________________________________
    # Defining the function that creates the results
def getmatches():

        # Defining the scope of an important variable
    global index

        # Using pandas to read both the files
    new = pd.read_csv('newsdata.csv', index_col='username')
    old = pd.read_csv('oldsdata.csv')

        # Extracting both user login input
    user = userna.get()
    pword = password2.get()

        # Checking if user account exists
    if user in new.index:

            # Extracting the row with user data
        myrow = new.loc[user]

            # Checking if the password entered is correct
        if myrow['password'] == pword:

                # Setting up a popup window on the top level of the screen
            name = myrow['name']
            mpopup = Toplevel(screen)
            mpopup.geometry('553x421')
            mpopup.title(f"{name}'s Matches")
            mpopup.configure(background='black')

                # Creating a heading on the popup window
            tk.Label(mpopup, text=f"Your Matches", background='black',foreground ='white',font=subheadingfontstyle2).pack()
            tk.Label(mpopup, text='', background='black').pack()
            tk.Label(mpopup, text='', background='black').pack()

            matchframe = tk.Frame(mpopup, background='#545454')
            matchframe.pack()



                # Creating numpy arrays of the usable data from both databases
            myrow = (((myrow).to_frame()).T)
            useddata = old.iloc[:,2:]
            myrow = myrow.iloc[:,2:]

            mylist = []

                # Only extracting the values chosen by the new student
            for x in range(28):
                mylist.append(True)

            for x in ((list(myrow))[28:]):
                z = ((myrow.iloc[0])[x]) == 1
                mylist.append(z)

            useddata = np.array(useddata.iloc[:,mylist])
            myrow = (np.array(myrow.iloc[:,mylist]))

                # Creating a K Nearest Neighbours Algorithm using Sklearn
            algorithm = NearestNeighbors(n_neighbors = 5, algorithm='auto')
                # Fitting the K Nearest Neighbors algorithm to the Old Students Data
            algorithm.fit(useddata)
                # Extracting the 5 nearest neighbours of the Account into a list
            rawmatches = list((algorithm.kneighbors(myrow, return_distance=False))[0])
                # Taking the first value of the output list (highest correlation)
            index = 0
            datath = rawmatches[index]
                # Opening the row with highest correlation
            chosen_row = old.iloc[datath,:]

                # Displaying the Name and Email ID of the matches on the page
            tk.Label(matchframe, text='',background='#545454').grid(row=1, column=2)
            tk.Label(matchframe, text='', background='#545454').grid(row=3, column=2)
            Name_l = tk.Label(matchframe, text=(chosen_row.loc['name']), foreground='#EDE7E7',background='#545454',font=subheadingfontstyle3 )
            Name_l.grid(column=2, row=2)
            Email_l = tk.Label(matchframe, text=(chosen_row.loc['email']), foreground='white', background='#E5B8A5',font=subheadingfontstyle4)
            Email_l.grid(column=2, row=4)
            tk.Label(matchframe, text='', background = '#545454').grid(column = 2, row = 5)

                # Defining Functions to scroll through the 5 data entries with most correlation
            def next():
                global index
                if index == 4:
                    index = 0
                else:
                    index += 1
                datath = rawmatches[index]

                chosen_row = old.iloc[datath, :]
                Name_l.config(text=chosen_row.loc['name'])
                Email_l.config(text=chosen_row.loc['email'])

            def previous():
                global index
                if index == 0:
                    index = 4
                else:
                    index -= 1
                datath = rawmatches[index]
                chosen_row = old.iloc[datath, :]
                Name_l.config(text=chosen_row.loc['name'])
                Email_l.config(text=chosen_row.loc['email'])

                # Creating the buttons to allow users to scroll through top 5 matches
            tk.Button(matchframe, text='<', bg='#E5B8A5', command=previous).grid(column=1, row=6)
            tk.Button(matchframe, text='>', bg='#E5B8A5',command=next).grid(column=3, row=6)
            tk.Label(matchframe, text='', background='#545454').grid(row=7, column=2)

            # Printing error message if password is wrong
        else:
            tk.Label(Your_Matches, text=f'Your Password is Incorrect, Please try again!', background='Black', foreground='white').pack()

        # Printing error message if account does not exist
    else:
        tk.Label(Your_Matches, text='''Sorry, your account does not exist,
        Go to the Questionnaire Page to create one!''', foreground='white', background='black').pack()
# ____________________________________________ END OF MATCHING FUNCTION____________________________________________



        # Section 3: Creating Important Pages



# ____________________________________________ FORMSPAGE____________________________________________
    # Setting up the Form Page
Formspage = tk.Frame(Tabs, background='black')
Tabs.add(Formspage, text="Take the Questionnaire")

    # Adding text to the Form Page
tk.Label(Formspage, text='Questionnaire',font=subheadingfontstyle2, foreground='white', background='black').pack()
tk.Label(Formspage, text='''Answer a series of questions about 
yourself, and our algorithm will find people 
who have the most in common with you! ''', background='black', foreground='#CCD6DD').pack()

tk.Label(Formspage, text='Start filling it out!', foreground='#E5B8A5', background='black', font=subheadingfontstyle).pack()

    # Collecting Basic User Input
#Name
tk.Label(Formspage, text='What is your name?', foreground='white', background='black').pack()
namev = tk.Entry(Formspage, background='grey')
namev.pack()
tk.Label(Formspage, text='', background='black').pack()

#Old or New
tk.Label(Formspage, text='Are you a new student or a pre-existing student?', foreground='white', background='black').pack()
new_old = ['','New Student','Pre-existing Student']
nqonv = StringVar(Formspage)
nqonv.set(new_old[0])
nqon = OptionMenu(Formspage, nqonv, *new_old)
nqon.pack()

tk.Label(Formspage, text='', background='black').pack()

#Button to start questionnaire
Button(Formspage, text="Start the Questionnaire!", command=StudentsQuestionnaire).pack()
tk.Label(Formspage, text='', background='black').pack()
# ____________________________________________ END OF FORMSPAGE____________________________________________





# ____________________________________________ RESULTS PAGE ____________________________________________
    # Setting up the page
Your_Matches= tk.Frame(Tabs,background='black')
Tabs.add(Your_Matches, text="Your Matches")
tk.Label(Your_Matches, text='Matches',font=headingfontstyle, foreground='white', background='black').pack()



    # Allowing new users to log in
#Username
tk.Label(Your_Matches, text='''Username:''', foreground='white', background='black').pack()
userna = tk.Entry(Your_Matches, background='grey')
userna.pack()
tk.Label(Your_Matches, text='',background='black').pack()

#Password
tk.Label(Your_Matches, text='''Password:''', foreground='white', background='black').pack()
password2 = tk.Entry(Your_Matches, background='grey')
password2.pack()
tk.Label(Your_Matches, text='',background='black').pack()

#Button to get matches
Button(Your_Matches, text='Get Matches!',command=getmatches).pack()
# ____________________________________________ RESULTS PAGE ____________________________________________


screen.mainloop()









