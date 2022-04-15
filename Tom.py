# Made by: Pythonista, Visual Studio Code
# Creators: Suri
# Checkers: Suri
# Socialized: False
# Version: 1.0.1

#Import the Basic Modules. Can be found in the same folder
import Classes
import Functions
import sys
#Importing the python in-modules
import datetime
import time



print("<<< Please login")
Username, Password = Functions.login()
    
        
while True:
    #Printing Menu
    Functions.Menu()
    
    #Ask the need of the User
    Entry = Functions.Enter("What is your need")
    if Entry == "1":
        while True:
            #Cauculation starting
            Functions.Cauculation_menu()
            Paw = Functions.Enter("Which one are you needing for")

            #Keep out any other choices
            if Paw not in ["1", "2", "3", "4", "5", "Quit"]:
                print("*  No such way of Cauculating. ")
            else:
                if Paw != "Quit":
                    a = float(Functions.Enter("A"))
                    b = float(Functions.Enter("B"))
                    if Paw == "1":
                        print("*   Answer: "+str(Classes.Cauculation.add(a, b)))
                    if Paw == "2":
                        print("*   Answer: "+str(Classes.Cauculation.subtract(a, b)))
                    if Paw == "3":
                        print("*   Answer: "+str(Classes.Cauculation.mutiply(a, b)))
                    if Paw == "4":
                        print("*   Answer: "+str(Classes.Cauculation.divide(a, b)))
                    if Paw == "5":
                        print("*   Answer: "+str(Classes.Cauculation.power(a, b)))
                    print("______________________________________________________________________________________")
                else:
                    break
    elif Entry == "2":
        while True:
            Choice = input("*   Do you want to add question or have ask a Question? (Ask=0, Add=1)")
            if Choice == "0":
                print("*   Welcome yo question answer. What is your question?")
                Question = input("*   ").lower()
                Questions = {}
                Question_list = []
                with open(Username+".txt", "r") as Question_file:
                    for line in Question_file:
                        line = line.rstrip('\n')
                        Current_question, Current_ancwer = line.split("/")
                        Question_list.append(Current_question)
                        Questions[Current_question] = Current_ancwer                        
                #The questions Dictionary in the questions are In the txt files
                if Question == "time":
                    print("*   "+Functions.get_time())
                
                    #The get_time function must be run mutiple times to be always the newest time.
                else:
                    if Question in Questions:
                        print(Questions[Question])
                    else:
                        print("*   Sorry but no such question exsits.")
            elif Choice == "1":
                pass
            elif Choice == "Quit":
                break
            else:
                print("*   There is no such command")
    elif Entry == "3":
        #The gaming Part
        Functions.Game_menu()
        Game_mode = int(input("*   Which game do you want to play(Input numbers): "))
        if Game_mode == 1:
            import Guess_the_word
            continue
    elif Entry == "4":
        #in the file will be "Problem/Title/Username" and new line
        print("*   What is the problem?")
        Problem = input("*   ")
        print("*   What is the title?")
        Title = input("*   ")
        with open("Reports.txt", "a") as Reports:
            Reports.write(Problem+'/'+Title+'/'+Username+'\n')
        
            
    elif Entry == "5":
        print("*   Version: 1.0.0")
        print("*   Creator: Yusuli")
    elif Entry == "Quit":
        Functions.quit()
    else:
        print("*   No such command")
    #Draw a big line so the User won't mistaken the entry before
    print("""
_______________________________________________________________________________________________________________________
    """)
