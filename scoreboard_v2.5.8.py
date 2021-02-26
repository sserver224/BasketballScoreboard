from tkinter import *
import pygame
import time
from tkinter import messagebox
scoreboard=Tk()
shotclock=Tk()
shotclock.seconds=0
shotclock.tenths=0
shotclock.clockState=False
scoreboard.config(bg='black')
scoreboard.grid()
shotclock.clockSwitch=False
scoreboard.title('Main Scoreboard')
timeLabel=Label(scoreboard, text='  0.0  ', bg="black", foreground='yellow')
timeLabel.grid(column=350,row=0,sticky='N')
homeScoreLabel=Label(scoreboard, text='    0', bg='black', foreground='red')
homeScoreLabel.grid(column=0,row=300,sticky='SW')
guestScoreLabel=Label(scoreboard, text='    0', bg='black', foreground='red')
guestScoreLabel.grid(column=400,row=300,sticky='SE')
homeNameLabel=Label(scoreboard, text="HOME", bg='black', foreground='orange')
homeNameLabel.grid(column=0,row=290,sticky='W')
shotclock.config(bg='black')
homePossLabel=Label(scoreboard, text="← POSS", bg='black', foreground='#001900')
homePossLabel.grid(column=0, row=0)
homeBonusLabel=Label(scoreboard, text="← BONUS", bg='black', foreground='#190000')
homeBonusLabel.grid(column=0, row=100)
guestNameLabel=Label(scoreboard, text="GUEST", bg='black', foreground='orange')
guestNameLabel.grid(column=400,row=290,sticky='E')
guestPossLabel=Label(scoreboard, text="POSS →", bg='black', foreground='#001900')
guestPossLabel.grid(column=400, row=0)
guestBonusLabel=Label(scoreboard, text="BONUS →", bg='black', foreground='#190000')
guestBonusLabel.grid(column=400, row=100)
homePossLabel.config(font=('Century Gothic', 25))
guestPossLabel.config(font=('Century Gothic', 25))
homeBonusLabel.config(font=('Century Gothic', 25))
guestBonusLabel.config(font=('Century Gothic', 25))
scoreboard.autoHorn=True
periodLabel=Label(scoreboard, text='1', bg='black', foreground='#00ff00')
periodLabel.place(x=380, y=250)
periodNameLabel=Label(scoreboard, text='PERIOD', font=('Century Gothic', 25), bg='black', foreground='white')
periodNameLabel.place(x=350, y=200)
homeFoulsNameLabel=Label(scoreboard, text='FOULS', bg='black', foreground='white')
homeFoulsNameLabel.place(x=0, y=390)
homeFoulsLabel=Label(scoreboard, text='  0', bg='black', foreground='#00ff00')
homeFoulsLabel.place(x=0, y=430)
guestFoulsNameLabel=Label(scoreboard, text='FOULS', bg='black', foreground='white')
guestFoulsNameLabel.place(x=690, y=390)
guestFoulsLabel=Label(scoreboard, text='  0', bg='black', foreground='#00ff00')
guestFoulsLabel.place(x=640, y=430)
playerLabel=Label(scoreboard, text='    ', bg='black', fg='red', font=('Century Gothic', 100))
playerLabel.place(x=280, y=430)
playerNameLabel=Label(scoreboard, text='PLAYER      FOUL', bg='black', fg='white', font=('Century Gothic', 25))
playerNameLabel.place(x=305, y=390)
foulLabel=Label(scoreboard, text='  ', bg='black', fg='red', font=('Century Gothic', 100))
foulLabel.place(x=475, y=430)
mainTimeLabel=Label(shotclock, text='  0.0  ', bg='black', foreground='yellow')
mainTimeLabel.pack()
shotclock.title('Shot Clock')
shotTimeLabel=Label(shotclock, text='    ', bg='black', foreground='red')
shotTimeLabel.pack()
shotclock.resizable(False, False)
shotclock.reset1=24
shotclock.reset2=14
shotTimeLabel.config(font=('Century Gothic', 200))
scoreboard.minutes=0
scoreboard.seconds=0
scoreboard.tenths=0
scoreboard.poss=0
scoreboard.homeTol=5
scoreboard.guestTol=5
shotclock.enabled=False
scoreboard.homeFouls=0
scoreboard.guestFouls=0
scoreboard.autoStopClock=False
scoreboard.homeBonus=False
scoreboard.guestBonus=False
scoreboard.homeScore=0
scoreboard.guestScore=0
scoreboard.period=1
pygame.mixer.init()
channel=pygame.mixer.find_channel()
scoreboard.fast=False
scoreboard.clockState=False
mainTimeLabel.config(font=("Century Gothic", 100))
timeLabel.config(font=("Century Gothic", 100))
homeScoreLabel.config(font=("Century Gothic", 100))
guestScoreLabel.config(font=("Century Gothic", 100))
periodLabel.config(font=('Century Gothic', 80))
homeNameLabel.config(font=('Century Gothic', 25))
guestNameLabel.config(font=('Century Gothic', 25))
scoreboard.geometry('800x580')
homeFoulsLabel.config(font=('Century Gothic', 100))
guestFoulsLabel.config(font=('Century Gothic', 100))
homeFoulsNameLabel.config(font=('Century Gothic', 25))
guestFoulsNameLabel.config(font=('Century Gothic', 25))
scoreboard.homeName='HOME'
scoreboard.guestName='GUEST'
controlpanel=Tk()
controlpanel.homeScoreSet=StringVar()
controlpanel.guestScoreSet=StringVar()
controlpanel.homeFoulsSet=StringVar()
controlpanel.guestFoulsSet=StringVar()
controlpanel.shotClockSet=StringVar()
controlpanel.periodSet=StringVar()
shotclockcontrolpanel=Tk()
homeTolNameLabel=Label(scoreboard, text='TOL', bg='black', fg='white', font=('Century Gothic', 15))
homeTolNameLabel.place(x=200, y=445)
guestTolNameLabel=Label(scoreboard, text='TOL', bg='black', fg='white', font=('Century Gothic', 15))
guestTolNameLabel.place(x=595, y=445)
homeTolLabel=Label(scoreboard, text='5', bg='black', fg='red', font=('Century Gothic', 50))
homeTolLabel.place(x=200, y=470)
guestTolLabel=Label(scoreboard, text='5', bg='black', fg='red', font=('Century Gothic', 50))
guestTolLabel.place(x=595, y=470)
setcontrolpanel=Tk()
setcontrolpanel.title('Options')
controlpanel.title('Control Panel')
controlpanel.settingReset1=False
controlpanel.settingReset2=False
shotclockcontrolpanel.title('Shot Clock Control Panel')
shotclockcontrolpanel.resizable(False, False)
shotclockcontrolpanel.geometry('200x200')
setcontrolpanel.geometry('250x560')
setcontrolpanel.resizable(False, False)
scoreboard.resizable(False, False)
def buzzer():
    sound=pygame.mixer.Sound('Buzzer.wav')
    channel.play(sound)
