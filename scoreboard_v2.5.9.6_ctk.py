from tkinter import *
import pygame
from tk_tools import *
import time
from tkinter import messagebox
from customtkinter import *
import os, sys
def grp(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
scoreboard=Tk()
shotclock=Tk()
shotclock.seconds=0
shotclock.tenths=0
shotclock.clockState=False
scoreboard.config(bg='black')
scoreboard.grid()
shotclock.clockSwitch=False
scoreboard.title('Display Screen-Scorely v2.5.9.6 ©sserver')
minuteLabel=SevenSegmentDigits(scoreboard, digits=2, background='black', digit_color='yellow', height=100)
minuteLabel.grid(column=3,row=1)
timecolon=Label(scoreboard, text=':', foreground='white', background='black', font=('Century Gothic', 75))
timecolon.grid(column=4, row=1)
secondLabel=SevenSegmentDigits(scoreboard, digits=2, background='black', digit_color='yellow', height=100)
secondLabel.grid(column=5, row=1)
homeScoreLabel=SevenSegmentDigits(scoreboard, digits=3, background='black', digit_color='red', height=100)
homeScoreLabel.grid(column=1, row=3)
guestScoreLabel=SevenSegmentDigits(scoreboard, digits=3, background='black', digit_color='red', height=100)
guestScoreLabel.grid(column=7,row=3)
homeNameLabel=Label(scoreboard, text="HOME", background='black', foreground='orange')
homeNameLabel.grid(column=1,row=2)
shotclock.config(bg='black')
homePossLabel=Label(scoreboard, text="← POSS", background='black', foreground='#001900')
homePossLabel.place(x=0, y=0)
homeBonusLabel=Label(scoreboard, text="← BONUS", background='black', foreground='#190000')
homeBonusLabel.place(x=0, y=50)
guestNameLabel=Label(scoreboard, text="GUEST", background='black', foreground='orange')
guestNameLabel.grid(column=7, row=2)
guestPossLabel=Label(scoreboard, text="POSS →", background='black', foreground='#001900')
guestPossLabel.place(x=600, y=0)
guestBonusLabel=Label(scoreboard, text="BONUS →", background='black', foreground='#190000')
guestBonusLabel.place(x=570, y=50)
homePossLabel.config(font=('Century Gothic', 25))
guestPossLabel.config(font=('Century Gothic', 25))
homeBonusLabel.config(font=('Century Gothic', 25))
guestBonusLabel.config(font=('Century Gothic', 25))
scoreboard.autoHorn=True
scoreboard.endTime=None
periodLabel=SevenSegmentDigits(scoreboard, digits=1, background='black', digit_color='yellow')
periodLabel.grid(column=4, row=3)
periodNameLabel=Label(scoreboard, text='PERIOD', font=('Century Gothic', 25), background='black', foreground='white')
periodNameLabel.grid(column=4, row=2)
homeFoulsNameLabel=Label(scoreboard, text='FOULS', background='black', foreground='white')
homeFoulsNameLabel.grid(column=1, row=4)
homeFoulsLabel=SevenSegmentDigits(scoreboard, digits=2, background='black', digit_color='red', height=100)
homeFoulsLabel.grid(column=1, row=5)
guestFoulsNameLabel=Label(scoreboard, text='FOULS', background='black', foreground='white')
guestFoulsNameLabel.grid(column=7, row=4)
guestFoulsLabel=SevenSegmentDigits(scoreboard, digits=2, background='black', digit_color='red', height=100)
guestFoulsLabel.grid(column=7,row=5)
mainminuteLabel=SevenSegmentDigits(shotclock, digits=2, background='black', digit_color='yellow', height=100)
mainminuteLabel.grid(column=1,row=1)
maintimecolon=Label(shotclock, text=':', foreground='white', background='black', font=('Century Gothic', 75))
maintimecolon.grid(column=2, row=1)
mainsecondLabel=SevenSegmentDigits(shotclock, digits=2, background='black', digit_color='yellow', height=100)
mainsecondLabel.grid(column=3,row=1)
shotclock.title('Shot Clock Screen-Scorely v2.5.9.6 ©sserver')
shotTimeLabel=SevenSegmentDigits(shotclock, digits=2, background='black', digit_color='red', height=200)
playerLabel=SevenSegmentDigits(scoreboard, digits=2, background='black', digit_color='yellow', height=100)
playerLabel.place(x=230, y=320)
playerNameLabel=Label(scoreboard, text='PLAYER    FOUL', background='black', foreground='white', font=('Century Gothic', 25))
playerNameLabel.place(x=230, y=270)
foulLabel=SevenSegmentDigits(scoreboard, digits=1, background='black', digit_color='yellow', height=100)
foulLabel.place(x=390, y=320)
homeTolNameLabel=Label(scoreboard, text='TOL', background='black', foreground='white', font=('Century Gothic', 15))
homeTolNameLabel.grid(column=2, row=4)
guestTolNameLabel=Label(scoreboard, text='TOL', background='black', foreground='white', font=('Century Gothic', 15))
guestTolNameLabel.grid(column=6, row=4)
homeTolLabel=SevenSegmentDigits(scoreboard, digits=1, background='black', digit_color='yellow', height=50)
homeTolLabel.grid(column=2, row=5)
guestTolLabel=SevenSegmentDigits(scoreboard, digits=1, background='black', digit_color='yellow', height=50)
guestTolLabel.grid(column=6,row=5)
shotTimeLabel.place(x=20, y=120)
scoreboard.resizable(False, False)
shotclock.resizable(False, False)
shotclock.reset1=24
shotclock.reset2=14
scoreboard.minutes=20
scoreboard.seconds=0
scoreboard.tenths=0
scoreboard.poss=0
shotclock.enabled=False
scoreboard.homeFouls=0
scoreboard.guestFouls=0
scoreboard.autoStopClock=False
scoreboard.homeBonus=False
scoreboard.guestBonus=False
scoreboard.homeScore=0
scoreboard.homeTol=5
scoreboard.guestTol=5
scoreboard.guestScore=0
scoreboard.period=1
pygame.mixer.init()
channel=pygame.mixer.find_channel()
scoreboard.fast=False
scoreboard.clockState=False
homeNameLabel.config(font=('Century Gothic', 25))
guestNameLabel.config(font=('Century Gothic', 25))
homeFoulsNameLabel.config(font=('Century Gothic', 25))
guestFoulsNameLabel.config(font=('Century Gothic', 25))
scoreboard.homeName='HOME'
scoreboard.guestName='GUEST'
controlpanel=CTk()
controlpanel.homeScoreSet=StringVar()
controlpanel.guestScoreSet=StringVar()
controlpanel.homeFoulsSet=StringVar()
controlpanel.guestFoulsSet=StringVar()
controlpanel.shotClockSet=StringVar()
controlpanel.periodSet=StringVar()
shotclockcontrolpanel=CTkToplevel()
setcontrolpanel=CTkToplevel()
shotclock.geometry('245x340')
scoreboard.geometry('730x450')
scoreboard.player=0
scoreboard.playerfoul=0
setcontrolpanel.title('Options')
controlpanel.title('Control Screen-Scorely v2.5.9.6 ©sserver')
controlpanel.settingReset1=False
controlpanel.settingReset2=False
shotclockcontrolpanel.title('Shot Clock Control Panel')
shotclockcontrolpanel.resizable(False, False)
shotclockcontrolpanel.geometry('200x200')
setcontrolpanel.resizable(False, False)
minuteLabel.set_value('20')
secondLabel.set_value('00')
periodLabel.set_value('1')
homeScoreLabel.set_value('0')
guestScoreLabel.set_value('0')
homeFoulsLabel.set_value('0')
guestFoulsLabel.set_value('0')
shotclock.endTime=None
homeTolLabel.set_value('5')
guestTolLabel.set_value('5')
mainminuteLabel.set_value('20')
mainsecondLabel.set_value('00')
shotclock.timeSaved=False
shotclock.started=False
def shotclock_on_state_change():
    if shotclock.clockState and scoreboard.clockState:
        shotclock.endTime=round(time.time()*10)/10+shotclock.seconds+shotclock.tenths*0.1
        shotclock.timeSaved=False
        shotclock.started=True
    elif shotclock.endTime is not None and not shotclock.timeSaved:
        timeSave=shotclock.endTime-round(time.time()*10)/10
        shotclock.seconds=int(timeSave//1)
        shotclock.tenths=int(timeSave*10)%10
        shotclock.started=False
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
        if shotclock.clockState:
            enabledBefore=True
        else:
            enabledBefore=False
        shotclock.clockState=False
        shotclock_on_state_change()
        shotclock.seconds=shotclock.reset1
        shotclock.tenths=9
        if scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds:
            if shotclock.seconds>9:
                shotTimeLabel.set_value(str(shotclock.seconds))
                shotLabel.configure(text=str(shotclock.seconds))
            else:
                shotTimeLabel.set_value('0'+str(shotclock.seconds))
                shotLabel.configure(text='0'+str(shotclock.seconds))
        else:
            shotTimeLabel.set_value('')
            shotLabel.configure(text='    ')
            enabledBefore=False
        shotclock.clockState=enabledBefore
        shotclock_on_state_change()
    else:
            shotTimeLabel.set_value('')
            shotLabel.configure(text='    ')
    shotclock.update_idletasks()
def reset_2():
    if shotclock.enabled and (not controlpanel.settingReset2):
        if shotclock.clockState:
            enabledBefore=True
        else:
            enabledBefore=False
        shotclock.seconds=shotclock.reset2
        shotclock.tenths=9
        if scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds:
            if shotclock.seconds>9:
                shotTimeLabel.set_value(str(shotclock.seconds))
                shotLabel.configure(text=str(shotclock.seconds))
            else:
                shotTimeLabel.set_value('0'+str(shotclock.seconds))
                shotLabel.configure(text='0'+str(shotclock.seconds))
        else:
            shotTimeLabel.set_value('')
            shotLabel.configure(text='    ')
            enabledBefore=False
        shotclock.clockState=enabledBefore
        shotclock_on_state_change()
    else:
        shotTimeLabel.set_value('')
        shotLabel.configure(text='    ')
    shotclock.update_idletasks()
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
        if scoreboard.clockState:
            timeLeft=scoreboard.endTime-round(time.time()*10)/10
            scoreboard.minutes=int(timeLeft//60)
            scoreboard.seconds=int(timeLeft)%60
            scoreboard.tenths=int(timeLeft*10)%10
            if scoreboard.clockState and timeLeft<=0:
                scoreboard.minutes=0
                scoreboard.seconds=0
                minuteLabel.set_value('00')
                secondLabel.set_value('0')
                mainminuteLabel.set_value('00')
                mainsecondLabel.set_value('0')
                clockLabel.configure(text='00.0  ')
                scoreboard.update_idletasks()
                scoreboard.clockState=False
                if scoreboard.autoHorn:
                    buzzer()
                return
             
            if (scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds) and shotclock.enabled:
                 if shotclock.started and shotclock.seconds>=0:
                    if shotclock.seconds<=0:
                        shotclock.seconds=0
                        shotclock.tenths=0
                        shotTimeLabel.set_value('00')
                        if scoreboard.autoHorn:
                                horn()
                        shotclock.clockState=False
                        shotclock_on_state_change()
                        runButton.deselect()
                        if scoreboard.autoStopClock:
                            scoreboard.clockState=False
                            timeSave=scoreboard.endTime-round(time.time()*10)/10
                            scoreboard.minutes=timeSave//60
                            scoreboard.seconds=(timeSave//1)%60
                            scoreboard.tenths=(timeSave*10)%10
                            return
                    else:
                        shotTimeLeft=shotclock.endTime-round(time.time()*10)/10
                        shotclock.seconds=int(shotTimeLeft//1)
                        shotclock.tenths=int(shotTimeLeft*10)%10
                    if shotclock.seconds<10:
                        shotTimeLabel.set_value('0'+str(shotclock.seconds))
                        shotLabel.configure(text='0'+str(shotclock.seconds))
                    else:
                        shotTimeLabel.set_value(str(shotclock.seconds))
                        shotLabel.configure(text=str(shotclock.seconds))
            else:
                    shotTimeLabel.set_value('')
                    shotLabel.configure(text='    ')
                    shotclock.seconds=0
                    shotclock.tenths=0
                    channel.stop()
                    shotclock.clockState=False
                    shotclock_on_state_change()
                    runButton.deselect()
            if scoreboard.seconds<10 and scoreboard.minutes>0:
                if scoreboard.minutes<10:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value('0'+str(scoreboard.seconds))
                    clockLabel.configure(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value('0'+str(scoreboard.seconds))
                else:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value('0'+str(scoreboard.seconds))
                    clockLabel.configure(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value('0'+str(scoreboard.seconds))
            elif scoreboard.minutes==0:
                if scoreboard.seconds<10:
                    minuteLabel.set_value('0'+str(scoreboard.seconds))
                    secondLabel.set_value(str(scoreboard.tenths))
                    clockLabel.configure(text='0'+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    mainminuteLabel.set_value('0'+str(scoreboard.seconds))
                    mainsecondLabel.set_value(str(scoreboard.tenths))
                else:
                    minuteLabel.set_value(str(scoreboard.seconds))
                    secondLabel.set_value(str(scoreboard.tenths))
                    clockLabel.configure(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    mainminuteLabel.set_value('0'+str(scoreboard.seconds))
                    mainsecondLabel.set_value(str(scoreboard.tenths))
            else:
                if scoreboard.minutes<10:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value(str(scoreboard.seconds))
                    clockLabel.configure(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value(str(scoreboard.seconds))
                else:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value(str(scoreboard.seconds))
                    clockLabel.configure(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value(str(scoreboard.seconds))
            scoreboard.update_idletasks()
            controlpanel.update_idletasks()
            shotclock.update_idletasks()
            scoreboard.after(10, start_time)
def increase_home_score_by_1():
        scoreboard.homeScore+=1
        if scoreboard.homeScore>199:
            scoreboard.homeScore=199
        homeScoreLabel.set_value(str(scoreboard.homeScore))
        if scoreboard.homeScore<10:
            homeLabel.configure(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeLabel.configure(text='  '+str(scoreboard.homeScore))
        else:
            homeLabel.configure(text=str(scoreboard.homeScore))
        scoreboard.update_idletasks()
def increase_home_score_by_2():
        scoreboard.homeScore+=2
        if scoreboard.homeScore>199:
            scoreboard.homeScore=199
        homeScoreLabel.set_value(str(scoreboard.homeScore))
        if scoreboard.homeScore<10:
            homeLabel.configure(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeLabel.configure(text='  '+str(scoreboard.homeScore))
        else:
            homeLabel.configure(text=str(scoreboard.homeScore))
        scoreboard.update_idletasks()  
def increase_home_score_by_3():
        scoreboard.homeScore+=3
        if scoreboard.homeScore>199:
            scoreboard.homeScore=199
        homeScoreLabel.set_value(str(scoreboard.homeScore))
        if scoreboard.homeScore<10:
            homeLabel.configure(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeLabel.configure(text='  '+str(scoreboard.homeScore))
        else:
            homeLabel.configure(text=str(scoreboard.homeScore))
        scoreboard.update_idletasks()
def decrease_home_score():
        if scoreboard.homeScore>0:
            scoreboard.homeScore-=1
        homeScoreLabel.set_value(str(scoreboard.homeScore))
        if scoreboard.homeScore<10:
            homeLabel.configure(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeLabel.configure(text='  '+str(scoreboard.homeScore))
        else:
            homeLabel.configure(text=str(scoreboard.homeScore))
        scoreboard.update_idletasks()
def increase_guest_score_by_1():
        scoreboard.guestScore+=1
        if scoreboard.guestScore>199:
            scoreboard.guestScore=199
        guestScoreLabel.set_value(str(scoreboard.guestScore))
        if scoreboard.guestScore<10:
            guestLabel.configure(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestLabel.configure(text='  '+str(scoreboard.guestScore))
        else:
            guestLabel.configure(text=str(scoreboard.guestScore))
        scoreboard.update_idletasks()
def increase_guest_score_by_2():
        scoreboard.guestScore+=2
        if scoreboard.guestScore>199:
            scoreboard.guestScore=199
        guestScoreLabel.set_value(str(scoreboard.guestScore))
        if scoreboard.guestScore<10:
            guestLabel.configure(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestLabel.configure(text='  '+str(scoreboard.guestScore))
        else:
            guestLabel.configure(text=str(scoreboard.guestScore))
        scoreboard.update_idletasks()
def increase_guest_score_by_3():
        scoreboard.guestScore+=3
        if scoreboard.guestScore>199:
            scoreboard.guestScore=199
        guestScoreLabel.set_value(str(scoreboard.guestScore))
        if scoreboard.guestScore<10:
            guestLabel.configure(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestLabel.configure(text='  '+str(scoreboard.guestScore))
        else:
            guestLabel.configure(text=str(scoreboard.guestScore))
        scoreboard.update_idletasks()
def decrease_guest_score():
        if scoreboard.guestScore>0:
            scoreboard.guestScore-=1
        guestScoreLabel.set_value(str(scoreboard.guestScore))
        if scoreboard.guestScore<10:
            guestLabel.configure(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestLabel.configure(text='  '+str(scoreboard.guestScore))
        else:
            guestLabel.configure(text=str(scoreboard.guestScore))
        scoreboard.update_idletasks()

def decrease_period():
    scoreboard.period-=1
    if scoreboard.period<1:
        scoreboard.period=9
    periodLabel.set_value(str(scoreboard.period))
    periodControl.configure(text=str(scoreboard.period))
    scoreboard.update_idletasks()
    controlpanel.update_idletasks()
def increase_period():
    scoreboard.period+=1
    if scoreboard.period>9:
        scoreboard.period=1
    periodLabel.set_value(str(scoreboard.period))
    periodControl.configure(text=str(scoreboard.period))
    scoreboard.update_idletasks()
    controlpanel.update_idletasks()
controlpanel.resizable(False, False)
controlpanel.settingTime=False
controlpanel.settingHomeName=False
controlpanel.settingGuestName=False
controlpanel.settingHomeScore=False
controlpanel.settingHomeFouls=False
controlpanel.settingGuestScore=False
controlpanel.settingPlayerFouls=False
controlpanel.settingGuestFouls=False
controlpanel.settingShotClock=False
def set_time():
        if controlpanel.settingTime==False and (not scoreboard.clockState):
            minuteEntry.configure(state=NORMAL)
            secondEntry.configure(state=NORMAL)
            setTimeButton.configure(text='Confirm Time')
            controlpanel.settingTime=True
        else:
            try:
                setErrorLabel.configure(text='')
                if int(minuteEntry.get())>99 or int(minuteEntry.get())<0 or int(secondEntry.get())>59 or int(secondEntry.get())<0:
                    setErrorLabel.configure(text='Error: Value(s) are invalid.')
                elif not scoreboard.clockState:
                    scoreboard.minutes=int(minuteEntry.get())
                    scoreboard.seconds=int(secondEntry.get())
                    setTimeButton.configure(text='Set Time')
                    controlpanel.settingTime=False
                    minuteEntry.configure(state=DISABLED)
                    secondEntry.configure(state=DISABLED)
                if scoreboard.seconds<10 and scoreboard.minutes>0:
                    if scoreboard.minutes<10:
                        minuteLabel.set_value(str(scoreboard.minutes))
                        secondLabel.set_value('0'+str(scoreboard.seconds))
                        clockLabel.configure(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                        mainminuteLabel.set_value(str(scoreboard.minutes))
                        mainsecondLabel.set_value('0'+str(scoreboard.seconds))
                    else:
                        minuteLabel.set_value(str(scoreboard.minutes))
                        secondLabel.set_value('0'+str(scoreboard.seconds))
                        clockLabel.configure(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                        mainminuteLabel.set_value(str(scoreboard.minutes))
                        mainsecondLabel.set_value('0'+str(scoreboard.seconds))
                elif scoreboard.minutes==0:
                    if scoreboard.seconds<10:
                        minuteLabel.set_value('0'+str(scoreboard.seconds))
                        secondLabel.set_value(str(scoreboard.tenths))
                        clockLabel.configure(text='0'+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                        mainminuteLabel.set_value('0'+str(scoreboard.seconds))
                        mainsecondLabel.set_value(str(scoreboard.tenths))
                    else:
                        minuteLabel.set_value(str(scoreboard.seconds))
                        secondLabel.set_value(str(scoreboard.tenths))
                        clockLabel.configure(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                        mainminuteLabel.set_value('0'+str(scoreboard.seconds))
                        mainsecondLabel.set_value(str(scoreboard.tenths))
                else:
                    if scoreboard.minutes<10:
                        minuteLabel.set_value(str(scoreboard.minutes))
                        secondLabel.set_value(str(scoreboard.seconds))
                        clockLabel.configure(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                        mainminuteLabel.set_value(str(scoreboard.minutes))
                        mainsecondLabel.set_value(str(scoreboard.seconds))
                    else:
                        minuteLabel.set_value(str(scoreboard.minutes))
                        secondLabel.set_value(str(scoreboard.seconds))
                        clockLabel.configure(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                        mainminuteLabel.set_value(str(scoreboard.minutes))
                        mainsecondLabel.set_value(str(scoreboard.seconds))
                    if (scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds) and shotclock.enabled:
                        if shotclock.seconds<10:
                            shotTimeLabel.set_value('0'+str(shotclock.seconds))
                            shotLabel.configure(text='0'+str(shotclock.seconds))
                        else:
                            shotTimeLabel.set_value(str(shotclock.seconds))
                            shotLabel.configure(text=str(shotclock.seconds))
                    else:
                        shotTimeLabel.set_value('')
                        shotLabel.configure(text='    ')
                        shotclock.clockState=False
                        shotclock_on_state_change()
                        runButton.deselect()
            except ValueError:
                setErrorLabel.configure(text='Error: Value(s) are invalid.')
        scoreboard.update_idletasks()
        controlpanel.update_idletasks()
        shotclock.update_idletasks()

def start_stop():
        if (not scoreboard.clockState) and (scoreboard.minutes>0 or scoreboard.seconds>0) and controlpanel.settingTime==False:
            scoreboard.endTime=round(time.time()*10)/10+scoreboard.minutes*60+scoreboard.seconds+0.1*scoreboard.tenths
            scoreboard.clockState=True
            shotclock_on_state_change()
            start_time()
        else:
            scoreboard.clockState=False
            timeSave=scoreboard.endTime-round(time.time()*10)/10
            scoreboard.minutes=int(timeSave//60)
            scoreboard.seconds=int(timeSave//1)%60
            scoreboard.tenths=int(timeSave*10)%10
            shotclock_on_state_change()
def reset():
        if (not scoreboard.clockState) and (not controlpanel.settingTime):
            if minuteEntry.get()!='':
                scoreboard.minutes=int(minuteEntry.get())
                scoreboard.seconds=int(secondEntry.get())
            else:
                scoreboard.minutes=20
                scoreboard.seconds=0
            scoreboard.tenths=0
            if scoreboard.seconds<10 and scoreboard.minutes>0:
                if scoreboard.minutes<10:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value('0'+str(scoreboard.seconds))
                    clockLabel.configure(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value('0'+str(scoreboard.seconds))
                else:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value('0'+str(scoreboard.seconds))
                    clockLabel.configure(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value('0'+str(scoreboard.seconds))
            elif scoreboard.minutes==0:
                if scoreboard.seconds<10:
                    minuteLabel.set_value('0'+str(scoreboard.seconds))
                    secondLabel.set_value(str(scoreboard.tenths))
                    clockLabel.configure(text='0'+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    mainminuteLabel.set_value('0'+str(scoreboard.seconds))
                    mainsecondLabel.set_value(str(scoreboard.tenths))
                else:
                    minuteLabel.set_value(str(scoreboard.seconds))
                    secondLabel.set_value(str(scoreboard.tenths))
                    clockLabel.configure(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    mainminuteLabel.set_value('0'+str(scoreboard.seconds))
                    mainsecondLabel.set_value(str(scoreboard.tenths))
            else:
                if scoreboard.minutes<10:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value(str(scoreboard.seconds))
                    clockLabel.configure(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value(str(scoreboard.seconds))
                else:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value(str(scoreboard.seconds))
                    clockLabel.configure(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value(str(scoreboard.seconds))
        if (scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds) and shotclock.enabled:
            if shotclock.seconds<10:
                shotTimeLabel.set_value('0'+str(shotclock.seconds))
                shotLabel.configure(text='0'+str(shotclock.seconds))
            else:
                shotTimeLabel.set_value(str(shotclock.seconds))
                shotLabel.configure(text=str(shotclock.seconds))
        else:
            shotTimeLabel.set_value('')
            shotLabel.configure(text='    ')
            shotclock.clockState=False
            shotclock_on_state_change()
            runButton.deselect()
        scoreboard.update_idletasks()
        shotclock.update_idletasks()
        controlpanel.update_idletasks()
        
def shot_run_stop():
    if bool(runButton.get()):
        if (shotclock.seconds>0 or shotclock.tenths>0) and (scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds):
            shotclock.clockState=True
            shotclock_on_state_change()
        else:
            runButton.deselect()
    else:
        shotclock.clockState=False
        shotclock_on_state_change()
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
    homeFoulsLabel.set_value(str(scoreboard.homeFouls))
    if scoreboard.homeFouls<10:
        fouls1Label.configure(text='  '+str(scoreboard.homeFouls))
    else:
        fouls1Label.configure(text=str(scoreboard.homeFouls))
def remove_home_fouls():
    if scoreboard.homeFouls>0:
        scoreboard.homeFouls-=1
    homeFoulsLabel.set_value(str(scoreboard.homeFouls))
    if scoreboard.homeFouls<10:
        fouls1Label.configure(text='  '+str(scoreboard.homeFouls))
    else:
        fouls1Label.configure(text=str(scoreboard.homeFouls))
def increase_guest_fouls():
    if scoreboard.guestFouls<19:
        scoreboard.guestFouls+=1
    guestFoulsLabel.set_value(str(scoreboard.guestFouls))
    if scoreboard.guestFouls<10:
        fouls2Label.configure(text='  '+str(scoreboard.guestFouls))
    else:
        fouls2Label.configure(text=str(scoreboard.guestFouls))
def remove_guest_fouls():
    if scoreboard.guestFouls>0:
        scoreboard.guestFouls-=1
    guestFoulsLabel.set_value(str(scoreboard.guestFouls))
    if scoreboard.guestFouls<10:
        fouls2Label.configure(text='  '+str(scoreboard.guestFouls))
    else:
        fouls2Label.configure(text=str(scoreboard.guestFouls))
def auto_stop_clock():
    if bool(autoStopClockButton.get()):
        scoreboard.autoStopClock=True
    else:
        scoreboard.autoStopClock=False
def set_home_name():
    if not controlpanel.settingHomeName:
        homeChangeNameButton.configure(text='Confirm Name')
        controlpanel.settingHomeName=True
        homeNameEntry.configure(state=NORMAL)
    else:
        if len(homeNameEntry.get())<9:
            if homeNameEntry.get()=='':
                scoreboard.homeName='HOME'
            else:
                scoreboard.homeName=homeNameEntry.get()
            homeNameLabel.configure(text=scoreboard.homeName.upper())
            controlpanel.settingHomeName=False
            homeChangeNameButton.configure(text='Set Name')
            homeNameEntry.configure(state=DISABLED)
        else:
            messagebox.showinfo('Cannot Set Name', 'The name you entered must be 8 letters or less.', icon='error', parent=controlpanel)
def set_guest_name():
    if not controlpanel.settingGuestName:
        guestChangeNameButton.configure(text='Confirm Name')
        controlpanel.settingGuestName=True
        guestNameEntry.configure(state=NORMAL)
    else:
        if len(guestNameEntry.get())<9:
            if guestNameEntry.get()=='':
                scoreboard.guestName='GUEST'
            else:
                scoreboard.guestName=guestNameEntry.get()
            guestNameLabel.configure(text=scoreboard.guestName.upper())
            controlpanel.settingGuestName=False
            guestChangeNameButton.configure(text='Set Name')
            guestNameEntry.configure(state=DISABLED)
        else:
            messagebox.showinfo('Cannot Set Name', 'The name you entered must be 8 letters or less.', icon='error', parent=controlpanel)
def toggle_shot_clock():
    if bool(toggleShotClockButton.get()):
        shotclock.enabled=True
        shotResetButton1.configure(state=NORMAL)
        shotResetButton2.configure(state=NORMAL)
        runButton.configure(state=NORMAL)
        setShotClockButton.configure(state=NORMAL)
        autoStopClockButton.configure(state=NORMAL)
        setReset1Button.configure(state=NORMAL)
        setReset2Button.configure(state=NORMAL)
        if scoreboard.minutes>0 or scoreboard.seconds>24:
                    if shotclock.seconds<10:
                        shotTimeLabel.set_value('0'+str(shotclock.seconds))
                        shotLabel.configure(text='0'+str(shotclock.seconds))
                    else:
                        shotTimeLabel.set_value(str(shotclock.seconds))
                        shotLabel.configure(text=str(shotclock.seconds))
        else:
                        shotTimeLabel.set_value('')
                        shotLabel.configure(text='    ')
                        shotclock.clockState=False
                        shotclock_on_state_change()
                        runButton.deselect()
    elif (not controlpanel.settingShotClock) and (not controlpanel.settingReset1) and (not controlpanel.settingReset2) and not shotclock.clockState:
        shotTimeLabel.set_value('')
        shotLabel.configure(text='    ')
        shotclock.clockState=False
        shotclock.enabled=False
        runButton.deselect()
        setReset1Button.configure(state=DISABLED)
        setReset2Button.configure(state=DISABLED)
        shotResetButton1.configure(state=DISABLED)
        shotResetButton2.configure(state=DISABLED)
        runButton.configure(state=DISABLED)
        autoStopClockButton.deselect()
        scoreboard.autoStopClock=False
        autoStopClockButton.configure(state=DISABLED)
        autoStopClockButton.deselect()
        setShotClockButton.configure(state=DISABLED)
    else:
        toggleShotClockButton.select()
def set_reset_1():
    if not controlpanel.settingReset1:
        controlpanel.settingReset1=True
        reset1Entry.configure(state=NORMAL)
        setErrorLabel.configure(text='')
    else:
        try:
            if int(reset1Entry.get())<=99 and int(reset1Entry.get())>0:
                shotclock.reset1=int(reset1Entry.get())
                controlpanel.settingReset1=False
                reset1Entry.configure(state=DISABLED)
                setErrorLabel.configure(text='')
            elif int(reset1Entry.get())==0:
                shotclock.reset1==24
                controlpanel.settingReset1=False
                reset1Entry.configure(state=DISABLED)
                setErrorLabel.configure(text='')
            else:
                setErrorLabel.configure(text='Error: Value(s) are invalid.')
        except:
            setErrorLabel.configure(text='Error: Value(s) are invalid.')
def set_reset_2():
    if not controlpanel.settingReset2:
        controlpanel.settingReset2=True
        reset2Entry.configure(state=NORMAL)
        setErrorLabel.configure(text='')
    else:
        try:
            if int(reset2Entry.get())<=99 and int(reset2Entry.get())>0:
                shotclock.reset2=int(reset2Entry.get())
                controlpanel.settingReset2=False
                reset2Entry.configure(state=DISABLED)
                setErrorLabel.configure(text='')
            elif int(reset2Entry.get())==0:
                shotclock.reset2=14
                controlpanel.settingReset2=False
                reset2Entry.configure(state=DISABLED)
            else:
                setErrorLabel.configure(text='Error: Value(s) are invalid.')
        except:
            setErrorLabel.configure(text='Error: Value(s) are invalid.')
def set_home_score():
    setErrorLabel.configure(text='')
    if not controlpanel.settingHomeScore:
        homeScoreEntry.configure(state=NORMAL)
        controlpanel.settingHomeScore=True
    else:
        try:
            if homeScoreEntry.get()=='':
                homeScoreEntry.configure(state=DISABLED)
                controlpanel.settingHomeScore=False
            elif int(homeScoreEntry.get())<=199 and int(homeScoreEntry.get())>=0:
                scoreboard.homeScore=int(homeScoreEntry.get())
                homeScoreEntry.configure(state=DISABLED)
                controlpanel.settingHomeScore=False
                controlpanel.homeScoreSet.set('')
                homeScoreLabel.set_value(str(scoreboard.homeScore))
                if scoreboard.homeScore<10:
                    homeLabel.configure(text='    '+str(scoreboard.homeScore))
                elif scoreboard.homeScore<100:
                    homeLabel.configure(text='  '+str(scoreboard.homeScore))
                else:
                    homeLabel.configure(text=str(scoreboard.homeScore))
                scoreboard.update_idletasks()
            else:
                setErrorLabel.configure(text='Error: Value(s) are invalid')
        except ValueError:
            setErrorLabel.configure(text='Error: Value(s) are invalid')
def set_guest_score():
    setErrorLabel.configure(text='')
    if not controlpanel.settingGuestScore:
        guestScoreEntry.configure(state=NORMAL)
        controlpanel.settingGuestScore=True
    else:
        try:
            if guestScoreEntry.get()=='':
                guestScoreEntry.configure(state=DISABLED)
                controlpanel.settingGuestScore=False
            elif int(guestScoreEntry.get())<=199 and int(guestScoreEntry.get())>=0:
                scoreboard.guestScore=int(guestScoreEntry.get())
                guestScoreEntry.configure(state=DISABLED)
                controlpanel.guestScoreSet.set('')
                controlpanel.settingGuestScore=False
                guestScoreLabel.set_value(str(scoreboard.guestScore))
                if scoreboard.guestScore<10:
                    guestLabel.configure(text='    '+str(scoreboard.guestScore))
                elif scoreboard.guestScore<100:
                    guestLabel.configure(text='  '+str(scoreboard.guestScore))
                else:
                    guestLabel.configure(text=str(scoreboard.guestScore))
                scoreboard.update_idletasks()
            else:
                setErrorLabel.configure(text='Error: Value(s) are invalid')
        except ValueError:
            setErrorLabel.configure(text='Error: Value(s) are invalid')
def set_home_fouls():
    setErrorLabel.configure(text='')
    if not controlpanel.settingHomeFouls:
        homeFoulsEntry.configure(state=NORMAL)
        controlpanel.settingHomeFouls=True
    else:
        try:
            if homeFoulsEntry.get()=='':
                homeFoulsEntry.configure(state=DISABLED)
                controlpanel.settingHomeFouls=False
            elif int(homeFoulsEntry.get())<=19 and int(homeFoulsEntry.get())>=0:
                scoreboard.homeFouls=int(homeFoulsEntry.get())
                homeFoulsEntry.configure(state=DISABLED)
                controlpanel.settingHomeFouls=False
                homeFoulsLabel.set_value(str(scoreboard.homeFouls))
                if scoreboard.homeFouls<10:
                    fouls1Label.configure(text='  '+str(scoreboard.homeFouls))
                else:
                    fouls1Label.configure(text=str(scoreboard.homeFouls))
                controlpanel.homeFoulsSet.set('')
                scoreboard.update_idletasks()
            else:
                setErrorLabel.configure(text='Error: Value(s) are invalid')
        except ValueError:
            setErrorLabel.configure(text='Error: Value(s) are invalid')
def set_guest_fouls():
    setErrorLabel.configure(text='')
    if not controlpanel.settingGuestFouls:
        guestFoulsEntry.configure(state=NORMAL)
        controlpanel.settingGuestFouls=True
    else:
        try:
            if guestFoulsEntry.get()=='':
                guestFoulsEntry.configure(state=DISABLED)
                controlpanel.settingGuestFouls=False
            elif int(guestFoulsEntry.get())<=19 and int(guestFoulsEntry.get())>=0:
                scoreboard.guestFouls=int(guestFoulsEntry.get())
                guestFoulsEntry.configure(state=DISABLED)
                controlpanel.settingGuestFouls=False
                guestFoulsLabel.set_value(str(scoreboard.guestFouls))
                if scoreboard.guestFouls<10:
                    fouls2Label.configure(text='  '+str(scoreboard.guestFouls))
                else:
                    fouls2Label.configure(text=str(scoreboard.guestFouls))
                scoreboard.update_idletasks()
            else:
                setErrorLabel.configure(text='Error: Value(s) are invalid')
        except ValueError:
            setErrorLabel.configure(text='Error: Value(s) are invalid')
def set_shot_clock():
    setErrorLabel.configure(text='')
    if (not shotclock.clockState) and (not controlpanel.settingShotClock):
        shotClockEntry.configure(state=NORMAL)
        controlpanel.settingShotClock=True
    elif not shotclock.clockState:
        try:
            if shotClockEntry.get()=='':
                shotClockEntry.configure(state=DISABLED)
                controlpanel.settingShotClock=False
            elif int(shotClockEntry.get())<=99 and int(shotClockEntry.get())>=0:
                shotclock.seconds=int(shotClockEntry.get())
                shotclock.tenths=9
                shotClockEntry.configure(state=DISABLED)
                controlpanel.settingShotClock=False
                if shotclock.enabled and (scoreboard.minutes>0 or scoreboard.seconds>24):
                    if shotclock.seconds>9:
                        shotTimeLabel.set_value(str(shotclock.seconds))
                        shotLabel.configure(text=str(shotclock.seconds))
                    else:
                        shotTimeLabel.set_value('0'+str(shotclock.seconds))
                        shotLabel.configure(text='0'+str(shotclock.seconds))
                else:
                        shotTimeLabel.set_value('')
                scoreboard.update_idletasks()
                shotclock.update_idletasks()
                shotclockcontrolpanel.update_idletasks()
            else:
                setErrorLabel.configure(text='Error: Value(s) are invalid')
        except ValueError:
            setErrorLabel.configure(text='Error: Value(s) are invalid')
def set_player_fouls():
    setErrorLabel.configure(text='')
    if not controlpanel.settingPlayerFouls:
        controlpanel.settingPlayerFouls=True
        playerEntry.configure(state=NORMAL)
        foulEntry.configure(state=NORMAL)
    else:
        if playerEntry.get()=='' or foulEntry.get()=='':
            playerLabel.set_value('')
            foulLabel.set_value('')
            playerEntry.configure(state=DISABLED)
            foulEntry.configure(state=DISABLED)
            controlpanel.settingPlayerFouls=False
        else:
            try:
                if int(playerEntry.get())<=99 and int(playerEntry.get())>=0 and int(foulEntry.get())<=9 and int(foulEntry.get())>=0:
                    scoreboard.player=int(playerEntry.get())
                    scoreboard.playerFoul=int(foulEntry.get())
                    playerLabel.set_value(str(scoreboard.player))
                    foulLabel.set_value(str(scoreboard.playerFoul))
                    playerEntry.configure(state=DISABLED)
                    foulEntry.configure(state=DISABLED)
                    controlpanel.settingPlayerFouls=False
                else:
                    setErrorLabel.configure(text='Error: Value(s) are invalid')
            except ValueError:
                setErrorLabel.configure(text='Error: Value(s) are invalid')
def add_home_tol():
    if scoreboard.homeTol<9:
        scoreboard.homeTol+=1
    homeTolLabel.set_value(str(scoreboard.homeTol))
    tol1Label.configure(text=str(scoreboard.homeTol))
def remove_home_tol():
    if scoreboard.homeTol>0:
        scoreboard.homeTol-=1
    homeTolLabel.set_value(str(scoreboard.homeTol))
    tol1Label.configure(text=str(scoreboard.homeTol))
def add_guest_tol():
    if scoreboard.guestTol<9:
        scoreboard.guestTol+=1
    guestTolLabel.set_value(str(scoreboard.guestTol))
    tol2Label.configure(text=str(scoreboard.guestTol))
def remove_guest_tol():
    if scoreboard.guestTol>0:
        scoreboard.guestTol-=1
    guestTolLabel.set_value(str(scoreboard.guestTol))
    tol2Label.configure(text=str(scoreboard.guestTol))
controlpanel.grid()
setErrorLabel=CTkLabel(setcontrolpanel, text='', text_color=('red', 'red'))
setErrorLabel.pack()
clockLabel=CTkLabel(controlpanel, text='20:00', fg_color=('black','black'), text_color=('orange','orange'))   
clockLabel.grid(column=3, row=1)
minuteEntry=CTkEntry(controlpanel, state=DISABLED)
minuteEntry.grid(column=3, row=2)
secondEntry=CTkEntry(controlpanel, state=DISABLED)
secondEntry.grid(column=3, row=3)
setTimeButton=CTkButton(controlpanel, text='Set Time', command=set_time, state=NORMAL)
setTimeButton.grid(column=3, row=4)
startStopButton=CTkButton(controlpanel, text='Start/Stop', command=start_stop)
startStopButton.grid(column=3, row=5)
reset1Entry=CTkEntry(setcontrolpanel, state=DISABLED)
reset1Entry.pack()
setReset1Button=CTkButton(setcontrolpanel, state=DISABLED, text='Set Shot Clock Reset 1', command=set_reset_1)
setReset1Button.pack()
reset2Entry=CTkEntry(setcontrolpanel, state=DISABLED)
reset2Entry.pack()
setReset2Button=CTkButton(setcontrolpanel, state=DISABLED, text='Set Shot Clock Reset 2', command=set_reset_2)
setReset2Button.pack()
homeScoreEntry=CTkEntry(setcontrolpanel, textvariable=controlpanel.homeScoreSet, state=DISABLED)
homeScoreEntry.pack()
setHomeScoreButton=CTkButton(setcontrolpanel, text='Set Home Score', command=set_home_score)
setHomeScoreButton.pack()
guestScoreEntry=CTkEntry(setcontrolpanel, textvariable=controlpanel.guestScoreSet, state=DISABLED)
guestScoreEntry.pack()
setGuestScoreButton=CTkButton(setcontrolpanel, text='Set Guest Score',command=set_guest_score)
setGuestScoreButton.pack()
homeFoulsEntry=CTkEntry(setcontrolpanel, textvariable=controlpanel.homeFoulsSet, state=DISABLED)
homeFoulsEntry.pack()
setHomeFoulsButton=CTkButton(setcontrolpanel, text='Set Home Fouls', command=set_home_fouls)
setHomeFoulsButton.pack()
guestFoulsEntry=CTkEntry(setcontrolpanel, textvariable=controlpanel.guestFoulsSet, state=DISABLED)
guestFoulsEntry.pack()
setGuestFoulsButton=CTkButton(setcontrolpanel, text='Set Guest Fouls', command=set_guest_fouls)
setGuestFoulsButton.pack()
shotClockEntry=CTkEntry(setcontrolpanel, textvariable=controlpanel.shotClockSet, state=DISABLED)
shotClockEntry.pack()
setShotClockButton=CTkButton(setcontrolpanel, text='Set Shot Clock', state=DISABLED, command=set_shot_clock)
setShotClockButton.pack()
resetButton=CTkButton(controlpanel, text='Reset', command=reset)
resetButton.grid(column=3, row=6)
homeLabel=CTkLabel(controlpanel, text='    0', fg_color=('black','black'), text_color=('orange','orange'))
homeLabel.grid(column=1, row=1)
homeNameEntry=CTkEntry(setcontrolpanel, state=DISABLED)
homeNameEntry.pack()
homeChangeNameButton=CTkButton(setcontrolpanel, text='Set Home Name', command=set_home_name)
homeChangeNameButton.pack()
homeScore1=CTkButton(controlpanel, text='Score +1', command=increase_home_score_by_1)
homeScore1.grid(column=1, row=2)
homeScore2=CTkButton(controlpanel, text='Score +2', command=increase_home_score_by_2)
homeScore2.grid(column=1, row=3)
homeScore3=CTkButton(controlpanel, text='Score +3', command=increase_home_score_by_3)
homeScore3.grid(column=1, row=4)
homeScore4=CTkButton(controlpanel, text='Score -1', command=decrease_home_score)
homeScore4.grid(column=1, row=5)
fouls1Label=CTkLabel(controlpanel, text='  0', fg_color=('black','black'), text_color=('orange','orange'))
fouls1Label.grid(column=1, row=6)
homeAddFoulsButton=CTkButton(controlpanel, text='Foul +', command=increase_home_fouls)
homeAddFoulsButton.grid(column=1, row=7)
homeRemoveFoulsButton=CTkButton(controlpanel, text='Foul -', command=remove_home_fouls)
homeRemoveFoulsButton.grid(column=1, row=8)
tol1Label=CTkLabel(controlpanel, text='5', fg_color=('black','black'), text_color=('orange','orange'))
tol1Label.grid(column=2, row=6)
homeAddTolButton=CTkButton(controlpanel, text='TOL +', command=add_home_tol)
homeAddTolButton.grid(column=2, row=7)
homeRemoveTolButton=CTkButton(controlpanel, text='TOL -', command=remove_home_tol)
homeRemoveTolButton.grid(column=2, row=8)
homePossButton=CTkButton(controlpanel, text='←Poss', command=change_poss_to_home)
homePossButton.grid(column=2, row=1)
homeBonusButton=CTkButton(controlpanel, text='←Bonus',  command=toggle_home_bonus)
homeBonusButton.grid(column=2, row=2)
guestLabel=CTkLabel(controlpanel, text='    0', fg_color=('black','black'), text_color=('orange','orange'))
guestLabel.grid(column=5, row=1)
guestNameEntry=CTkEntry(setcontrolpanel, state=DISABLED)
guestNameEntry.pack()
guestChangeNameButton=CTkButton(setcontrolpanel, text='Set Guest Name', command=set_guest_name)
guestChangeNameButton.pack()
guestScore1=CTkButton(controlpanel, text='Score +1', command=increase_guest_score_by_1)
guestScore1.grid(column=5, row=2)
guestScore2=CTkButton(controlpanel, text='Score +2', command=increase_guest_score_by_2)
guestScore2.grid(column=5, row=3)
guestScore3=CTkButton(controlpanel, text='Score +3', command=increase_guest_score_by_3)
guestScore3.grid(column=5, row=4)
guestScore4=CTkButton(controlpanel, text='Score -1', command=decrease_guest_score)
guestScore4.grid(column=5, row=5)
fouls2Label=CTkLabel(controlpanel, text='  0', fg_color=('black','black'), text_color=('orange','orange'))
fouls2Label.grid(column=5, row=6)
guestAddFoulsButton=CTkButton(controlpanel, text='Foul +', command=increase_guest_fouls)
guestAddFoulsButton.grid(column=5, row=7)
guestRemoveFoulsButton=CTkButton(controlpanel, text='Foul -', command=remove_guest_fouls)
guestRemoveFoulsButton.grid(column=5, row=8)
tol2Label=CTkLabel(controlpanel, text='5', fg_color=('black','black'), text_color=('orange','orange'))
tol2Label.grid(column=4, row=6)
guestAddTolButton=CTkButton(controlpanel, text='TOL +', command=add_guest_tol)
guestAddTolButton.grid(column=4, row=7)
guestRemoveTolButton=CTkButton(controlpanel, text='TOL -', command=remove_guest_tol)
guestRemoveTolButton.grid(column=4, row=8)
guestPossButton=CTkButton(controlpanel, text='Poss→', command=change_poss_to_guest)
guestPossButton.grid(column=4, row=1)
guestBonusButton=CTkButton(controlpanel, text='Bonus→', command=toggle_guest_bonus)
guestBonusButton.grid(column=4, row=2)
periodControl=CTkLabel(controlpanel, text='1', fg_color=('black','black'), text_color=('orange','orange'))
periodControl.grid(column=3, row=7)
periodButton1=CTkButton(controlpanel, text='Previous Period', command=decrease_period)
periodButton1.grid(column=3, row=8)
periodButton2=CTkButton(controlpanel, text='Next Period', command=increase_period)
periodButton2.grid(column=3, row=9)
shotLabel=CTkLabel(shotclockcontrolpanel, text='    ', fg_color=('black','black'), text_color=('orange','orange'))
shotLabel.pack()
shotResetButton1=CTkButton(shotclockcontrolpanel, text='Reset 1', command=reset_1, state=DISABLED)
shotResetButton1.pack()
shotResetButton2=CTkButton(shotclockcontrolpanel, text='Reset 2', command=reset_2, state=DISABLED)
shotResetButton2.pack()
runButton=CTkSwitch(shotclockcontrolpanel, text='Time In', command=shot_run_stop)
runButton.pack()
autoStopClockButton=CTkSwitch(setcontrolpanel, state=DISABLED, text='Stop main clock when shot clock expires', command=auto_stop_clock)
autoStopClockButton.pack()
toggleShotClockButton=CTkSwitch(setcontrolpanel, text='Enable Shot Clock', command=toggle_shot_clock)
toggleShotClockButton.pack()
buzzerButton=CTkButton(controlpanel, text='Buzzer')
playerEntry=CTkEntry(controlpanel, state=DISABLED)
playerEntry.grid(column=3, row=10)
foulEntry=CTkEntry(controlpanel, state=DISABLED)
foulEntry.grid(column=3, row=11)
setPlayerFoulButton=CTkButton(controlpanel, text='Set Player Fouls', command=set_player_fouls)
setPlayerFoulButton.grid(column=3, row=12)
buzzerButton.grid(column=3, row=13)
homeTeamLabel=CTkLabel(controlpanel, text='HOME', text_color=('#00ff00','#00ff00'))
homeTeamLabel.grid(column=1, row=9)
homeTeamLabel=CTkLabel(controlpanel, text='GUEST', text_color=('red','red'))
homeTeamLabel.grid(column=5, row=9)
buzzerButton.bind('<ButtonPress-1>', start_buzzer_loop)
buzzerButton.bind('<ButtonRelease-1>', stop_buzzer_loop)
runButton.configure(state=DISABLED)
scoreboard.iconbitmap(grp('shotclock.ico'))
shotclock.iconbitmap(grp('shotclock.ico'))
controlpanel.iconbitmap(grp('shotclock.ico'))
shotclockcontrolpanel.iconbitmap(grp('shotclock.ico'))
setcontrolpanel.iconbitmap(grp('shotclock.ico'))
controlpanel.mainloop()
