import time
import Tkinter

# Have to incorporate weekly tracker, load total pomodoros from file and reset weekly
# Add in sounds for starting/completing work and breaks
# Implement a pause function
# Make executable GUI
# In GUI include Start and pause/resume buttons, countdown timer, number of pomodoros, working/short/long break info
# Make settings button/drop down where you can adjust the times
# keybinds?


# Maybe sleep every second and run if pause variable isn't true, button toggles variable between true and false

# Keep track of completed pomodoros and goals
completedpomodoros=0
totalpomodoros=0
pomodorogoal=30

# Working/break times for adjustment
pomodorotime=25
shortbreaktime=5
longbreaktime=15

# Boolean variables for current state
working=True
shortbreak=False
longbreak=False
pause=False

# Main method to run the program
def run():
    global completedpomodoros
    global totalpomodoros
    global pomodorogoal
    global pomodorotime
    global shortbreaktime
    global longbreaktime
    global working
    global shortbreak
    global longbreak
    global pause

    print "Starting work session..."
    print "So far, have completed " + str(completedpomodoros) + " of goal of " + str(pomodorogoal) + " pomodoros for the week"

    while 0==0:
        pomodorotimeleft=pomodorotime
        while working:
            print str(pomodorotimeleft) + " minutes left to work"
            time.sleep(15)
            pomodorotimeleft-=.25
            if pomodorotimeleft==0:
                working=False
                completedpomodoros+=1
                totalpomodoros+=1
                pomodorosleft=pomodorogoal-totalpomodoros
                print "Pomodoro completed. " + str(completedpomodoros) + " pomodoros have been completed this session, for a total productive time of " + str((completedpomodoros*pomodorotime)) + " minutes"
                print str(totalpomodoros) + " pomodoros have been completed this week, for a total of " + str((totalpomodoros*pomodorotime)) + " productive minutes"
                print "Currently " + str((pomodorogoal-totalpomodoros)) + " pomodoros away from reaching this week's goal of " + str(pomodorogoal) + " pomodoros"
                if completedpomodoros%4==0:
                    longbreak=True
                    longbreaktimeleft=longbreaktime
                    print "Taking a long break of " + str(longbreaktime) + " minutes"
                else:
                    shortbreak=True
                    shortbreaktimeleft=shortbreaktime
                    print "Taking a short break of " + str(shortbreaktime) + " minutes"

        while shortbreak:
            print str(shortbreaktimeleft) + " minutes left on short break"
            time.sleep(15)
            shortbreaktimeleft-=.25
            if shortbreaktimeleft==0:
                shortbreak=False
                working=True

        while longbreak:
            print str(longbreaktimeleft) + "minutes left on long break"
            time.sleep(15)
            longbreaktimeleft-=.25
            if longbreaktimeleft==0:
                longbreak=False
                working=True

run()

'''
# Call this when pause=True to sleep until pause=False
def pause():
    global pause
    if pauseB["text"]=="Pause":
        pauseB.config(text="Resume")
        pause=False
    elif pauseB["text"]=="Resume":
        pauseB.config(text="Pause")
        pause=True




# Making GUI

window=Tkinter.Tk()
window.title('Pomodoro Timer')
startB = Tkinter.Button(window,text="Start", command = run)
startB.pack()

pauseB = Tkinter.Button(window,text="Pause", command = pause)
pauseB.pack()

window.mainloop()
'''