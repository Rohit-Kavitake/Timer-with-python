#This a very basic timer program made using python programming
#Author:- Rohit Kavitake


#Importing modules
from time import sleep,ctime
import webbrowser
import random


#Listof URL's to play
#make sure your song url is present in this list to play as timer tone
url = ("https://www.youtube.com/watch?v=zzwRbKI2pn4","https://www.youtube.com/watch?v=oBfRJplcSuk","https://www.youtube.com/watch?v=13cHnQ1Suj8","https://www.youtube.com/watch?v=7wtfhZwyrcc","https://www.youtube.com/watch?v=gOsM-DYAEhY","https://www.youtube.com/watch?v=HhjHYkPQ8F0","https://www.youtube.com/watch?v=g6oZhAk_wKY")

#convertig hours and minutes to seconds
def timetosec(h,m,s):
    sec = 3600 * h + 60 * m + s
    return sec


#part of presentation
def line():
    print("--------------------------------------------------------------------------------")


#main Timer Function
def main():
    line()
    print("Welcome to the Timer program")
    line()
    print("The current Date and time is {}".format(ctime()))
    line()
    run = input("Do you want to set timer?(y/n)")
    line()
    if (run == "y"):
        h = int(input("Hours:"))
        m = int(input("Minutes:"))    #Taking timer input
        s = int(input("Seconds:"))
        line()
        confirm = input("Set alarm for {}hours {}minutes {} seconds?(y/n):".format(h,m,s))
        line()
        if confirm == "y":
            print("Alarm set for {}hours {}minutes {} seconds.".format(h,m,s))
            sleep(timetosec(h,m,s))
            webbrowser.open_new(random.choice(url))
            line()
            stop = input("Stop the timer?(y/n):")
            line()
            if stop == "y":
                quit()
            else:
                main()
    else:

        main()

#execution of main function
main()
