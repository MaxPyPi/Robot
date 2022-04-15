import datetime
import sys
import time


def quit():
    time.sleep(10)
    sys.exit()
    

def login():
    """
    This function will make the user login
    """
    while True:
        User_dict = {"Admin":"AliceFym5", "Suli":"suli@2008", "Bluesailor":"bluesailor@2008", "Yuhan":"yuhan@2008", "MaoMao":"MaoMao@2008"}
        Username_list = ["Admin", "Suli", "Bluesailor", "Yuahn", "MaoMao"]
        Username = input("<   Your username: ")
        if Username in Username_list:
            Password = input("<   Your password: ")
            if Password == User_dict[Username]:
                print("*   Logged in :)")
                return Username, Password
                break
            else:
                print("<   Password error")
        print("<   Username error")
        
        



def Menu():
    """
    The function of the main menu.
    """

    Item = """
    -----------Menu-----------
    *   1.Cauculator         *
    *   2.Question Answer    *
    *   3.Gaming             *
    *   4.Report             *
    *   5.About me           *
    --------------------------
    # Type Quit in every place
    # To Exit
    """
    print(Item)


def Game_menu():
    """
    The function of the gaming menu
    """
    Item = """
    -------Gaming  Menu-------
    *   1.Nine lives         *
    --------------------------
    """
    print(Item)


def Enter(info):
    Item = input("*   "+info+": ")
    return Item


def Cauculation_menu():
    Item = """
    ----Cauculation Menu----
    *   1.Addition         *
    *   2.Subtraction      *
    *   3.Mutiply          *
    *   4.Divide           *
    *   5.Power            *
    ------------------------
    """
    print(Item)
    

def get_time():
    date_format = '%Y-%m-%d %H:%M'
    now = datetime.datetime.now()
    date_str = now.strftime(date_format)
    return date_str