def horn():
    sound=pygame.mixer.Sound('Horn.wav')
    channel.play(sound)
def start_buzzer_loop(c):
    sound=pygame.mixer.Sound('BuzzerLoop.wav')
    channel.play(sound, -1)
def stop_buzzer_loop(c):
    channel.stop()
def reset_1():
    if shotclock.enabled and (not controlpanel.settingReset1):
        shotclock.seconds=shotclock.reset1
        shotclock.tenths=0
        if scoreboard.minutes>0 or scoreboard.seconds>24:
            if shotclock.seconds>9:
                shotTimeLabel.config(text=str(shotclock.seconds))
                shotLabel.config(text=str(shotclock.seconds))
            else:
                shotTimeLabel.config(text='0'+str(shotclock.seconds))
                shotLabel.config(text='0'+str(shotclock.seconds))
        else:
            shotTimeLabel.config(text='    ')
    else:
            shotTimeLabel.config(text='    ')
    shotclock.update()
def reset_2():
    if shotclock.enabled and (not controlpanel.settingReset2):
        shotclock.seconds=shotclock.reset2
        shotclock.tenths=0
        if scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds:
            if shotclock.seconds>9:
                shotTimeLabel.config(text=str(shotclock.seconds))
                shotLabel.config(text=str(shotclock.seconds))
            else:
                shotTimeLabel.config(text='0'+str(shotclock.seconds))
                shotLabel.config(text='0'+str(shotclock.seconds))
        else:
            shotTimeLabel.config(text='    ')
    else:
        shotTimeLabel.config(text='    ')
    shotclock.update()
def doSomething():
    if not scoreboard.clockState:
        shotclock.destroy()
        controlpanel.destroy()
        scoreboard.destroy()
        shotclockcontrolpanel.destroy()
        setcontrolpanel.destroy()
