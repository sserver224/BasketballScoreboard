from tkinter import *
import pygame
from tk_tools import *
import time
from tkinter import messagebox
from tkinter.ttk import *
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
controlpanel=Tk()
controlpanel.homeScoreSet=StringVar()
controlpanel.guestScoreSet=StringVar()
controlpanel.homeFoulsSet=StringVar()
controlpanel.guestFoulsSet=StringVar()
controlpanel.shotClockSet=StringVar()
controlpanel.periodSet=StringVar()
shotclockcontrolpanel=Tk()
setcontrolpanel=Tk()
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
setcontrolpanel.geometry('250x560')
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
                shotLabel.config(text=str(shotclock.seconds))
            else:
                shotTimeLabel.set_value('0'+str(shotclock.seconds))
                shotLabel.config(text='0'+str(shotclock.seconds))
        else:
            shotTimeLabel.set_value('')
            shotLabel.config(text='    ')
            enabledBefore=False
        shotclock.clockState=enabledBefore
        shotclock_on_state_change()
    else:
            shotTimeLabel.set_value('')
            shotLabel.config(text='    ')
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
                shotLabel.config(text=str(shotclock.seconds))
            else:
                shotTimeLabel.set_value('0'+str(shotclock.seconds))
                shotLabel.config(text='0'+str(shotclock.seconds))
        else:
            shotTimeLabel.set_value('')
            shotLabel.config(text='    ')
            enabledBefore=False
        shotclock.clockState=enabledBefore
        shotclock_on_state_change()
    else:
        shotTimeLabel.set_value('')
        shotLabel.config(text='    ')
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
                clockLabel.config(text='00.0  ')
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
                        runButton.state(['!selected'])
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
                        shotLabel.config(text='0'+str(shotclock.seconds))
                    else:
                        shotTimeLabel.set_value(str(shotclock.seconds))
                        shotLabel.config(text=str(shotclock.seconds))
            else:
                    shotTimeLabel.set_value('')
                    shotLabel.config(text='    ')
                    shotclock.seconds=0
                    shotclock.tenths=0
                    channel.stop()
                    shotclock.clockState=False
                    shotclock_on_state_change()
                    runButton.state(['!selected'])
            if scoreboard.seconds<10 and scoreboard.minutes>0:
                if scoreboard.minutes<10:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value('0'+str(scoreboard.seconds))
                    clockLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value('0'+str(scoreboard.seconds))
                else:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value('0'+str(scoreboard.seconds))
                    clockLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value('0'+str(scoreboard.seconds))
            elif scoreboard.minutes==0:
                if scoreboard.seconds<10:
                    minuteLabel.set_value('0'+str(scoreboard.seconds))
                    secondLabel.set_value(str(scoreboard.tenths))
                    clockLabel.config(text='0'+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    mainminuteLabel.set_value('0'+str(scoreboard.seconds))
                    mainsecondLabel.set_value(str(scoreboard.tenths))
                else:
                    minuteLabel.set_value(str(scoreboard.seconds))
                    secondLabel.set_value(str(scoreboard.tenths))
                    clockLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    mainminuteLabel.set_value('0'+str(scoreboard.seconds))
                    mainsecondLabel.set_value(str(scoreboard.tenths))
            else:
                if scoreboard.minutes<10:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value(str(scoreboard.seconds))
                    clockLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value(str(scoreboard.seconds))
                else:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value(str(scoreboard.seconds))
                    clockLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
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
            homeLabel.config(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeLabel.config(text='  '+str(scoreboard.homeScore))
        else:
            homeLabel.config(text=str(scoreboard.homeScore))
        scoreboard.update_idletasks()
def increase_home_score_by_2():
        scoreboard.homeScore+=2
        if scoreboard.homeScore>199:
            scoreboard.homeScore=199
        homeScoreLabel.set_value(str(scoreboard.homeScore))
        if scoreboard.homeScore<10:
            homeLabel.config(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeLabel.config(text='  '+str(scoreboard.homeScore))
        else:
            homeLabel.config(text=str(scoreboard.homeScore))
        scoreboard.update_idletasks()  
def increase_home_score_by_3():
        scoreboard.homeScore+=3
        if scoreboard.homeScore>199:
            scoreboard.homeScore=199
        homeScoreLabel.set_value(str(scoreboard.homeScore))
        if scoreboard.homeScore<10:
            homeLabel.config(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeLabel.config(text='  '+str(scoreboard.homeScore))
        else:
            homeLabel.config(text=str(scoreboard.homeScore))
        scoreboard.update_idletasks()
def decrease_home_score():
        if scoreboard.homeScore>0:
            scoreboard.homeScore-=1
        homeScoreLabel.set_value(str(scoreboard.homeScore))
        if scoreboard.homeScore<10:
            homeLabel.config(text='    '+str(scoreboard.homeScore))
        elif scoreboard.homeScore<100:
            homeLabel.config(text='  '+str(scoreboard.homeScore))
        else:
            homeLabel.config(text=str(scoreboard.homeScore))
        scoreboard.update_idletasks()
def increase_guest_score_by_1():
        scoreboard.guestScore+=1
        if scoreboard.guestScore>199:
            scoreboard.guestScore=199
        guestScoreLabel.set_value(str(scoreboard.guestScore))
        if scoreboard.guestScore<10:
            guestLabel.config(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestLabel.config(text='  '+str(scoreboard.guestScore))
        else:
            guestLabel.config(text=str(scoreboard.guestScore))
        scoreboard.update_idletasks()
def increase_guest_score_by_2():
        scoreboard.guestScore+=2
        if scoreboard.guestScore>199:
            scoreboard.guestScore=199
        guestScoreLabel.set_value(str(scoreboard.guestScore))
        if scoreboard.guestScore<10:
            guestLabel.config(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestLabel.config(text='  '+str(scoreboard.guestScore))
        else:
            guestLabel.config(text=str(scoreboard.guestScore))
        scoreboard.update_idletasks()
def increase_guest_score_by_3():
        scoreboard.guestScore+=3
        if scoreboard.guestScore>199:
            scoreboard.guestScore=199
        guestScoreLabel.set_value(str(scoreboard.guestScore))
        if scoreboard.guestScore<10:
            guestLabel.config(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestLabel.config(text='  '+str(scoreboard.guestScore))
        else:
            guestLabel.config(text=str(scoreboard.guestScore))
        scoreboard.update_idletasks()
def decrease_guest_score():
        if scoreboard.guestScore>0:
            scoreboard.guestScore-=1
        guestScoreLabel.set_value(str(scoreboard.guestScore))
        if scoreboard.guestScore<10:
            guestLabel.config(text='    '+str(scoreboard.guestScore))
        elif scoreboard.guestScore<100:
            guestLabel.config(text='  '+str(scoreboard.guestScore))
        else:
            guestLabel.config(text=str(scoreboard.guestScore))
        scoreboard.update_idletasks()

def decrease_period():
    scoreboard.period-=1
    if scoreboard.period<1:
        scoreboard.period=9
    periodLabel.set_value(str(scoreboard.period))
    periodControl.config(text=str(scoreboard.period))
    scoreboard.update_idletasks()
    controlpanel.update_idletasks()
def increase_period():
    scoreboard.period+=1
    if scoreboard.period>9:
        scoreboard.period=1
    periodLabel.set_value(str(scoreboard.period))
    periodControl.config(text=str(scoreboard.period))
    scoreboard.update_idletasks()
    controlpanel.update_idletasks()
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
controlpanel.settingPlayerFouls=False
controlpanel.settingGuestFouls=False
controlpanel.settingShotClock=False
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
                        minuteLabel.set_value(str(scoreboard.minutes))
                        secondLabel.set_value('0'+str(scoreboard.seconds))
                        clockLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                        mainminuteLabel.set_value(str(scoreboard.minutes))
                        mainsecondLabel.set_value('0'+str(scoreboard.seconds))
                    else:
                        minuteLabel.set_value(str(scoreboard.minutes))
                        secondLabel.set_value('0'+str(scoreboard.seconds))
                        clockLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                        mainminuteLabel.set_value(str(scoreboard.minutes))
                        mainsecondLabel.set_value('0'+str(scoreboard.seconds))
                elif scoreboard.minutes==0:
                    if scoreboard.seconds<10:
                        minuteLabel.set_value('0'+str(scoreboard.seconds))
                        secondLabel.set_value(str(scoreboard.tenths))
                        clockLabel.config(text='0'+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                        mainminuteLabel.set_value('0'+str(scoreboard.seconds))
                        mainsecondLabel.set_value(str(scoreboard.tenths))
                    else:
                        minuteLabel.set_value(str(scoreboard.seconds))
                        secondLabel.set_value(str(scoreboard.tenths))
                        clockLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                        mainminuteLabel.set_value('0'+str(scoreboard.seconds))
                        mainsecondLabel.set_value(str(scoreboard.tenths))
                else:
                    if scoreboard.minutes<10:
                        minuteLabel.set_value(str(scoreboard.minutes))
                        secondLabel.set_value(str(scoreboard.seconds))
                        clockLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                        mainminuteLabel.set_value(str(scoreboard.minutes))
                        mainsecondLabel.set_value(str(scoreboard.seconds))
                    else:
                        minuteLabel.set_value(str(scoreboard.minutes))
                        secondLabel.set_value(str(scoreboard.seconds))
                        clockLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                        mainminuteLabel.set_value(str(scoreboard.minutes))
                        mainsecondLabel.set_value(str(scoreboard.seconds))
                    if (scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds) and shotclock.enabled:
                        if shotclock.seconds<10:
                            shotTimeLabel.set_value('0'+str(shotclock.seconds))
                            shotLabel.config(text='0'+str(shotclock.seconds))
                        else:
                            shotTimeLabel.set_value(str(shotclock.seconds))
                            shotLabel.config(text=str(shotclock.seconds))
                    else:
                        shotTimeLabel.set_value('')
                        shotLabel.config(text='    ')
                        shotclock.clockState=False
                        shotclock_on_state_change()
                        runButton.state(['!selected'])
            except ValueError:
                setErrorLabel.config(text='Error: Value(s) are invalid.')
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
            scoreboard.minutes=int(minuteEntry.get()) if minuteEntry.get()!='' else 20
            scoreboard.seconds=int(secondEntry.get()) if secondEntry.get()!='' else 0
            scoreboard.tenths=0
            if scoreboard.seconds<10 and scoreboard.minutes>0:
                if scoreboard.minutes<10:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value('0'+str(scoreboard.seconds))
                    clockLabel.config(text='  '+str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value('0'+str(scoreboard.seconds))
                else:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value('0'+str(scoreboard.seconds))
                    clockLabel.config(text=str(scoreboard.minutes)+':0'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value('0'+str(scoreboard.seconds))
            elif scoreboard.minutes==0:
                if scoreboard.seconds<10:
                    minuteLabel.set_value('0'+str(scoreboard.seconds))
                    secondLabel.set_value(str(scoreboard.tenths))
                    clockLabel.config(text='0'+str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    mainminuteLabel.set_value('0'+str(scoreboard.seconds))
                    mainsecondLabel.set_value(str(scoreboard.tenths))
                else:
                    minuteLabel.set_value(str(scoreboard.seconds))
                    secondLabel.set_value(str(scoreboard.tenths))
                    clockLabel.config(text=str(scoreboard.seconds)+'.'+str(scoreboard.tenths)+'  ')
                    mainminuteLabel.set_value('0'+str(scoreboard.seconds))
                    mainsecondLabel.set_value(str(scoreboard.tenths))
            else:
                if scoreboard.minutes<10:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value(str(scoreboard.seconds))
                    clockLabel.config(text='  '+str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value(str(scoreboard.seconds))
                else:
                    minuteLabel.set_value(str(scoreboard.minutes))
                    secondLabel.set_value(str(scoreboard.seconds))
                    clockLabel.config(text=str(scoreboard.minutes)+':'+str(scoreboard.seconds))
                    mainminuteLabel.set_value(str(scoreboard.minutes))
                    mainsecondLabel.set_value(str(scoreboard.seconds))
        if (scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds) and shotclock.enabled:
            if shotclock.seconds<10:
                shotTimeLabel.set_value('0'+str(shotclock.seconds))
                shotLabel.config(text='0'+str(shotclock.seconds))
            else:
                shotTimeLabel.set_value(str(shotclock.seconds))
                shotLabel.config(text=str(shotclock.seconds))
        else:
            shotTimeLabel.set_value('')
            shotLabel.config(text='    ')
            shotclock.clockState=False
            shotclock_on_state_change()
            runButton.state(['!selected'])
        scoreboard.update_idletasks()
        shotclock.update_idletasks()
        controlpanel.update_idletasks()
        
def shot_run_stop():
    if runButton.instate(['selected']):
        if (shotclock.seconds>0 or shotclock.tenths>0) and (scoreboard.minutes>0 or scoreboard.seconds>shotclock.seconds):
            shotclock.clockState=True
            shotclock_on_state_change()
        else:
            runButton.state(['!selected'])
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
        fouls1Label.config(text='  '+str(scoreboard.homeFouls))
    else:
        fouls1Label.config(text=str(scoreboard.homeFouls))
def remove_home_fouls():
    if scoreboard.homeFouls>0:
        scoreboard.homeFouls-=1
    homeFoulsLabel.set_value(str(scoreboard.homeFouls))
    if scoreboard.homeFouls<10:
        fouls1Label.config(text='  '+str(scoreboard.homeFouls))
    else:
        fouls1Label.config(text=str(scoreboard.homeFouls))
def increase_guest_fouls():
    if scoreboard.guestFouls<19:
        scoreboard.guestFouls+=1
    guestFoulsLabel.set_value(str(scoreboard.guestFouls))
    if scoreboard.guestFouls<10:
        fouls2Label.config(text='  '+str(scoreboard.guestFouls))
    else:
        fouls2Label.config(text=str(scoreboard.guestFouls))
def remove_guest_fouls():
    if scoreboard.guestFouls>0:
        scoreboard.guestFouls-=1
    guestFoulsLabel.set_value(str(scoreboard.guestFouls))
    if scoreboard.guestFouls<10:
        fouls2Label.config(text='  '+str(scoreboard.guestFouls))
    else:
        fouls2Label.config(text=str(scoreboard.guestFouls))
def auto_stop_clock():
    if autoStopClockButton.instate(['selected']):
        scoreboard.autoStopClock=True
    else:
        scoreboard.autoStopClock=False
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
            messagebox.showinfo('Cannot Set Name', 'The name you entered must be 8 letters or less.', icon='error', parent=controlpanel)
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
            messagebox.showinfo('Cannot Set Name', 'The name you entered must be 8 letters or less.', icon='error', parent=controlpanel)
def toggle_shot_clock():
    if toggleShotClockButton.instate(['selected']):
        shotclock.enabled=True
        shotResetButton1.config(state=NORMAL)
        shotResetButton2.config(state=NORMAL)
        runButton.config(state=NORMAL)
        setShotClockButton.config(state=NORMAL)
        autoStopClockButton.config(state=NORMAL)
        setReset1Button.config(state=NORMAL)
        setReset2Button.config(state=NORMAL)
        runButton.state(['!alternate'])
        autoStopClockButton.state(['!alternate'])
        if scoreboard.minutes>0 or scoreboard.seconds>24:
                    if shotclock.seconds<10:
                        shotTimeLabel.set_value('0'+str(shotclock.seconds))
                        shotLabel.config(text='0'+str(shotclock.seconds))
                    else:
                        shotTimeLabel.set_value(str(shotclock.seconds))
                        shotLabel.config(text=str(shotclock.seconds))
        else:
                        shotTimeLabel.set_value('')
                        shotLabel.config(text='    ')
                        shotclock.clockState=False
                        shotclock_on_state_change()
                        runButton.state(['!selected'])
    elif (not controlpanel.settingShotClock) and (not controlpanel.settingReset1) and (not controlpanel.settingReset2) and not shotclock.clockState:
        shotTimeLabel.set_value('')
        shotLabel.config(text='    ')
        shotclock.clockState=False
        shotclock.enabled=False
        runButton.state(['!selected'])
        setReset1Button.config(state=DISABLED)
        setReset2Button.config(state=DISABLED)
        shotResetButton1.config(state=DISABLED)
        shotResetButton2.config(state=DISABLED)
        runButton.config(state=DISABLED)
        runButton.state(['!alternate'])
        autoStopClockButton.state(['!selected'])
        scoreboard.autoStopClock=False
        autoStopClockButton.config(state=DISABLED)
        autoStopClockButton.state(['!alternate'])
        autoStopClockButton.state(['!selected'])
        setShotClockButton.config(state=DISABLED)
    else:
        toggleShotClockButton.state(['selected'])
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
                homeScoreLabel.set_value(str(scoreboard.homeScore))
                if scoreboard.homeScore<10:
                    homeLabel.config(text='    '+str(scoreboard.homeScore))
                elif scoreboard.homeScore<100:
                    homeLabel.config(text='  '+str(scoreboard.homeScore))
                else:
                    homeLabel.config(text=str(scoreboard.homeScore))
                scoreboard.update_idletasks()
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
                guestScoreLabel.set_value(str(scoreboard.guestScore))
                if scoreboard.guestScore<10:
                    guestLabel.config(text='    '+str(scoreboard.guestScore))
                elif scoreboard.guestScore<100:
                    guestLabel.config(text='  '+str(scoreboard.guestScore))
                else:
                    guestLabel.config(text=str(scoreboard.guestScore))
                scoreboard.update_idletasks()
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
                homeFoulsLabel.set_value(str(scoreboard.homeFouls))
                if scoreboard.homeFouls<10:
                    fouls1Label.config(text='  '+str(scoreboard.homeFouls))
                else:
                    fouls1Label.config(text=str(scoreboard.homeFouls))
                controlpanel.homeFoulsSet.set('')
                scoreboard.update_idletasks()
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
                guestFoulsLabel.set_value(str(scoreboard.guestFouls))
                if scoreboard.guestFouls<10:
                    fouls2Label.config(text='  '+str(scoreboard.guestFouls))
                else:
                    fouls2Label.config(text=str(scoreboard.guestFouls))
                scoreboard.update_idletasks()
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
                shotclock.tenths=9
                shotClockEntry.config(state=DISABLED)
                controlpanel.settingShotClock=False
                if shotclock.enabled and (scoreboard.minutes>0 or scoreboard.seconds>24):
                    if shotclock.seconds>9:
                        shotTimeLabel.set_value(str(shotclock.seconds))
                        shotLabel.config(text=str(shotclock.seconds))
                    else:
                        shotTimeLabel.set_value('0'+str(shotclock.seconds))
                        shotLabel.config(text='0'+str(shotclock.seconds))
                else:
                        shotTimeLabel.set_value('')
                scoreboard.update_idletasks()
                shotclock.update_idletasks()
                shotclockcontrolpanel.update_idletasks()
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
            playerLabel.set_value('')
            foulLabel.set_value('')
            playerEntry.config(state=DISABLED)
            foulEntry.config(state=DISABLED)
            controlpanel.settingPlayerFouls=False
        else:
            try:
                if int(playerEntry.get())<=99 and int(playerEntry.get())>=0 and int(foulEntry.get())<=9 and int(foulEntry.get())>=0:
                    scoreboard.player=int(playerEntry.get())
                    scoreboard.playerFoul=int(foulEntry.get())
                    playerLabel.set_value(str(scoreboard.player))
                    foulLabel.set_value(str(scoreboard.playerFoul))
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
    homeTolLabel.set_value(str(scoreboard.homeTol))
    tol1Label.config(text=str(scoreboard.homeTol))
def remove_home_tol():
    if scoreboard.homeTol>0:
        scoreboard.homeTol-=1
    homeTolLabel.set_value(str(scoreboard.homeTol))
    tol1Label.config(text=str(scoreboard.homeTol))
def add_guest_tol():
    if scoreboard.guestTol<9:
        scoreboard.guestTol+=1
    guestTolLabel.set_value(str(scoreboard.guestTol))
    tol2Label.config(text=str(scoreboard.guestTol))
def remove_guest_tol():
    if scoreboard.guestTol>0:
        scoreboard.guestTol-=1
    guestTolLabel.set_value(str(scoreboard.guestTol))
    tol2Label.config(text=str(scoreboard.guestTol))
controlpanel.grid()
setErrorLabel=Label(setcontrolpanel, text='', foreground='red')
setErrorLabel.pack()
clockLabel=Label(controlpanel, text='20:00', background='black', foreground='orange')   
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
homeLabel=Label(controlpanel, text='    0', background='black', foreground='orange')
homeLabel.grid(column=1, row=1)
homeNameEntry=Entry(setcontrolpanel, state=DISABLED)
homeNameEntry.pack()
homeChangeNameButton=Button(setcontrolpanel, text='Set Home Name', command=set_home_name)
homeChangeNameButton.pack()
homeScore1=Button(controlpanel, text='Score +1', command=increase_home_score_by_1)
homeScore1.grid(column=1, row=2)
homeScore2=Button(controlpanel, text='Score +2', command=increase_home_score_by_2)
homeScore2.grid(column=1, row=3)
homeScore3=Button(controlpanel, text='Score +3', command=increase_home_score_by_3)
homeScore3.grid(column=1, row=4)
homeScore4=Button(controlpanel, text='Score -1', command=decrease_home_score)
homeScore4.grid(column=1, row=5)
fouls1Label=Label(controlpanel, text='  0', background='black', foreground='orange')
fouls1Label.grid(column=1, row=6)
homeAddFoulsButton=Button(controlpanel, text='Foul +', command=increase_home_fouls)
homeAddFoulsButton.grid(column=1, row=7)
homeRemoveFoulsButton=Button(controlpanel, text='Foul -', command=remove_home_fouls)
homeRemoveFoulsButton.grid(column=1, row=8)
tol1Label=Label(controlpanel, text='5', background='black', foreground='orange')
tol1Label.grid(column=2, row=6)
homeAddTolButton=Button(controlpanel, text='TOL +', command=add_home_tol)
homeAddTolButton.grid(column=2, row=7)
homeRemoveTolButton=Button(controlpanel, text='TOL -', command=remove_home_tol)
homeRemoveTolButton.grid(column=2, row=8)
homePossButton=Button(controlpanel, text='←Poss', command=change_poss_to_home)
homePossButton.grid(column=2, row=1)
homeBonusButton=Button(controlpanel, text='←Bonus',  command=toggle_home_bonus)
homeBonusButton.grid(column=2, row=2)
guestLabel=Label(controlpanel, text='    0', background='black', foreground='orange')
guestLabel.grid(column=5, row=1)
guestNameEntry=Entry(setcontrolpanel, state=DISABLED)
guestNameEntry.pack()
guestChangeNameButton=Button(setcontrolpanel, text='Set Guest Name', command=set_guest_name)
guestChangeNameButton.pack()
guestScore1=Button(controlpanel, text='Score +1', command=increase_guest_score_by_1)
guestScore1.grid(column=5, row=2)
guestScore2=Button(controlpanel, text='Score +2', command=increase_guest_score_by_2)
guestScore2.grid(column=5, row=3)
guestScore3=Button(controlpanel, text='Score +3', command=increase_guest_score_by_3)
guestScore3.grid(column=5, row=4)
guestScore4=Button(controlpanel, text='Score -1', command=decrease_guest_score)
guestScore4.grid(column=5, row=5)
fouls2Label=Label(controlpanel, text='  0', foreground='orange', background='black')
fouls2Label.grid(column=5, row=6)
guestAddFoulsButton=Button(controlpanel, text='Foul +', command=increase_guest_fouls)
guestAddFoulsButton.grid(column=5, row=7)
guestRemoveFoulsButton=Button(controlpanel, text='Foul -', command=remove_guest_fouls)
guestRemoveFoulsButton.grid(column=5, row=8)
tol2Label=Label(controlpanel, text='5', foreground='orange', background='black')
tol2Label.grid(column=4, row=6)
guestAddTolButton=Button(controlpanel, text='TOL +', command=add_guest_tol)
guestAddTolButton.grid(column=4, row=7)
guestRemoveTolButton=Button(controlpanel, text='TOL -', command=remove_guest_tol)
guestRemoveTolButton.grid(column=4, row=8)
guestPossButton=Button(controlpanel, text='Poss→', command=change_poss_to_guest)
guestPossButton.grid(column=4, row=1)
guestBonusButton=Button(controlpanel, text='Bonus→', command=toggle_guest_bonus)
guestBonusButton.grid(column=4, row=2)
periodControl=Label(controlpanel, text='1', background='black', foreground='orange')
periodControl.grid(column=3, row=7)
periodButton1=Button(controlpanel, text='Previous Period', command=decrease_period)
periodButton1.grid(column=3, row=8)
periodButton2=Button(controlpanel, text='Next Period', command=increase_period)
periodButton2.grid(column=3, row=9)
shotLabel=Label(shotclockcontrolpanel, text='    ', background='black', foreground='orange')
shotLabel.pack()
shotResetButton1=Button(shotclockcontrolpanel, text='Reset 1', command=reset_1, state=DISABLED)
shotResetButton1.pack()
shotResetButton2=Button(shotclockcontrolpanel, text='Reset 2', command=reset_2, state=DISABLED)
shotResetButton2.pack()
runButton=Checkbutton(shotclockcontrolpanel, text='Time In', command=shot_run_stop)
runButton.pack()
autoStopClockButton=Checkbutton(setcontrolpanel, state=DISABLED, text='Stop main clock when shot clock expires', command=auto_stop_clock)
autoStopClockButton.pack()
toggleShotClockButton=Checkbutton(setcontrolpanel, text='Enable Shot Clock', command=toggle_shot_clock)
toggleShotClockButton.pack()
buzzerButton=Button(controlpanel, text='Buzzer')
playerEntry=Entry(controlpanel, state=DISABLED)
playerEntry.grid(column=3, row=10)
foulEntry=Entry(controlpanel, state=DISABLED)
foulEntry.grid(column=3, row=11)
setPlayerFoulButton=Button(controlpanel, text='Set Player Fouls', command=set_player_fouls)
setPlayerFoulButton.grid(column=3, row=12)
buzzerButton.grid(column=3, row=13)
homeTeamLabel=Label(controlpanel, text='HOME', foreground='#00ff00')
homeTeamLabel.grid(column=1, row=9)
homeTeamLabel=Label(controlpanel, text='GUEST', foreground='red')
homeTeamLabel.grid(column=5, row=9)
buzzerButton.bind('<ButtonPress-1>', start_buzzer_loop)
buzzerButton.bind('<ButtonRelease-1>', stop_buzzer_loop)
toggleShotClockButton.state(['!alternate'])
autoStopClockButton.state(['!alternate'])
runButton.config(state=DISABLED)
runButton.state(['!alternate'])
scoreboard.mainloop()
