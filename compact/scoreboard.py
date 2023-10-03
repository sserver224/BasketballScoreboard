from tkinter import *
from tkinter.ttk import *
import pygame
import time, os
from tkinter import messagebox
def grp(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
scoreboard=Tk()
scoreboard.minutes=20
scoreboard.config(bg='black')
scoreboard.grid()
scoreboard.clockDigit1=PhotoImage(file=grp('yellow-'+str(scoreboard.minutes)[0]+'.gif'))
scoreboard.clockDigit2=PhotoImage(file=grp('yellow-'+str(scoreboard.minutes)[1]+'.gif'))
scoreboard.clockDigit3=PhotoImage(file=grp('yellow-0.gif'))
scoreboard.clockDigit4=PhotoImage(file=grp('yellow-0.gif'))
scoreboard.img=Label(scoreboard, background='black', image=scoreboard.clockDigit1)
scoreboard.img1 = Label(scoreboard, background='black', image=scoreboard.clockDigit2)
scoreboard.img2 = Label(scoreboard, background='black', image=scoreboard.clockDigit3)
scoreboard.img3 = Label(scoreboard, background='black', image=scoreboard.clockDigit4)
scoreboard.img.grid(column=1, row=1)
scoreboard.img1.grid(column=2, row=1)
scoreboard.img2.grid(column=4, row=1)
scoreboard.img3.grid(column=5, row=1)
scoreboard.scoreDigit1=PhotoImage(file=grp('.gif'))
scoreboard.scoreDigit2=PhotoImage(file=grp('.gif'))
scoreboard.scoreDigit3=PhotoImage(file=grp('red-0.gif'))
scoreboard.scoreDigit4=PhotoImage(file=grp('.gif'))
scoreboard.scoreDigit5=PhotoImage(file=grp('.gif'))
scoreboard.scoreDigit6=PhotoImage(file=grp('red-0.gif'))
scoreboard.img4=Label(scoreboard, background='black', image=scoreboard.scoreDigit1)
scoreboard.img5 = Label(scoreboard, background='black', image=scoreboard.scoreDigit2)
scoreboard.img6 = Label(scoreboard, background='black', image=scoreboard.scoreDigit3)
scoreboard.img7 = Label(scoreboard, background='black', image=scoreboard.scoreDigit4)
scoreboard.img8 = Label(scoreboard, background='black', image=scoreboard.scoreDigit5)
scoreboard.img9 = Label(scoreboard, background='black', image=scoreboard.scoreDigit6)
scoreboard.img4.grid(column=0, row=3)
scoreboard.img5.grid(column=1, row=3)
scoreboard.img6.grid(column=2, row=3)
scoreboard.img7.grid(column=4, row=3)
scoreboard.img8.grid(column=5, row=3)
scoreboard.img9.grid(column=6, row=3)
scoreboard.periodDigit=PhotoImage(file=grp('yellow-1.gif'))
scoreboard.periodDigit= scoreboard.periodDigit.zoom(25) #with 250, I ended up running out of memory
scoreboard.periodDigit = scoreboard.periodDigit.subsample(32)
scoreboard.img10 = Label(scoreboard, background='black', image=scoreboard.periodDigit)
scoreboard.img10.grid(column=3, row=3)
def update_period():
    scoreboard.periodDigit=PhotoImage(file=grp('yellow-'+str(scoreboard.period)+'.gif'))
    scoreboard.periodDigit= scoreboard.periodDigit.zoom(25) #with 250, I ended up running out of memory
    scoreboard.periodDigit = scoreboard.periodDigit.subsample(32)
    scoreboard.img10.config(image=scoreboard.periodDigit)
    periodControl.config(text=str(scoreboard.period))
    controlpanel.update_idletasks()
    scoreboard.update_idletasks()
def update_score():
    if scoreboard.homeScore>99:
        scoreboard.scoreDigit1=PhotoImage(file=grp('red-'+str(scoreboard.homeScore)[0]+'.gif'))
        scoreboard.scoreDigit2=PhotoImage(file=grp('red-'+str(scoreboard.homeScore)[1]+'.gif'))
        scoreboard.scoreDigit3=PhotoImage(file=grp('red-'+str(scoreboard.homeScore)[2]+'.gif'))
    elif scoreboard.homeScore>9:
        scoreboard.scoreDigit1=PhotoImage(file=grp('.gif'))
        scoreboard.scoreDigit2=PhotoImage(file=grp('red-'+str(scoreboard.homeScore)[0]+'.gif'))
        scoreboard.scoreDigit3=PhotoImage(file=grp('red-'+str(scoreboard.homeScore)[1]+'.gif'))
    else:
        scoreboard.scoreDigit1=PhotoImage(file=grp('.gif'))
        scoreboard.scoreDigit2=PhotoImage(file=grp('.gif'))
        scoreboard.scoreDigit3=PhotoImage(file=grp('red-'+str(scoreboard.homeScore)+'.gif'))
    if scoreboard.guestScore>99:
        scoreboard.scoreDigit4=PhotoImage(file=grp('red-'+str(scoreboard.guestScore)[0]+'.gif'))
        scoreboard.scoreDigit5=PhotoImage(file=grp('red-'+str(scoreboard.guestScore)[1]+'.gif'))
        scoreboard.scoreDigit6=PhotoImage(file=grp('red-'+str(scoreboard.guestScore)[2]+'.gif'))
    elif scoreboard.guestScore>9:
        scoreboard.scoreDigit4=PhotoImage(file=grp('.gif'))
        scoreboard.scoreDigit5=PhotoImage(file=grp('red-'+str(scoreboard.guestScore)[0]+'.gif'))
        scoreboard.scoreDigit6=PhotoImage(file=grp('red-'+str(scoreboard.guestScore)[1]+'.gif'))
    else:
        scoreboard.scoreDigit4=PhotoImage(file=grp('.gif'))
        scoreboard.scoreDigit5=PhotoImage(file=grp('.gif'))
        scoreboard.scoreDigit6=PhotoImage(file=grp('red-'+str(scoreboard.guestScore)+'.gif'))
    scoreboard.img4.config(image=scoreboard.scoreDigit1)
    scoreboard.img5.config(image=scoreboard.scoreDigit2)
    scoreboard.img6.config(image=scoreboard.scoreDigit3)
    scoreboard.img7.config(image=scoreboard.scoreDigit4)
    scoreboard.img8.config(image=scoreboard.scoreDigit5)
    scoreboard.img9.config(image=scoreboard.scoreDigit6)
    scoreboard.update_idletasks()
def update_clock(self):
    if scoreboard.minutes>0:
        timecolon.config(text=':')
        if scoreboard.minutes>9:
            if scoreboard.seconds>9:
                self.clockDigit1=PhotoImage(file=grp('yellow-'+str(scoreboard.minutes)[0]+'.gif'))
                self.clockDigit2=PhotoImage(file=grp('yellow-'+str(scoreboard.minutes)[1]+'.gif'))
                self.clockDigit3=PhotoImage(file=grp('yellow-'+str(scoreboard.seconds)[0]+'.gif'))
                self.clockDigit4=PhotoImage(file=grp('yellow-'+str(scoreboard.seconds)[1]+'.gif'))
            else:
                self.clockDigit1=PhotoImage(file=grp('yellow-'+str(scoreboard.minutes)[0]+'.gif'))
                self.clockDigit2=PhotoImage(file=grp('yellow-'+str(scoreboard.minutes)[1]+'.gif'))
                self.clockDigit3=PhotoImage(file=grp('yellow-0.gif'))
                self.clockDigit4=PhotoImage(file=grp('yellow-'+str(scoreboard.seconds)+'.gif'))
        else:
            if scoreboard.seconds>9:
                self.clockDigit1=PhotoImage(file=grp('.gif'))
                self.clockDigit2=PhotoImage(file=grp('yellow-'+str(scoreboard.minutes)+'.gif'))
                self.clockDigit3=PhotoImage(file=grp('yellow-'+str(scoreboard.seconds)[0]+'.gif'))
                self.clockDigit4=PhotoImage(file=grp('yellow-'+str(scoreboard.seconds)[1]+'.gif'))
            else:
                self.clockDigit1=PhotoImage(file=grp('.gif'))
                self.clockDigit2=PhotoImage(file=grp('yellow-'+str(scoreboard.minutes)+'.gif'))
                self.clockDigit3=PhotoImage(file=grp('yellow-0.gif'))
                self.clockDigit4=PhotoImage(file=grp('yellow-'+str(scoreboard.seconds)+'.gif'))
    else:
        timecolon.config(text='.')
        if scoreboard.seconds>9:
            self.clockDigit1=PhotoImage(file=grp('yellow-'+str(scoreboard.seconds)[0]+'.gif'))
            self.clockDigit2=PhotoImage(file=grp('yellow-'+str(scoreboard.seconds)[1]+'.gif'))
            self.clockDigit3=PhotoImage(file=grp('yellow-'+str(scoreboard.tenths)+'.gif'))
            self.clockDigit4=PhotoImage(file=grp('.gif'))
        else:
            self.clockDigit1=PhotoImage(file=grp('.gif'))
            self.clockDigit2=PhotoImage(file=grp('yellow-'+str(scoreboard.seconds)+'.gif'))
            self.clockDigit3=PhotoImage(file=grp('yellow-'+str(scoreboard.tenths)+'.gif'))
            self.clockDigit4=PhotoImage(file=grp('.gif'))
    self.img.config(image=scoreboard.clockDigit1)
    self.img1.config(image=scoreboard.clockDigit2)
    self.img2.config(image=scoreboard.clockDigit3)
    self.img3.config(image=scoreboard.clockDigit4)
    if scoreboard.seconds<10 and scoreboard.minutes>0:
            if scoreboard.minutes<10:
                    clockLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
            else:
                    clockLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
    elif scoreboard.minutes==0:
            if scoreboard.seconds<10:
                    clockLabel.config(text='  '+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
            else:
                    clockLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
    else:
            if scoreboard.minutes<10:
                    clockLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
            else:
                    clockLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
    scoreboard.update_idletasks()
scoreboard.title('Display Screen-Scorely Compact ©sserver')
setseconds=StringVar()
setminutes=StringVar()
timecolon=Label(scoreboard, text=':', foreground='white', background='black', font=('Century Gothic', 200))
timecolon.grid(column=3, row=1)
homeNameLabel=Label(scoreboard, text="HOME", background='black', foreground='orange')
homeNameLabel.place(x=0, y=320)
homePossLabel=Label(scoreboard, text="<<<", background='black', foreground='#190000')
homePossLabel.grid(column=0, row=1)
guestNameLabel=Label(scoreboard, text="GUEST", background='black', foreground='orange')
guestNameLabel.place(x=1000, y=320)
guestPossLabel=Label(scoreboard, text=">>>", background='black', foreground='#190000')
guestPossLabel.grid(column=6, row=1)
homePossLabel.config(font=('Segoe UI', 75))
guestPossLabel.config(font=('Segoe UI', 75))
scoreboard.autoHorn=True
periodNameLabel=Label(scoreboard, text='PERIOD', font=('Century Gothic', 75), background='black', foreground='white')
periodNameLabel.grid(column=3, row=2)
scoreboard.seconds=0
scoreboard.tenths=0
scoreboard.poss=0
endTime=None
scoreboard.resizable(False, False)
scoreboard.homeFouls=0
scoreboard.guestFouls=0
scoreboard.homeBonus=False
scoreboard.guestBonus=False
scoreboard.homeScore=0
scoreboard.guestScore=0
scoreboard.period=1
pygame.mixer.init()
channel=pygame.mixer.find_channel()
scoreboard.fast=False
scoreboard.clockState=False
homeNameLabel.config(font=('Century Gothic', 75))
guestNameLabel.config(font=('Century Gothic', 75))
scoreboard.homeName='HOME'
scoreboard.guestName='GUEST'
controlpanel=Tk()
controlpanel.title('Control Panel-Scorely Compact ©sserver')
def buzzer():
    sound=pygame.mixer.Sound(grp('Buzzer.wav'))
    channel.play(sound)
def horn():
    sound=pygame.mixer.Sound(grp('Horn.wav'))
    channel.play(sound)
def start_buzzer_loop(c):
    sound=pygame.mixer.Sound(grp('BuzzerLoop.wav'))
    channel.play(sound, -1)
def stop_buzzer_loop(c):
    channel.stop()
def doSomething():
    if not scoreboard.clockState:
        controlpanel.destroy()
        scoreboard.destroy()
scoreboard.protocol('WM_DELETE_WINDOW', doSomething)
controlpanel.protocol('WM_DELETE_WINDOW', doSomething)
def start_time():
        global endTime
        if scoreboard.clockState:
            timeLeft=endTime-round(time.time()*10)/10
            scoreboard.minutes=int(timeLeft//60)
            scoreboard.seconds=int(timeLeft)%60
            scoreboard.tenths=int(timeLeft*10)%10
            if scoreboard.seconds==0 and scoreboard.clockState and scoreboard.minutes==0 and scoreboard.tenths==0:
                scoreboard.minutes=0
                scoreboard.seconds=0
                scoreboard.clockDigit1=PhotoImage(file=grp('.gif'))
                scoreboard.clockDigit2=PhotoImage(file=grp('yellow-0.gif'))
                scoreboard.clockDigit3=PhotoImage(file=grp('yellow-0.gif'))
                scoreboard.clockDigit4=PhotoImage(file=grp('.gif'))
                scoreboard.img.config(image=scoreboard.clockDigit1)
                scoreboard.img1.config(image=scoreboard.clockDigit2)
                scoreboard.img2.config(image=scoreboard.clockDigit3)
                scoreboard.img3.config(image=scoreboard.clockDigit4)
                clockLabel.config(text='  0.0  ')
                scoreboard.update_idletasks()
                scoreboard.clockState=False
                if scoreboard.autoHorn:
                    buzzer()
                return
            update_clock(scoreboard)
            scoreboard.update_idletasks()
            controlpanel.update_idletasks()
            scoreboard.after(10, start_time)
def increase_home_score():
        scoreboard.homeScore+=1
        if scoreboard.homeScore>199:
            scoreboard.homeScore=199
        if scoreboard.homeScore<10:
            homeLabel.config(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeLabel.config(text='  '+str(scoreboard.homeScore))
        else:
            homeLabel.config(text=str(scoreboard.homeScore))
        update_score()
        scoreboard.update_idletasks()
def decrease_home_score():
        if scoreboard.homeScore>0:
            scoreboard.homeScore-=1
        if scoreboard.homeScore<10:
            homeLabel.config(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeLabel.config(text='  '+str(scoreboard.homeScore))
        else:
            homeLabel.config(text=str(scoreboard.homeScore))
        update_score()
        scoreboard.update_idletasks()
def decrease_guest_score():
        if scoreboard.guestScore>0:
            scoreboard.guestScore-=1
        if scoreboard.guestScore<10:
            guestLabel.config(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestLabel.config(text='  '+str(scoreboard.guestScore))
        else:
            guestLabel.config(text=str(scoreboard.guestScore))
        update_score()
        scoreboard.update_idletasks()
def increase_guest_score():
        if scoreboard.guestScore<199:
            scoreboard.guestScore+=1
        if scoreboard.guestScore<10:
            guestLabel.config(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestLabel.config(text='  '+str(scoreboard.guestScore))
        else:
            guestLabel.config(text=str(scoreboard.guestScore))
        update_score()
        scoreboard.update_idletasks()
def decrease_period():
    scoreboard.period-=1
    if scoreboard.period<1:
        scoreboard.period=9
    update_period()
    scoreboard.update_idletasks()
    controlpanel.update_idletasks()
def increase_period():
    scoreboard.period+=1
    if scoreboard.period>9:
        scoreboard.period=1
    update_period()
    scoreboard.update_idletasks()
    controlpanel.update_idletasks()
controlpanel.resizable(False, False)
controlpanel.settingTime=False
controlpanel.settingHomeName=False
controlpanel.settingGuestName=False
def set_time():
        if controlpanel.settingTime==False and (not scoreboard.clockState):
            minuteEntry.config(state=NORMAL)
            secondEntry.config(state=NORMAL)
            setTimeButton.config(text='Confirm Time')
            controlpanel.settingTime=True
        else:
            try:
                if int(minuteEntry.get())>99 or int(minuteEntry.get())<0 or int(secondEntry.get())>59 or int(secondEntry.get())<0:
                    messagebox.showinfo('Error', 'Value(s) are invalid', parent=controlpanel)
                elif not scoreboard.clockState:
                    scoreboard.minutes=int(minuteEntry.get())
                    scoreboard.seconds=int(secondEntry.get())
                    scoreboard.tenths=0
                    setTimeButton.config(text='Set Time')
                    controlpanel.settingTime=False
                    minuteEntry.config(state=DISABLED)
                    secondEntry.config(state=DISABLED)
                    update_clock(scoreboard)
            except ValueError:
                messagebox.showerror('Error', 'Value(s) are invalid', parent=controlpanel)
        scoreboard.update_idletasks()
def start_stop():
        global endTime
        if (not scoreboard.clockState) and (scoreboard.minutes>0 or scoreboard.seconds>0) and controlpanel.settingTime==False:
            scoreboard.clockState=True
            endTime=round(time.time()*10)/10+scoreboard.minutes*60+scoreboard.seconds+0.1*scoreboard.tenths
            start_time()
        else:
            scoreboard.clockState=False
            timeSave=endTime-round(time.time()*10)/10
            scoreboard.minutes=timeSave//60
            scoreboard.seconds=(timeSave//1)%60
            scoreboard.tenths=(timeSave*10)%10
def reset():
        if (not scoreboard.clockState) and (not controlpanel.settingTime):
            if minuteEntry.get()=='' or secondEntry.get=='':
                scoreboard.minutes=20
                scoreboard.seconds=0
            else:
                scoreboard.minutes=int(minuteEntry.get())
                scoreboard.seconds=int(secondEntry.get())
                scoreboard.tenths=0
            update_clock(scoreboard)
        scoreboard.update_idletasks()
        controlpanel.update_idletasks()
def change_poss_to_home():
    if scoreboard.poss==1:
        scoreboard.poss=0
    else:
        scoreboard.poss=1
    if scoreboard.poss==1:
        homePossLabel.config(foreground='red')
        guestPossLabel.config(foreground='#190000')
    elif scoreboard.poss==2:
        homePossLabel.config(foreground='#190000')
        guestPossLabel.config(foreground='#red')
    else:
        homePossLabel.config(foreground='#190000')
        guestPossLabel.config(foreground='#190000')
def change_poss_to_guest():
    if scoreboard.poss==2:
        scoreboard.poss=0
    else:
        scoreboard.poss=2
    if scoreboard.poss==1:
        homePossLabel.config(foreground='red')
        guestPossLabel.config(foreground='#190000')
    elif scoreboard.poss==2:
        homePossLabel.config(foreground='#190000')
        guestPossLabel.config(foreground='red')
    else:
        homePossLabel.config(foreground='#190000')
        guestPossLabel.config(foreground='#190000')
def set_home_name():
    if not controlpanel.settingHomeName:
        homeChangeNameButton.config(text='Confirm Name')
        controlpanel.settingHomeName=True
        homeNameEntry.config(state=NORMAL)
    else:
        if len(homeNameEntry.get())<9:
            if homeNameEntry.get()=='':
                scoreboard.homeName='HOME'
            else:
                scoreboard.homeName=homeNameEntry.get()
            homeNameLabel.config(text=scoreboard.homeName.upper())
            controlpanel.settingHomeName=False
            homeChangeNameButton.config(text='Set Name')
            homeNameEntry.config(state=DISABLED)
        else:
            messagebox.showinfo('Cannot Set Name', 'The name you entered must be 8 characters or less.', icon='error', parent=controlpanel)
def set_guest_name():
    if not controlpanel.settingGuestName:
        guestChangeNameButton.config(text='Confirm Name')
        controlpanel.settingGuestName=True
        guestNameEntry.config(state=NORMAL)
    else:
        if len(guestNameEntry.get())<9:
            if guestNameEntry.get()=='':
                scoreboard.guestName='GUEST'
            else:
                scoreboard.guestName=guestNameEntry.get()
            guestNameLabel.config(text=scoreboard.guestName.upper())
            controlpanel.settingGuestName=False
            guestChangeNameButton.config(text='Set Name')
            guestNameEntry.config(state=DISABLED)
        else:
            messagebox.showinfo('Cannot Set Name', 'The name you entered must be 8 characters or less.', icon='error', parent=controlpanel)
def new_game():
    global minuteEntry
    global secondEntry
    if not scoreboard.clockState:
        MsgBox = messagebox.askquestion('Reset Scoreboard','Are you sure you want to reset the scoreboard?', parent=controlpanel, icon = 'warning')
        if MsgBox=='yes':
            reset()
            homeLabel.config(text='    0')
            guestLabel.config(text='    0')
            periodControl.config(text='1')
            scoreboard.poss=0
            scoreboard.homeScore=0
            scoreboard.guestScore=0
            scoreboard.period=1
            update_score()
            update_period()
controlpanel.grid()
clockLabel=Label(controlpanel, text='20:00', background='black', foreground='orange')
clockLabel.grid(column=2, row=1)
minuteEntry=Spinbox(controlpanel, from_=0, to=99, textvariable=setminutes, state=DISABLED)
minuteEntry.grid(column=2, row=2)
secondEntry=Spinbox(controlpanel, from_=0, to=59, textvariable=setseconds, state=DISABLED)
secondEntry.grid(column=2, row=3)
setTimeButton=Button(controlpanel, text='Set Time', command=set_time, state=NORMAL)
setTimeButton.grid(column=2, row=4)
startStopButton=Button(controlpanel, text='Start/Stop', command=start_stop)
startStopButton.grid(column=2, row=5)
resetButton=Button(controlpanel, text='Reset', command=reset)
resetButton.grid(column=2, row=6)
homeLabel=Label(controlpanel, text='    0', background='black', foreground='orange')
homeLabel.grid(column=1, row=1)
homeNameEntry=Entry(controlpanel, state=DISABLED)
homeNameEntry.grid(column=1, row=4)
homeChangeNameButton=Button(controlpanel, text='Set Home Name', command=set_home_name)
homeChangeNameButton.grid(column=1, row=5)
homeScore1=Button(controlpanel, text='Score +1', command=increase_home_score)
homeScore1.grid(column=1, row=2)
homeScore2=Button(controlpanel, text='Score -1', command=decrease_home_score)
homeScore2.grid(column=1, row=3)
homePossButton=Button(controlpanel, text='←Poss', command=change_poss_to_home)
homePossButton.grid(column=1, row=6)
guestLabel=Label(controlpanel, text='    0', background='black', foreground='orange')
guestLabel.grid(column=3, row=1)
guestNameEntry=Entry(controlpanel, state=DISABLED)
guestNameEntry.grid(column=3, row=4)
guestChangeNameButton=Button(controlpanel, text='Set Guest Name', command=set_guest_name)
guestChangeNameButton.grid(column=3, row=5)
guestScore1=Button(controlpanel, text='Score +1', command=increase_guest_score)
guestScore1.grid(column=3, row=2)
guestScore2=Button(controlpanel, text='Score -1', command=decrease_guest_score)
guestScore2.grid(column=3, row=3)
guestPossButton=Button(controlpanel, text='Poss→', command=change_poss_to_guest)
guestPossButton.grid(column=3, row=6)
periodControl=Label(controlpanel, text='1', background='black', foreground='orange')
periodControl.grid(column=2, row=7)
periodButton1=Button(controlpanel, text='Previous Period', command=decrease_period)
periodButton1.grid(column=2, row=8)
periodButton2=Button(controlpanel, text='Next Period', command=increase_period)
periodButton2.grid(column=2, row=9)
buzzerButton=Button(controlpanel, text='Buzzer')
buzzerButton.grid(column=2, row=13)
homeTeamLabel=Label(controlpanel, text='HOME', foreground='#00ff00')
homeTeamLabel.grid(column=1, row=9)
homeTeamLabel=Label(controlpanel, text='GUEST', foreground='red')
homeTeamLabel.grid(column=3, row=9)
buzzerButton.bind('<ButtonPress-1>', start_buzzer_loop)
buzzerButton.bind('<ButtonRelease-1>', stop_buzzer_loop)
setminutes.set('20')
setseconds.set('0')
scoreboard.minutes=20
newGameButton=Button(controlpanel, text='Reset Scoreboard', command=new_game)
newGameButton.grid(column=1, row=13)
try:
    scoreboard.iconbitmap(grp('shotclock.ico'))
    controlpanel.iconbitmap(grp('shotclock.ico'))
except:
    messagebox.showinfo('Icon Error', 'App icon photo is missing or corrupt', parent=controlpanel, icon='error')
controlpanel.update_idletasks()
scoreboard.mainloop()