scoreboard.protocol('WM_DELETE_WINDOW', doSomething)
shotclock.protocol('WM_DELETE_WINDOW', doSomething)
controlpanel.protocol('WM_DELETE_WINDOW', doSomething)
setcontrolpanel.protocol('WM_DELETE_WINDOW', doSomething)
shotclockcontrolpanel.protocol('WM_DELETE_WINDOW', doSomething)
def start_time():
        while scoreboard.clockState:
            if scoreboard.fast:
                if shotclock.clockState:
                    time.sleep(0.02)
                else:
                    time.sleep(0.04)
            else:
                if shotclock.clockState:
                    time.sleep(0.077)
                else:
                    if (scoreboard.seconds>shotclock.seconds or scoreboard.minutes>0) and shotclock.enabled:
                        time.sleep(0.093)
                    else:
                        time.sleep(0.09)
            if scoreboard.tenths<=0:
                scoreboard.seconds-=1
                scoreboard.tenths=9
                if scoreboard.seconds<0:
                    scoreboard.minutes-=1
                    scoreboard.seconds=59
            else:
                scoreboard.tenths-=1
            if scoreboard.seconds==0 and scoreboard.clockState and scoreboard.minutes==0 and scoreboard.tenths==0:
                scoreboard.minutes=0
                scoreboard.seconds=0
                timeLabel.config(text='  0.0  ')
                mainTimeLabel.config(text='  0.0  ')
                clockLabel.config(text='  0.0  ')
                scoreboard.update()
                scoreboard.clockState=False
                if scoreboard.autoHorn:
                    buzzer()
                break
             
            if (scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds) and shotclock.enabled:
                 if shotclock.clockState and shotclock.seconds>=0:
                    if shotclock.seconds<=0:
                            shotclock.seconds=0
                            shotclock.tenths=0
                            shotTimeLabel.config(text='00')
                            if scoreboard.autoHorn:
                                horn()
                            shotclock.clockState=False
                            runButton.set(0)
                            if scoreboard.autoStopClock:
                                scoreboard.clockState=False
                                break

                    else:
                        shotclock.tenths-=1
                        if shotclock.tenths<0:
                            shotclock.seconds-=1
                            shotclock.tenths=9
                    if shotclock.seconds<10:
                        shotTimeLabel.config(text='0'+str(shotclock.seconds))
                        shotLabel.config(text='0'+str(shotclock.seconds))
                    else:
                        shotTimeLabel.config(text=str(shotclock.seconds))
                        shotLabel.config(text=str(shotclock.seconds))
            else:
                    shotTimeLabel.config(text='    ')
                    shotLabel.config(text='    ')
                    shotclock.seconds=0
                    shotclock.tenths=0
                    channel.stop()
                    shotclock.clockState=False
                    runButton.set(0)
            if scoreboard.seconds<10 and scoreboard.minutes>0:
                if scoreboard.minutes<10:
                    timeLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    clockLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    mainTimeLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                else:
                    timeLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    clockLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    mainTimeLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
            elif scoreboard.minutes==0:
                if scoreboard.seconds<10:
                    timeLabel.config(text='  '+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    clockLabel.config(text='  '+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    mainTimeLabel.config(text='  '+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                else:
                    timeLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    clockLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    mainTimeLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
            else:
                if scoreboard.minutes<10:
                    timeLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    clockLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    mainTimeLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                else:
                    timeLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    clockLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    mainTimeLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
            scoreboard.update()
            controlpanel.update()
            shotclock.update()

def increase_home_score_by_1():
        scoreboard.homeScore+=1
        if scoreboard.homeScore>199:
            scoreboard.homeScore=199
        if scoreboard.homeScore<10:
            homeScoreLabel.config(text='    '+str(scoreboard.homeScore))
            homeLabel.config(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeScoreLabel.config(text='  '+str(scoreboard.homeScore))
            homeLabel.config(text='  '+str(scoreboard.homeScore))
        else:
            homeScoreLabel.config(text=str(scoreboard.homeScore))
            homeLabel.config(text=str(scoreboard.homeScore))
        scoreboard.update()
def increase_home_score_by_2():
        scoreboard.homeScore+=2
        if scoreboard.homeScore>199:
            scoreboard.homeScore=199
        if scoreboard.homeScore<10:
            homeScoreLabel.config(text='    '+str(scoreboard.homeScore))
            homeLabel.config(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeScoreLabel.config(text='  '+str(scoreboard.homeScore))
            homeLabel.config(text='  '+str(scoreboard.homeScore))
        else:
            homeScoreLabel.config(text=str(scoreboard.homeScore))
            homeLabel.config(text=str(scoreboard.homeScore))
        scoreboard.update()  
def increase_home_score_by_3():
        scoreboard.homeScore+=3
        if scoreboard.homeScore>199:
            scoreboard.homeScore=199
        if scoreboard.homeScore<10:
            homeScoreLabel.config(text='    '+str(scoreboard.homeScore))
            homeLabel.config(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeScoreLabel.config(text='  '+str(scoreboard.homeScore))
            homeLabel.config(text='  '+str(scoreboard.homeScore))
        else:
            homeScoreLabel.config(text=str(scoreboard.homeScore))
            homeLabel.config(text=str(scoreboard.homeScore))
        scoreboard.update()
def decrease_home_score():
        if scoreboard.homeScore>0:
            scoreboard.homeScore-=1
        if scoreboard.homeScore<10:
            homeScoreLabel.config(text='    '+str(scoreboard.homeScore))
            homeLabel.config(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeScoreLabel.config(text='  '+str(scoreboard.homeScore))
            homeLabel.config(text='  '+str(scoreboard.homeScore))
        else:
            homeScoreLabel.config(text=str(scoreboard.homeScore))
            homeLabel.config(text=str(scoreboard.homeScore))
        scoreboard.update()
def increase_guest_score_by_1():
        scoreboard.guestScore+=1
        if scoreboard.guestScore>199:
            scoreboard.guestScore=199
        if scoreboard.guestScore<10:
            guestScoreLabel.config(text='    '+str(scoreboard.guestScore))
            guestLabel.config(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestScoreLabel.config(text='  '+str(scoreboard.guestScore))
            guestLabel.config(text='  '+str(scoreboard.guestScore))
        else:
            guestScoreLabel.config(text=str(scoreboard.guestScore))
            guestLabel.config(text=str(scoreboard.guestScore))
        scoreboard.update()
def increase_guest_score_by_2():
        scoreboard.guestScore+=2
        if scoreboard.guestScore>199:
            scoreboard.guestScore=199
        if scoreboard.guestScore<10:
            guestScoreLabel.config(text='    '+str(scoreboard.guestScore))
            guestLabel.config(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestScoreLabel.config(text='  '+str(scoreboard.guestScore))
            guestLabel.config(text='  '+str(scoreboard.guestScore))
        else:
            guestScoreLabel.config(text=str(scoreboard.guestScore))
            guestLabel.config(text=str(scoreboard.guestScore))
        scoreboard.update()
def increase_guest_score_by_3():
        scoreboard.guestScore+=3
        if scoreboard.guestScore>199:
            scoreboard.guestScore=199
        if scoreboard.guestScore<10:
            guestScoreLabel.config(text='    '+str(scoreboard.guestScore))
            guestLabel.config(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestScoreLabel.config(text='  '+str(scoreboard.guestScore))
            guestLabel.config(text='  '+str(scoreboard.guestScore))
        else:
            guestScoreLabel.config(text=str(scoreboard.guestScore))
            guestLabel.config(text=str(scoreboard.guestScore))
        scoreboard.update()
def decrease_guest_score():
        if scoreboard.guestScore>0:
            scoreboard.guestScore-=1
        if scoreboard.guestScore<10:
            guestScoreLabel.config(text='    '+str(scoreboard.guestScore))
            guestLabel.config(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestScoreLabel.config(text='  '+str(scoreboard.guestScore))
            guestLabel.config(text='  '+str(scoreboard.guestScore))
        else:
            guestScoreLabel.config(text=str(scoreboard.guestScore))
            guestLabel.config(text=str(scoreboard.guestScore))
        scoreboard.update()

def decrease_period():
    scoreboard.period-=1
    if scoreboard.period<1:
        scoreboard.period=9
    periodLabel.config(text=str(scoreboard.period))
    periodControl.config(text=str(scoreboard.period))
    scoreboard.update()
    controlpanel.update()
def increase_period():
    scoreboard.period+=1
    if scoreboard.period>9:
        scoreboard.period=1
    periodLabel.config(text=str(scoreboard.period))
    periodControl.config(text=str(scoreboard.period))
    scoreboard.update()
    controlpanel.update()
try:
    scoreboard.iconbitmap('shotclock.ico')
    shotclock.iconbitmap('shotclock.ico')
    controlpanel.iconbitmap('shotclock.ico')
    shotclockcontrolpanel.iconbitmap('shotclock.ico')
    setcontrolpanel.iconbitmap('shotclock.ico')
except:
    messagebox.showinfo('Icon Error', 'App icon photo is missing or corrupt', icon='error')
controlpanel.resizable(False, False)
controlpanel.settingTime=False
controlpanel.settingHomeName=False
controlpanel.settingGuestName=False
controlpanel.settingHomeScore=False
controlpanel.settingHomeFouls=False
controlpanel.settingGuestScore=False
controlpanel.settingGuestFouls=False
controlpanel.settingShotClock=False
controlpanel.settingPlayerFouls=False
def set_time():
        if controlpanel.settingTime==False and (not scoreboard.clockState):
            minuteEntry.config(state=NORMAL)
            secondEntry.config(state=NORMAL)
            setTimeButton.config(text='Confirm Time')
            controlpanel.settingTime=True
        else:
            try:
                setErrorLabel.config(text='')
                if int(minuteEntry.get())>99 or int(minuteEntry.get())<0 or int(secondEntry.get())>59 or int(secondEntry.get())<0:
                    setErrorLabel.config(text='Error: Value(s) are invalid.')
                elif not scoreboard.clockState:
                    scoreboard.minutes=int(minuteEntry.get())
                    scoreboard.seconds=int(secondEntry.get())
                    setTimeButton.config(text='Set Time')
                    controlpanel.settingTime=False
                    minuteEntry.config(state=DISABLED)
                    secondEntry.config(state=DISABLED)
                    if scoreboard.seconds<10 and scoreboard.minutes>0:
                        if scoreboard.minutes<10:
                            timeLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                            clockLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                            mainTimeLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                        else:
                            timeLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                            clockLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                            mainTimeLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    elif scoreboard.minutes==0:
                        if scoreboard.seconds<10:
                            timeLabel.config(text='  '+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                            clockLabel.config(text='  '+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                            mainTimeLabel.config(text='  '+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                        else:
                            timeLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                            clockLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                            mainTimeLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    else:
                        if scoreboard.minutes<10:
                            timeLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                            clockLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                            mainTimeLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                        else:
                            timeLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                            clockLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                            mainTimeLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    if (scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds) and shotclock.enabled:
                        if shotclock.seconds<10:
                            shotTimeLabel.config(text='0'+str(shotclock.seconds))
                            shotLabel.config(text='0'+str(shotclock.seconds))
                        else:
                            shotTimeLabel.config(text=str(shotclock.seconds))
                            shotLabel.config(text=str(shotclock.seconds))
                    else:
                        shotTimeLabel.config(text='    ')
                        shotLabel.config(text='    ')
                        shotclock.clockState=False
                        runButton.set(0)
            except ValueError:
                setErrorLabel.config(text='Error: Value(s) are invalid.')
        scoreboard.update()
        controlpanel.update()
        shotclock.update()

def start_stop():
        if (not scoreboard.clockState) and (scoreboard.minutes>0 or scoreboard.seconds>0) and controlpanel.settingTime==False:
            scoreboard.clockState=True
            start_time()
        else:
            scoreboard.clockState=False

def reset():
        if (not scoreboard.clockState) and (not controlpanel.settingTime):
            scoreboard.minutes=int(minuteEntry.get())
            scoreboard.seconds=int(secondEntry.get())
            scoreboard.tenths=0
        if scoreboard.seconds<10 and scoreboard.minutes>0:
                if scoreboard.minutes<10:
                    timeLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    clockLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    mainTimeLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                else:
                    timeLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    clockLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    mainTimeLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
        elif scoreboard.minutes==0:
                if scoreboard.seconds<10:
                    timeLabel.config(text='  '+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    clockLabel.config(text='  '+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    mainTimeLabel.config(text='  '+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                else:
                    timeLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    clockLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    mainTimeLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
        else:
                if scoreboard.minutes<10:
                    timeLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    clockLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    mainTimeLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                else:
                    timeLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    clockLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    mainTimeLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
        if (scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds) and shotclock.enabled:
            if shotclock.seconds<10:
                shotTimeLabel.config(text='0'+str(shotclock.seconds))
                shotLabel.config(text='0'+str(shotclock.seconds))
            else:
                shotTimeLabel.config(text=str(shotclock.seconds))
                shotLabel.config(text=str(shotclock.seconds))
        else:
            shotTimeLabel.config(text='    ')
            shotLabel.config(text='    ')
            shotclock.clockState=False
            runButton.set(0)
        scoreboard.update()
        shotclock.update()
        controlpanel.update()
        
def shot_run_stop(v):
    if int(v)==1:
        if (shotclock.seconds>0 or shotclock.tenths>0) and (scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds):
            shotclock.clockState=True
        else:
            runButton.set(0)
    else:
        shotclock.clockState=False
def toggle_fast():
    if not scoreboard.clockState:
        if not scoreboard.fast:
            scoreboard.fast=True
            fastButton.config(text='Fast Mode: ON')
        else:
            scoreboard.fast=False
            fastButton.config(text='Fast Mode: OFF')
def change_poss_to_home():
    if scoreboard.poss==1:
        scoreboard.poss=0
    else:
        scoreboard.poss=1
    if scoreboard.poss==1:
        homePossLabel.config(foreground='#00ff00')
        guestPossLabel.config(foreground='#001900')
    elif scoreboard.poss==2:
        homePossLabel.config(foreground='#001900')
        guestPossLabel.config(foreground='#00ff00')
    else:
        homePossLabel.config(foreground='#001900')
        guestPossLabel.config(foreground='#001900')
def change_poss_to_guest():
    if scoreboard.poss==2:
        scoreboard.poss=0
    else:
        scoreboard.poss=2
    if scoreboard.poss==1:
        homePossLabel.config(foreground='#00ff00')
        guestPossLabel.config(foreground='#001900')
    elif scoreboard.poss==2:
        homePossLabel.config(foreground='#001900')
        guestPossLabel.config(foreground='#00ff00')
    else:
        homePossLabel.config(foreground='#001900')
        guestPossLabel.config(foreground='#001900')
def toggle_home_bonus():
    if not scoreboard.homeBonus:
        scoreboard.homeBonus=True
    else:
        scoreboard.homeBonus=False
    if scoreboard.homeBonus:
        homeBonusLabel.config(foreground='red')
    else:
        homeBonusLabel.config(foreground='#190000')

def toggle_guest_bonus():
    if not scoreboard.guestBonus:
        scoreboard.guestBonus=True
    else:
        scoreboard.guestBonus=False
    if scoreboard.guestBonus:
        guestBonusLabel.config(foreground='red')
    else:
        guestBonusLabel.config(foreground='#190000')

def increase_home_fouls():
    if scoreboard.homeFouls<19:
        scoreboard.homeFouls+=1
    if scoreboard.homeFouls<10:
        homeFoulsLabel.config(text='  '+str(scoreboard.homeFouls))
        fouls1Label.config(text='  '+str(scoreboard.homeFouls))
    else:
        homeFoulsLabel.config(text=str(scoreboard.homeFouls))
        fouls1Label.config(text=str(scoreboard.homeFouls))
def remove_home_fouls():
    if scoreboard.homeFouls>0:
        scoreboard.homeFouls-=1
    if scoreboard.homeFouls<10:
        homeFoulsLabel.config(text='  '+str(scoreboard.homeFouls))
        fouls1Label.config(text='  '+str(scoreboard.homeFouls))
    else:
        homeFoulsLabel.config(text=str(scoreboard.homeFouls))
        fouls1Label.config(text=str(scoreboard.homeFouls))
def increase_guest_fouls():
    if scoreboard.guestFouls<19:
        scoreboard.guestFouls+=1
    if scoreboard.guestFouls<10:
        guestFoulsLabel.config(text='  '+str(scoreboard.guestFouls))
        fouls2Label.config(text='  '+str(scoreboard.guestFouls))
    else:
        guestFoulsLabel.config(text=str(scoreboard.guestFouls))
        fouls2Label.config(text=str(scoreboard.guestFouls))
def remove_guest_fouls():
    if scoreboard.guestFouls>0:
        scoreboard.guestFouls-=1
    if scoreboard.guestFouls<10:
        guestFoulsLabel.config(text='  '+str(scoreboard.guestFouls))
        fouls2Label.config(text='  '+str(scoreboard.guestFouls))
    else:
        guestFoulsLabel.config(text=str(scoreboard.guestFouls))
        fouls2Label.config(text=str(scoreboard.guestFouls))
def auto_stop_clock():
    if not scoreboard.autoStopClock:
        scoreboard.autoStopClock=True
        autoStopClockButton.config(text='Stop main clock when shot clock expires: ON')
    else:
        scoreboard.autoStopClock=False
        autoStopClockButton.config(text='Stop main clock when shot clock expires: OFF')
def set_home_name():
    setErrorLabel.config(text='')
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
            setErrorLabel.config(text='Error: Value is invalid')
def set_guest_name():
    setErrorLabel.config(text='')
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
            setErrorLabel.config(text='Error: Value is invalid')
def toggle_shot_clock():
    if not shotclock.enabled:
        shotclock.enabled=True
        shotResetButton1.config(state=NORMAL)
        shotResetButton2.config(state=NORMAL)
        runButton.config(state=NORMAL)
        setShotClockButton.config(state=NORMAL)
        autoStopClockButton.config(state=NORMAL)
        setReset1Button.config(state=NORMAL)
        setReset2Button.config(state=NORMAL)
        toggleShotClockButton.config(text='Enable Shot Clock: ON')
        if scoreboard.minutes>0 or scoreboard.seconds>24:
            if shotclock.seconds<10:
                shotTimeLabel.config(text='0'+str(shotclock.seconds))
                shotLabel.config(text='0'+str(shotclock.seconds))
            else:
                shotTimeLabel.config(text=str(shotclock.seconds))
                shotLabel.config(text=str(shotclock.seconds))
        else:
                shotTimeLabel.config(text='    ')
                shotLabel.config(text='    ')
                shotclock.clockState=False
                runButton.set(0)
    elif (not controlpanel.settingShotClock) and (not controlpanel.settingReset1) and (not controlpanel.settingReset2):
        shotTimeLabel.config(text='    ')
        shotLabel.config(text='    ')
        shotclock.clockState=False
        shotclock.enabled=False
        runButton.set(0)
        toggleShotClockButton.config(text='Enable Shot Clock: OFF')
        setReset1Button.config(state=DISABLED)
        setReset2Button.config(state=DISABLED)
        shotResetButton1.config(state=DISABLED)
        shotResetButton2.config(state=DISABLED)
        runButton.config(state=DISABLED)
        scoreboard.autoStopClock=False
        autoStopClockButton.config(text='Stop main clock when shot clock expires: OFF')
        autoStopClockButton.config(state=DISABLED)
        setShotClockButton.config(state=DISABLED)
def set_reset_1():
    if not controlpanel.settingReset1:
        controlpanel.settingReset1=True
        reset1Entry.config(state=NORMAL)
        setErrorLabel.config(text='')
    else:
        try:
            if int(reset1Entry.get())<=99 and int(reset1Entry.get())>0:
                shotclock.reset1=int(reset1Entry.get())
                controlpanel.settingReset1=False
                reset1Entry.config(state=DISABLED)
                setErrorLabel.config(text='')
            elif int(reset1Entry.get())==0:
                shotclock.reset1==24
                controlpanel.settingReset1=False
                reset1Entry.config(state=DISABLED)
                setErrorLabel.config(text='')
            else:
                setErrorLabel.config(text='Error: Value(s) are invalid.')
        except:
            setErrorLabel.config(text='Error: Value(s) are invalid.')
def set_reset_2():
    if not controlpanel.settingReset2:
        controlpanel.settingReset2=True
        reset2Entry.config(state=NORMAL)
        setErrorLabel.config(text='')
    else:
        try:
            if int(reset2Entry.get())<=99 and int(reset2Entry.get())>0:
                shotclock.reset2=int(reset2Entry.get())
                controlpanel.settingReset2=False
                reset2Entry.config(state=DISABLED)
                setErrorLabel.config(text='')
            elif int(reset2Entry.get())==0:
                shotclock.reset2=14
                controlpanel.settingReset2=False
                reset2Entry.config(state=DISABLED)
            else:
                setErrorLabel.config(text='Error: Value(s) are invalid.')
        except:
            setErrorLabel.config(text='Error: Value(s) are invalid.')
def set_home_score():
    setErrorLabel.config(text='')
    if not controlpanel.settingHomeScore:
        homeScoreEntry.config(state=NORMAL)
        controlpanel.settingHomeScore=True
    else:
        try:
            if homeScoreEntry.get()=='':
                homeScoreEntry.config(state=DISABLED)
                controlpanel.settingHomeScore=False
            elif int(homeScoreEntry.get())<=199 and int(homeScoreEntry.get())>=0:
                scoreboard.homeScore=int(homeScoreEntry.get())
                homeScoreEntry.config(state=DISABLED)
                controlpanel.settingHomeScore=False
                controlpanel.homeScoreSet.set('')
                if scoreboard.homeScore<10:
                    homeScoreLabel.config(text='    '+str(scoreboard.homeScore))
                    homeLabel.config(text='    '+str(scoreboard.homeScore))
                elif scoreboard.homeScore<100:
                    homeScoreLabel.config(text='  '+str(scoreboard.homeScore))
                    homeLabel.config(text='  '+str(scoreboard.homeScore))
                else:
                    homeScoreLabel.config(text=str(scoreboard.homeScore))
                    homeLabel.config(text=str(scoreboard.homeScore))
                scoreboard.update()
            else:
                setErrorLabel.config(text='Error: Value(s) are invalid')
        except ValueError:
            setErrorLabel.config(text='Error: Value(s) are invalid')
def set_guest_score():
    setErrorLabel.config(text='')
    if not controlpanel.settingGuestScore:
        guestScoreEntry.config(state=NORMAL)
        controlpanel.settingGuestScore=True
    else:
        try:
            if guestScoreEntry.get()=='':
                guestScoreEntry.config(state=DISABLED)
                controlpanel.settingGuestScore=False
            elif int(guestScoreEntry.get())<=199 and int(guestScoreEntry.get())>=0:
                scoreboard.guestScore=int(guestScoreEntry.get())
                guestScoreEntry.config(state=DISABLED)
                controlpanel.guestScoreSet.set('')
                controlpanel.settingGuestScore=False
                if scoreboard.guestScore<10:
                    guestScoreLabel.config(text='    '+str(scoreboard.guestScore))
                    guestLabel.config(text='    '+str(scoreboard.guestScore))
                elif scoreboard.guestScore<100:
                    guestScoreLabel.config(text='  '+str(scoreboard.guestScore))
                    guestLabel.config(text='  '+str(scoreboard.guestScore))
                else:
                    guestScoreLabel.config(text=str(scoreboard.guestScore))
                    guestLabel.config(text=str(scoreboard.guestScore))
                scoreboard.update()
            else:
                setErrorLabel.config(text='Error: Value(s) are invalid')
        except ValueError:
            setErrorLabel.config(text='Error: Value(s) are invalid')
def set_home_fouls():
    setErrorLabel.config(text='')
    if not controlpanel.settingHomeFouls:
        homeFoulsEntry.config(state=NORMAL)
        controlpanel.settingHomeFouls=True
    else:
        try:
            if homeFoulsEntry.get()=='':
                homeFoulsEntry.config(state=DISABLED)
                controlpanel.settingHomeFouls=False
            elif int(homeFoulsEntry.get())<=19 and int(homeFoulsEntry.get())>=0:
                scoreboard.homeFouls=int(homeFoulsEntry.get())
                homeFoulsEntry.config(state=DISABLED)
                controlpanel.settingHomeFouls=False
                if scoreboard.homeFouls>9:
                    homeFoulsLabel.config(text=str(scoreboard.homeFouls))
                    fouls1Label.config(text=str(scoreboard.homeFouls))
                else:
                    homeFoulsLabel.config(text=' '+str(scoreboard.homeFouls))
                    fouls1Label.config(text='  '+str(scoreboard.homeFouls))
                controlpanel.homeFoulsSet.set('')
                scoreboard.update()
            else:
                setErrorLabel.config(text='Error: Value(s) are invalid')
        except ValueError:
            setErrorLabel.config(text='Error: Value(s) are invalid')
def set_guest_fouls():
    setErrorLabel.config(text='')
    if not controlpanel.settingGuestFouls:
        guestFoulsEntry.config(state=NORMAL)
        controlpanel.settingGuestFouls=True
    else:
        try:
            if guestFoulsEntry.get()=='':
                guestFoulsEntry.config(state=DISABLED)
                controlpanel.settingGuestFouls=False
            elif int(guestFoulsEntry.get())<=19 and int(guestFoulsEntry.get())>=0:
                scoreboard.guestFouls=int(guestFoulsEntry.get())
                guestFoulsEntry.config(state=DISABLED)
                controlpanel.settingGuestFouls=False
                if scoreboard.guestFouls>9:
                    guestFoulsLabel.config(text=str(scoreboard.guestFouls))
                    fouls2Label.config(text=str(scoreboard.guestFouls))
                else:
                    guestFoulsLabel.config(text=' '+str(scoreboard.guestFouls))
                    fouls2Label.config(text='  '+str(scoreboard.guestFouls))
                scoreboard.update()
            else:
                setErrorLabel.config(text='Error: Value(s) are invalid')
        except ValueError:
            setErrorLabel.config(text='Error: Value(s) are invalid')
def set_shot_clock():
    setErrorLabel.config(text='')
    if (not shotclock.clockState) and (not controlpanel.settingShotClock):
        shotClockEntry.config(state=NORMAL)
        controlpanel.settingShotClock=True
    elif not shotclock.clockState:
        try:
            if shotClockEntry.get()=='':
                shotClockEntry.config(state=DISABLED)
                controlpanel.settingShotClock=False
            elif int(shotClockEntry.get())<=99 and int(shotClockEntry.get())>=0:
                shotclock.seconds=int(shotClockEntry.get())
                shotclock.tenths=0
                shotClockEntry.config(state=DISABLED)
                controlpanel.settingShotClock=False
                if shotclock.enabled and (scoreboard.minutes>0 or scoreboard.seconds>24):
                    if shotclock.seconds>9:
                        shotTimeLabel.config(text=str(shotclock.seconds))
                        shotLabel.config(text=str(shotclock.seconds))
                    else:
                        shotTimeLabel.config(text=str(shotclock.seconds)+str(shotclock.tenths))
                        shotLabel.config(text=str(shotclock.seconds)+str(shotclock.tenths))
                else:
                        shotTimeLabel.config(text='    ')
                scoreboard.update()
                shotclock.update()
                shotclockcontrolpanel.update()
            else:
                setErrorLabel.config(text='Error: Value(s) are invalid')
        except ValueError:
            setErrorLabel.config(text='Error: Value(s) are invalid')
def set_player_fouls():
    setErrorLabel.config(text='')
    if not controlpanel.settingPlayerFouls:
        controlpanel.settingPlayerFouls=True
        playerEntry.config(state=NORMAL)
        foulEntry.config(state=NORMAL)
    else:
        if playerEntry.get()=='' or foulEntry.get()=='':
            playerLabel.config(text='  ')
            foulLabel.config(text=' ')
            playerEntry.config(state=DISABLED)
            foulEntry.config(state=DISABLED)
            controlpanel.settingPlayerFouls=False
        else:
            try:
                if int(playerEntry.get())<=99 and int(playerEntry.get())>=0 and int(foulEntry.get())<=9 and int(foulEntry.get())>=0:
                    scoreboard.player=int(playerEntry.get())
                    scoreboard.playerFoul=int(foulEntry.get())
                    if scoreboard.player<10:
                        playerLabel.config(text=' '+str(scoreboard.player))
                    else:
                        playerLabel.config(text=str(scoreboard.player))
                    foulLabel.config(text=str(scoreboard.playerFoul))
                    playerEntry.config(state=DISABLED)
                    foulEntry.config(state=DISABLED)
                    controlpanel.settingPlayerFouls=False
                else:
                    setErrorLabel.config(text='Error: Value(s) are invalid')
            except ValueError:
                setErrorLabel.config(text='Error: Value(s) are invalid')
def add_home_tol():
    if scoreboard.homeTol<9:
        scoreboard.homeTol+=1
    homeTolLabel.config(text=str(scoreboard.homeTol))
    tol1Label.config(text=str(scoreboard.homeTol))
def remove_home_tol():
    if scoreboard.homeTol>0:
        scoreboard.homeTol-=1
    homeTolLabel.config(text=str(scoreboard.homeTol))
    tol1Label.config(text=str(scoreboard.homeTol))
def add_guest_tol():
    if scoreboard.guestTol<9:
        scoreboard.guestTol+=1
    guestTolLabel.config(text=str(scoreboard.guestTol))
    tol2Label.config(text=str(scoreboard.guestTol))
def remove_guest_tol():
    if scoreboard.guestTol>0:
        scoreboard.guestTol-=1
    guestTolLabel.config(text=str(scoreboard.guestTol))
    tol2Label.config(text=str(scoreboard.guestTol))
controlpanel.grid()
setErrorLabel=Label(setcontrolpanel, text='', foreground='red')
setErrorLabel.pack()
clockLabel=Label(controlpanel, text='  0.0  ', bg='black', foreground='orange')   
clockLabel.grid(column=3, row=1)
minuteEntry=Spinbox(controlpanel, from_=0, to=99, state=DISABLED)
minuteEntry.grid(column=3, row=2)
secondEntry=Spinbox(controlpanel, from_=0, to=59, state=DISABLED)
secondEntry.grid(column=3, row=3)
setTimeButton=Button(controlpanel, text='Set Time', command=set_time, state=NORMAL)
setTimeButton.grid(column=3, row=4)
startStopButton=Button(controlpanel, text='Start/Stop', command=start_stop)
startStopButton.grid(column=3, row=5)
reset1Entry=Spinbox(setcontrolpanel, from_=0, to=99, state=DISABLED)
reset1Entry.pack()
setReset1Button=Button(setcontrolpanel, state=DISABLED, text='Set Shot Clock Reset 1', command=set_reset_1)
setReset1Button.pack()
reset2Entry=Spinbox(setcontrolpanel, from_=0, to=99, state=DISABLED)
reset2Entry.pack()
setReset2Button=Button(setcontrolpanel, state=DISABLED, text='Set Shot Clock Reset 2', command=set_reset_2)
setReset2Button.pack()
homeScoreEntry=Entry(setcontrolpanel, textvar=controlpanel.homeScoreSet, state=DISABLED)
homeScoreEntry.pack()
setHomeScoreButton=Button(setcontrolpanel, text='Set Home Score', command=set_home_score)
setHomeScoreButton.pack()
guestScoreEntry=Entry(setcontrolpanel, textvar=controlpanel.guestScoreSet, state=DISABLED)
guestScoreEntry.pack()
setGuestScoreButton=Button(setcontrolpanel, text='Set Guest Score',command=set_guest_score)
setGuestScoreButton.pack()
homeFoulsEntry=Entry(setcontrolpanel, textvar=controlpanel.homeFoulsSet, state=DISABLED)
homeFoulsEntry.pack()
setHomeFoulsButton=Button(setcontrolpanel, text='Set Home Fouls', command=set_home_fouls)
setHomeFoulsButton.pack()
guestFoulsEntry=Entry(setcontrolpanel, textvar=controlpanel.guestFoulsSet, state=DISABLED)
guestFoulsEntry.pack()
setGuestFoulsButton=Button(setcontrolpanel, text='Set Guest Fouls', command=set_guest_fouls)
setGuestFoulsButton.pack()
shotClockEntry=Entry(setcontrolpanel, textvar=controlpanel.shotClockSet, state=DISABLED)
shotClockEntry.pack()
setShotClockButton=Button(setcontrolpanel, text='Set Shot Clock', state=DISABLED, command=set_shot_clock)
setShotClockButton.pack()
resetButton=Button(controlpanel, text='Reset', command=reset)
resetButton.grid(column=3, row=6)
fastButton=Button(setcontrolpanel, text='Fast Mode: OFF', command=toggle_fast)
fastButton.pack()
homeLabel=Label(controlpanel, text='    0', bg='black', foreground='orange')
homeLabel.grid(column=1, row=1)
homeNameEntry=Entry(setcontrolpanel, state=DISABLED)
homeNameEntry.pack()
homeChangeNameButton=Button(setcontrolpanel, text='Set Home Name', command=set_home_name)
homeChangeNameButton.pack()
homeScore1=Button(controlpanel, text='Score +1', fg='#00ff00', command=increase_home_score_by_1)
homeScore1.grid(column=1, row=2)
homeScore2=Button(controlpanel, text='Score +2', fg='#00ff00', command=increase_home_score_by_2)
homeScore2.grid(column=1, row=3)
homeScore3=Button(controlpanel, text='Score +3', fg='#00ff00', command=increase_home_score_by_3)
homeScore3.grid(column=1, row=4)
homeScore4=Button(controlpanel, text='Score -1', fg='#00ff00', command=decrease_home_score)
homeScore4.grid(column=1, row=5)
fouls1Label=Label(controlpanel, text='  0', bg='black', fg='orange')
fouls1Label.grid(column=1, row=6)
homeAddFoulsButton=Button(controlpanel, text='Foul +', fg='#00ff00', command=increase_home_fouls)
homeAddFoulsButton.grid(column=1, row=7)
homeRemoveFoulsButton=Button(controlpanel, text='Foul -',fg='#00ff00', command=remove_home_fouls)
homeRemoveFoulsButton.grid(column=1, row=8)
tol1Label=Label(controlpanel, text='5', bg='black', fg='orange')
tol1Label.grid(column=2, row=6)
homeAddTolButton=Button(controlpanel, text='TOL +', fg='#00ff00', command=add_home_tol)
homeAddTolButton.grid(column=2, row=7)
homeRemoveTolButton=Button(controlpanel, text='TOL -', fg='#00ff00', command=remove_home_tol)
homeRemoveTolButton.grid(column=2, row=8)
homePossButton=Button(controlpanel, text='←Poss', fg='#00ff00', command=change_poss_to_home)
homePossButton.grid(column=2, row=1)
homeBonusButton=Button(controlpanel, text='←Bonus', fg='#00ff00', command=toggle_home_bonus)
homeBonusButton.grid(column=2, row=2)
guestLabel=Label(controlpanel, text='    0', bg='black', foreground='orange')
guestLabel.grid(column=5, row=1)
guestNameEntry=Entry(setcontrolpanel, state=DISABLED)
guestNameEntry.pack()
guestChangeNameButton=Button(setcontrolpanel, text='Set Guest Name', command=set_guest_name)
guestChangeNameButton.pack()
guestScore1=Button(controlpanel, text='Score +1', fg='red', command=increase_guest_score_by_1)
guestScore1.grid(column=5, row=2)
guestScore2=Button(controlpanel, text='Score +2', fg='red', command=increase_guest_score_by_2)
guestScore2.grid(column=5, row=3)
guestScore3=Button(controlpanel, text='Score +3', fg='red', command=increase_guest_score_by_3)
guestScore3.grid(column=5, row=4)
guestScore4=Button(controlpanel, text='Score -1', fg='red', command=decrease_guest_score)
guestScore4.grid(column=5, row=5)
fouls2Label=Label(controlpanel, text='  0', fg='orange', bg='black')
fouls2Label.grid(column=5, row=6)
guestAddFoulsButton=Button(controlpanel, text='Fouls +', fg='red', command=increase_guest_fouls)
guestAddFoulsButton.grid(column=5, row=7)
guestRemoveFoulsButton=Button(controlpanel, text='Fouls -', fg='red', command=remove_guest_fouls)
guestRemoveFoulsButton.grid(column=5, row=8)
tol2Label=Label(controlpanel, text='5', fg='orange', bg='black')
tol2Label.grid(column=4, row=6)
guestAddTolButton=Button(controlpanel, text='TOL +', fg='red', command=add_guest_tol)
guestAddTolButton.grid(column=4, row=7)
guestRemoveTolButton=Button(controlpanel, text='TOL -', fg='red', command=remove_guest_tol)
guestRemoveTolButton.grid(column=4, row=8)
guestPossButton=Button(controlpanel, text='Poss→', fg='red', command=change_poss_to_guest)
guestPossButton.grid(column=4, row=1)
guestBonusButton=Button(controlpanel, text='Bonus→', fg='red', command=toggle_guest_bonus)
guestBonusButton.grid(column=4, row=2)
periodControl=Label(controlpanel, text='1', bg='black', foreground='orange')
periodControl.grid(column=3, row=7)
periodButton1=Button(controlpanel, text='Previous Period', command=decrease_period)
periodButton1.grid(column=3, row=8)
periodButton2=Button(controlpanel, text='Next Period', command=increase_period)
periodButton2.grid(column=3, row=9)
shotLabel=Label(shotclockcontrolpanel, text='    ', bg='black', foreground='orange')
shotLabel.pack()
shotResetButton1=Button(shotclockcontrolpanel, text='Reset 1', command=reset_1, state=DISABLED)
shotResetButton1.pack()
shotResetButton2=Button(shotclockcontrolpanel, text='Reset 2', command=reset_2, state=DISABLED)
shotResetButton2.pack()
runButton=Scale(shotclockcontrolpanel, sliderlength=40, orient=HORIZONTAL, from_=0, to=1, command=shot_run_stop, state=DISABLED)
runButton.pack()
runStopLabel=Label(shotclockcontrolpanel, text='Stop         Run')
runStopLabel.pack()
autoStopClockButton=Button(setcontrolpanel, state=DISABLED, text='Stop main clock when shot clock expires: OFF', command=auto_stop_clock)
autoStopClockButton.pack()
toggleShotClockButton=Button(setcontrolpanel, text='Enable Shot Clock: OFF', command=toggle_shot_clock)
toggleShotClockButton.pack()
buzzerButton=Button(controlpanel, text='Buzzer')
playerEntry=Entry(controlpanel, state=DISABLED)
playerEntry.grid(column=3, row=10)
foulEntry=Entry(controlpanel, state=DISABLED)
foulEntry.grid(column=3, row=11)
setPlayerFoulButton=Button(controlpanel, text='Set Player Fouls', command=set_player_fouls)
setPlayerFoulButton.grid(column=3, row=12)
buzzerButton.grid(column=3, row=13)
homeTeamLabel=Label(controlpanel, text='HOME', fg='#00ff00')
homeTeamLabel.grid(column=1, row=9)
homeTeamLabel=Label(controlpanel, text='GUEST', fg='red')
homeTeamLabel.grid(column=5, row=9)
buzzerButton.bind('<ButtonPress-1>', start_buzzer_loop)
buzzerButton.bind('<ButtonRelease-1>', stop_buzzer_loop)
scoreboard.mainloop()
