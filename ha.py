#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jul 30, 2018 11:51:34 PM
#Created by Bharath Kumar V

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import ha_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Home_Automation (root)
    ha_support.init(root, top)
    ha_support.tick()
    ha_support.loadDateDay()
    ha_support.loadTemperature()
    ha_support.loadPeopleCount(0)
    ha_support.loadSafetyStatus()
    ha_support.initSerialCommunication()
    root.mainloop()

w = None
def create_Home_Automation(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Home_Automation (w)
    ha_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Home_Automation():
    global w
    w.destroy()
    w = None


class Home_Automation:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#282830'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 20 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("800x480+309+125")
        top.title("Home Automation")
        top.configure(background="#282830")
        top.configure(highlightbackground="#282830")
        top.configure(highlightcolor="black")

        self.TimeLabel = Label(top)
        self.TimeLabel.place(relx=0.48, rely=0.05, height=38, width=195, anchor=CENTER)
        self.TimeLabel.configure(background="#282830")
        self.TimeLabel.configure(font=font10)
        self.TimeLabel.configure(foreground="#FFFFFF")

        self.DateDayLabel = Label(top)
        self.DateDayLabel.place(relx=0.48, rely=0.12, height=25, width=200, anchor=CENTER)
        self.DateDayLabel.configure(background="#282830")
        self.DateDayLabel.configure(font=font9)
        self.DateDayLabel.configure(foreground="#FFFFFF")
        
        self.InTempLabel = Label(top)
        self.InTempLabel.place(relx=1.02, rely=0.015, height=38, width=195, anchor=NE)
        self.InTempLabel.configure(background="#282830")
        self.InTempLabel.configure(font=font9)
        self.InTempLabel.configure(justify = LEFT)
        self.InTempLabel.configure(text='''Inside: 20.0^C''')
        self.InTempLabel.configure(foreground="#FFFFFF")

        self.OutTempLabel = Label(top)
        self.OutTempLabel.place(relx=1.02, rely=0.095, height=25, width=200, anchor=NE)
        self.OutTempLabel.configure(background="#282830")
        self.OutTempLabel.configure(font=font9)
        self.OutTempLabel.configure(justify = LEFT)
        self.OutTempLabel.configure(text='''Outside:20.0^C''')
        self.OutTempLabel.configure(foreground="#FFFFFF")

        self.R1Frame = Frame(top)
        self.R1Frame.place(relx=0.01, rely=0.2, relheight=0.5, relwidth=0.32)
        self.R1Frame.configure(relief=GROOVE)
        self.R1Frame.configure(borderwidth="2")
        self.R1Frame.configure(relief=GROOVE)
        self.R1Frame.configure(background="#249991")
        self.R1Frame.configure(highlightbackground="#249991")
        self.R1Frame.configure(highlightcolor="black")
        self.R1Frame.configure(width=125)

        self._led = PhotoImage(file="light_off.png")
        self.R1L01 = Button(self.R1Frame)
        self.R1L01.configure(image=self._led)
        self.R1L01.place(relx=0.02, rely=0.015, height=40, width=40, anchor=NW)
        self.R1L01.configure(borderwidth="0")
        self.R1L01.configure(background="#249991")
        self.R1L01.configure(overrelief="flat")
        self.R1L01.configure(pady="0")
        self.R1L01.configure(text='''OFF''')
        self.R1L01.bind('<Button-1>',lambda e:ha_support.room1Led1Control(self.R1L01['text']))

        self.R1L02 = Button(self.R1Frame)
        self.R1L02.configure(image=self._led)
        self.R1L02.place(relx=0.02, rely=0.99, height=40, width=40, anchor=SW)
        self.R1L02.configure(borderwidth="0")
        self.R1L02.configure(background="#249991")
        self.R1L02.configure(overrelief="flat")
        self.R1L02.configure(pady="0")
        self.R1L02.configure(text='''OFF''')
        self.R1L02.bind('<Button-1>',lambda e:ha_support.room1Led2Control(self.R1L02['text']))

        self.R1L03 = Button(self.R1Frame)
        self.R1L03.configure(image=self._led)
        self.R1L03.place(relx=0.98, rely=0.015, height=40, width=40, anchor=NE)
        self.R1L03.configure(borderwidth="0")
        self.R1L03.configure(background="#249991")
        self.R1L03.configure(overrelief="flat")
        self.R1L03.configure(pady="0")
        self.R1L03.configure(text='''OFF''')
        self.R1L03.bind('<Button-1>',lambda e:ha_support.room1Led3Control(self.R1L03['text']))

        self.R1L4 = Button(self.R1Frame)
        self.R1L4.configure(image=self._led)
        self.R1L4.place(relx=0.98, rely=0.99, height=40, width=40, anchor=SE)
        self.R1L4.configure(borderwidth="0")
        self.R1L4.configure(background="#249991")
        self.R1L4.configure(overrelief="flat")
        self.R1L4.configure(pady="0")
        self.R1L4.configure(text='''OFF''')
        self.R1L4.bind('<Button-1>',lambda e:ha_support.room1Led4Control(self.R1L4['text']))
        
        self._fan = PhotoImage(file="sfan.png")
        self.R1F01 = Button(self.R1Frame)
        self.R1F01.place(relx=0.35, rely=0.50, height=50, width=50, anchor = CENTER)
        self.R1F01.configure(borderwidth="0")
        self.R1F01.configure(image=self._fan)
        self.R1F01.configure(background="#249991")
        self.R1F01.configure(pady="0")
        self.R1F01.configure(text='''OFF''')
        self.R1F01.bind('<Button-1>',lambda e:ha_support.room1Fan1Control(self.R1F01['text']))

        self.R1F01S = Label(self.R1Frame)
        self.R1F01S.place(relx=0.20, rely=0.50, height=20, width=20, anchor=CENTER)
        self.R1F01S.configure(background="#249991")
        self.R1F01S.configure(font=font9)
        self.R1F01S.configure(justify = LEFT)
        self.R1F01S.configure(text=ha_support.loadFanState(self.R1F01S, 2))
        self.R1F01S.configure(foreground="#FFFFFF")

        self._fanUP = PhotoImage(file="fup.png")
        self.R1F01CU = Button(self.R1Frame)
        self.R1F01CU.place(relx=0.35, rely=0.33, height=20, width=40, anchor = CENTER)
        self.R1F01CU.configure(borderwidth="0")
        self.R1F01CU.configure(image=self._fanUP)
        self.R1F01CU.configure(background="#249991")
        self.R1F01CU.configure(pady="0")
        self.R1F01CU.configure(text='''U''')
        self.R1F01CU.bind('<Button-1>',lambda e:ha_support.room1Fan1SControl(self.R1F01CU['text']))
        
        self._fanDOWN = PhotoImage(file="fdown.png")
        self.R1F01CD = Button(self.R1Frame)
        self.R1F01CD.place(relx=0.35, rely=0.66, height=20, width=40, anchor = CENTER)
        self.R1F01CD.configure(borderwidth="0")
        self.R1F01CD.configure(image=self._fanDOWN)
        self.R1F01CD.configure(background="#249991")
        self.R1F01CD.configure(pady="0")
        self.R1F01CD.configure(text='''D''')
        self.R1F01CD.bind('<Button-1>',lambda e:ha_support.room1Fan1SControl(self.R1F01CD['text']))
        
        self.R1F02 = Button(self.R1Frame)
        self.R1F02.place(relx=0.60, rely=0.50, height=50, width=50, anchor = CENTER)
        self.R1F02.configure(borderwidth="0")
        self.R1F02.configure(image=self._fan)
        self.R1F02.configure(background="#249991")
        self.R1F02.configure(pady="0")
        self.R1F02.configure(text='''OFF''')
        self.R1F02.bind('<Button-1>',lambda e:ha_support.room1Fan2Control(self.R1F02['text']))

        self.R1F02CU = Button(self.R1Frame)
        self.R1F02CU.place(relx=0.60, rely=0.33, height=20, width=40, anchor = CENTER)
        self.R1F02CU.configure(borderwidth="0")
        self.R1F02CU.configure(image=self._fanUP)
        self.R1F02CU.configure(background="#249991")
        self.R1F02CU.configure(pady="0")
        self.R1F02CU.configure(text='''U''')
        self.R1F02CU.bind('<Button-1>',lambda e:ha_support.room1Fan2SControl(self.R1F02CU['text']))

        self.R1F02CD = Button(self.R1Frame)
        self.R1F02CD.place(relx=0.60, rely=0.66, height=20, width=40, anchor = CENTER)
        self.R1F02CD.configure(borderwidth="0")
        self.R1F02CD.configure(image=self._fanDOWN)
        self.R1F02CD.configure(background="#249991")
        self.R1F02CD.configure(pady="0")
        self.R1F02CD.configure(text='''D''')
        self.R1F02CD.bind('<Button-1>',lambda e:ha_support.room1Fan2SControl(self.R1F02CD['text']))

        self.R1F02S = Label(self.R1Frame)
        self.R1F02S.place(relx=0.75, rely=0.50, height=20, width=20, anchor=CENTER)
        self.R1F02S.configure(background="#249991")
        self.R1F02S.configure(font=font9)
        self.R1F02S.configure(justify = LEFT)
        self.R1F02S.configure(text=ha_support.loadFanState(self.R1F02S, 2))
        self.R1F02S.configure(foreground="#FFFFFF")

        self.R2Frame = Frame(top)
        self.R2Frame.place(relx=0.34, rely=0.2, relheight=0.5, relwidth=0.32)
        self.R2Frame.configure(relief=GROOVE)
        self.R2Frame.configure(borderwidth="2")
        self.R2Frame.configure(relief=GROOVE)
        self.R2Frame.configure(background="#249991")
        self.R2Frame.configure(highlightbackground="#249991")
        self.R2Frame.configure(highlightcolor="black")
        self.R2Frame.configure(width=125)

        self.R2L01 = Button(self.R2Frame)
        self.R2L01.configure(image=self._led)
        self.R2L01.place(relx=0.02, rely=0.015, height=40, width=40, anchor=NW)
        self.R2L01.configure(borderwidth="0")
        self.R2L01.configure(background="#249991")
        self.R2L01.configure(overrelief="flat")
        self.R2L01.configure(pady="0")
        self.R2L01.configure(text='''OFF''')
        self.R2L01.bind('<Button-1>',lambda e:ha_support.room2Led1Control(self.R2L01['text']))

        self.R2L02 = Button(self.R2Frame)
        self.R2L02.configure(image=self._led)
        self.R2L02.place(relx=0.02, rely=0.99, height=40, width=40, anchor=SW)
        self.R2L02.configure(borderwidth="0")
        self.R2L02.configure(background="#249991")
        self.R2L02.configure(overrelief="flat")
        self.R2L02.configure(pady="0")
        self.R2L02.configure(text='''OFF''')
        self.R2L02.bind('<Button-1>',lambda e:ha_support.room2Led2Control(self.R2L02['text']))

        self.R2L03 = Button(self.R2Frame)
        self.R2L03.configure(image=self._led)
        self.R2L03.place(relx=0.98, rely=0.015, height=40, width=40, anchor=NE)
        self.R2L03.configure(borderwidth="0")
        self.R2L03.configure(background="#249991")
        self.R2L03.configure(overrelief="flat")
        self.R2L03.configure(pady="0")
        self.R2L03.configure(text='''OFF''')
        self.R2L03.bind('<Button-1>',lambda e:ha_support.room2Led3Control(self.R2L03['text']))

        self.R2L04 = Button(self.R2Frame)
        self.R2L04.configure(image=self._led)
        self.R2L04.place(relx=0.98, rely=0.99, height=40, width=40, anchor=SE)
        self.R2L04.configure(borderwidth="0")
        self.R2L04.configure(background="#249991")
        self.R2L04.configure(overrelief="flat")
        self.R2L04.configure(pady="0")
        self.R2L04.configure(text='''OFF''')
        self.R2L04.bind('<Button-1>',lambda e:ha_support.room2Led4Control(self.R2L04['text']))
        
        self.R2F01S = Label(self.R2Frame)
        self.R2F01S.place(relx=0.20, rely=0.50, height=20, width=20, anchor=CENTER)
        self.R2F01S.configure(background="#249991")
        self.R2F01S.configure(font=font9)
        self.R2F01S.configure(justify = LEFT)
        self.R2F01S.configure(text=ha_support.loadFanState(self.R2F01S, 2))
        self.R2F01S.configure(foreground="#FFFFFF")
        
        self.R2F01 = Button(self.R2Frame)
        self.R2F01.place(relx=0.35, rely=0.5, height=50, width=50, anchor = CENTER)
        self.R2F01.configure(borderwidth="0")
        self.R2F01.configure(image=self._fan)
        self.R2F01.configure(background="#249991")
        self.R2F01.configure(pady="0")
        self.R2F01.configure(text='''OFF''')
        self.R2F01.bind('<Button-1>',lambda e:ha_support.room2Fan1Control(self.R2F01['text']))
        
        self.R2F01CU = Button(self.R2Frame)
        self.R2F01CU.place(relx=0.35, rely=0.33, height=20, width=40, anchor = CENTER)
        self.R2F01CU.configure(borderwidth="0")
        self.R2F01CU.configure(image=self._fanUP)
        self.R2F01CU.configure(background="#249991")
        self.R2F01CU.configure(pady="0")
        self.R2F01CU.configure(text='''U''')
        self.R2F01CU.bind('<Button-1>',lambda e:ha_support.room2Fan1SControl(self.R2F01CU['text']))

        self.R2F01CD = Button(self.R2Frame)
        self.R2F01CD.place(relx=0.35, rely=0.66, height=20, width=40, anchor = CENTER)
        self.R2F01CD.configure(borderwidth="0")
        self.R2F01CD.configure(image=self._fanDOWN)
        self.R2F01CD.configure(background="#249991")
        self.R2F01CD.configure(pady="0")
        self.R2F01CD.configure(text='''D''')
        self.R2F01CD.bind('<Button-1>',lambda e:ha_support.room2Fan1SControl(self.R2F01CD['text']))
        
        self.R2F02 = Button(self.R2Frame)
        self.R2F02.place(relx=0.60, rely=0.5, height=50, width=50, anchor = CENTER)
        self.R2F02.configure(borderwidth="0")
        self.R2F02.configure(image=self._fan)
        self.R2F02.configure(background="#249991")
        self.R2F02.configure(pady="0")
        self.R2F02.configure(text='''OFF''')
        self.R2F02.bind('<Button-1>',lambda e:ha_support.room2Fan2Control(self.R2F02['text']))

        self.R2F02CU = Button(self.R2Frame)
        self.R2F02CU.place(relx=0.6, rely=0.33, height=20, width=40, anchor = CENTER)
        self.R2F02CU.configure(borderwidth="0")
        self.R2F02CU.configure(image=self._fanUP)
        self.R2F02CU.configure(background="#249991")
        self.R2F02CU.configure(pady="0")
        self.R2F02CU.configure(text='''U''')
        self.R2F02CU.bind('<Button-1>',lambda e:ha_support.room2Fan2SControl(self.R2F02CU['text']))

        self.R2F02CD = Button(self.R2Frame)
        self.R2F02CD.place(relx=0.6, rely=0.66, height=20, width=40, anchor = CENTER)
        self.R2F02CD.configure(borderwidth="0")
        self.R2F02CD.configure(image=self._fanDOWN)
        self.R2F02CD.configure(background="#249991")
        self.R2F02CD.configure(pady="0")
        self.R2F02CD.configure(text='''D''')
        self.R2F02CD.bind('<Button-1>',lambda e:ha_support.room2Fan2SControl(self.R2F02CD['text']))

        self.R2F02S = Label(self.R2Frame)
        self.R2F02S.place(relx=0.75, rely=0.50, height=20, width=20, anchor=CENTER)
        self.R2F02S.configure(background="#249991")
        self.R2F02S.configure(font=font9)
        self.R2F02S.configure(justify = LEFT)
        self.R2F02S.configure(text=ha_support.loadFanState(self.R2F02S, 2))
        self.R2F02S.configure(foreground="#FFFFFF")

        self.R3Frame = Frame(top)
        self.R3Frame.place(relx=0.67, rely=0.2, relheight=0.5, relwidth=0.32)
        self.R3Frame.configure(relief=GROOVE)
        self.R3Frame.configure(borderwidth="2")
        self.R3Frame.configure(relief=GROOVE)
        self.R3Frame.configure(background="#249991")
        self.R3Frame.configure(highlightbackground="#249991")
        self.R3Frame.configure(highlightcolor="black")
        self.R3Frame.configure(width=125)

        self.R3L01 = Button(self.R3Frame)
        self.R3L01.place(relx=0.02, rely=0.015, height=40, width=40, anchor=NW)
        self.R3L01.configure(borderwidth="0")
        self.R3L01.configure(image=self._led)
        self.R3L01.configure(background="#249991")
        self.R3L01.configure(pady="0")
        self.R3L01.configure(text='''OFF''')
        self.R3L01.bind('<Button-1>',lambda e:ha_support.room3Led1Control(self.R3L01['text']))
        
        self.R3L02 = Button(self.R3Frame)
        self.R3L02.place(relx=0.02, rely=0.99, height=40, width=40, anchor=SW)
        self.R3L02.configure(borderwidth="0")
        self.R3L02.configure(image=self._led)
        self.R3L02.configure(background="#249991")
        self.R3L02.configure(pady="0")
        self.R3L02.configure(text='''OFF''')
        self.R3L02.bind('<Button-1>',lambda e:ha_support.room3Led2Control(self.R3L02['text']))

        self.R3L03 = Button(self.R3Frame)
        self.R3L03.place(relx=0.98, rely=0.015, height=40, width=40, anchor=NE)
        self.R3L03.configure(borderwidth="0")
        self.R3L03.configure(image=self._led)
        self.R3L03.configure(background="#249991")
        self.R3L03.configure(pady="0")
        self.R3L03.configure(text='''OFF''')
        self.R3L03.bind('<Button-1>',lambda e:ha_support.room3Led3Control(self.R3L03['text']))

        self.R3L04 = Button(self.R3Frame)
        self.R3L04.place(relx=0.98, rely=0.99, height=40, width=40, anchor=SE)
        self.R3L04.configure(borderwidth="0")
        self.R3L04.configure(image=self._led)
        self.R3L04.configure(background="#249991")
        self.R3L04.configure(pady="0")
        self.R3L04.configure(text='''OFF''')
        self.R3L04.bind('<Button-1>',lambda e:ha_support.room3Led4Control(self.R3L04['text']))

        self.R3F01S = Label(self.R3Frame)
        self.R3F01S.place(relx=0.20, rely=0.50, height=20, width=20, anchor=CENTER)
        self.R3F01S.configure(background="#249991")
        self.R3F01S.configure(font=font9)
        self.R3F01S.configure(justify = LEFT)
        self.R3F01S.configure(text=ha_support.loadFanState(self.R3F01S, 2))
        self.R3F01S.configure(foreground="#FFFFFF")

        self.R3F01 = Button(self.R3Frame)
        self.R3F01.place(relx=0.35, rely=0.50, height=50, width=50, anchor = CENTER)
        self.R3F01.configure(borderwidth="0")
        self.R3F01.configure(image=self._fan)
        self.R3F01.configure(background="#249991")
        self.R3F01.configure(pady="0")
        self.R3F01.configure(text='''OFF''')
        self.R3F01.bind('<Button-1>',lambda e:ha_support.room3Fan1Control(self.R3F01['text']))

        self.R3F01CU = Button(self.R3Frame)
        self.R3F01CU.place(relx=0.35, rely=0.33, height=20, width=40, anchor = CENTER)
        self.R3F01CU.configure(borderwidth="0")
        self.R3F01CU.configure(image=self._fanUP)
        self.R3F01CU.configure(background="#249991")
        self.R3F01CU.configure(pady="0")
        self.R3F01CU.configure(text='''U''')
        self.R3F01CU.bind('<Button-1>',lambda e:ha_support.room3Fan1SControl(self.R3F01CU['text']))

        self.R3F01CD = Button(self.R3Frame)
        self.R3F01CD.place(relx=0.35, rely=0.66, height=20, width=40, anchor = CENTER)
        self.R3F01CD.configure(borderwidth="0")
        self.R3F01CD.configure(image=self._fanDOWN)
        self.R3F01CD.configure(background="#249991")
        self.R3F01CD.configure(pady="0")
        self.R3F01CD.configure(text='''D''')
        self.R3F01CD.bind('<Button-1>',lambda e:ha_support.room3Fan1SControl(self.R3F01CD['text']))
        
        self.R3F02 = Button(self.R3Frame)
        self.R3F02.place(relx=0.60, rely=0.50, height=50, width=50, anchor = CENTER)
        self.R3F02.configure(borderwidth="0")
        self.R3F02.configure(image=self._fan)
        self.R3F02.configure(background="#249991")
        self.R3F02.configure(pady="0")
        self.R3F02.configure(text='''OFF''')
        self.R3F02.bind('<Button-1>',lambda e:ha_support.room3Fan2Control(self.R3F02['text']))

        self.R3F02CU = Button(self.R3Frame)
        self.R3F02CU.place(relx=0.60, rely=0.33, height=20, width=40, anchor = CENTER)
        self.R3F02CU.configure(borderwidth="0")
        self.R3F02CU.configure(image=self._fanUP)
        self.R3F02CU.configure(background="#249991")
        self.R3F02CU.configure(pady="0")
        self.R3F02CU.configure(text='''U''')
        self.R3F02CU.bind('<Button-1>',lambda e:ha_support.room3Fan2SControl(self.R3F02CU['text']))

        self.R3F02CD = Button(self.R3Frame)
        self.R3F02CD.place(relx=0.6, rely=0.66, height=20, width=40, anchor = CENTER)
        self.R3F02CD.configure(borderwidth="0")
        self.R3F02CD.configure(image=self._fanDOWN)
        self.R3F02CD.configure(background="#249991")
        self.R3F02CD.configure(pady="0")
        self.R3F02CD.configure(text='''D''')
        self.R3F02CD.bind('<Button-1>',lambda e:ha_support.room3Fan2SControl(self.R3F02CD['text']))
        
        self.R3F02S = Label(self.R3Frame)
        self.R3F02S.place(relx=0.75, rely=0.50, height=20, width=20, anchor=CENTER)
        self.R3F02S.configure(background="#249991")
        self.R3F02S.configure(font=font9)
        self.R3F02S.configure(justify = LEFT)
        self.R3F02S.configure(text=ha_support.loadFanState(self.R3F02S, 2))
        self.R3F02S.configure(foreground="#FFFFFF")
        
        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.67, rely=0.74, relheight=0.15, relwidth=0.32)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#249991")
        self.Frame2.configure(width=245)

        self.OutL01 = Button(self.Frame2)
        self.OutL01.place(relx=0.06, rely=0.23, height=40, width=40)
        self.OutL01.configure(borderwidth="0")
        self.OutL01.configure(image=self._led)
        self.OutL01.configure(background="#249991")
        self.OutL01.configure(pady="0")
        self.OutL01.configure(text='''OFF''')
        self.OutL01.bind('<Button-1>',lambda e:ha_support.outLed1Control(self.OutL01['text']))

        self.OutL02 = Button(self.Frame2)
        self.OutL02.place(relx=0.3, rely=0.23, height=40, width=40)
        self.OutL02.configure(borderwidth="0")
        self.OutL02.configure(image=self._led)
        self.OutL02.configure(background="#249991")
        self.OutL02.configure(pady="0")
        self.OutL02.configure(text='''OFF''')
        self.OutL02.bind('<Button-1>',lambda e:ha_support.outLed2Control(self.OutL02['text']))

        self.OutL03 = Button(self.Frame2)
        self.OutL03.place(relx=0.54, rely=0.23, height=40, width=40)
        self.OutL03.configure(borderwidth="0")
        self.OutL03.configure(image=self._led)
        self.OutL03.configure(background="#249991")
        self.OutL03.configure(pady="0")
        self.OutL03.configure(text='''OFF''')
        self.OutL03.bind('<Button-1>',lambda e:ha_support.outLed3Control(self.OutL03['text']))

        self.OutL04 = Button(self.Frame2)
        self.OutL04.place(relx=0.78, rely=0.23, height=40, width=40)
        self.OutL04.configure(borderwidth="0")
        self.OutL04.configure(image=self._led)
        self.OutL04.configure(background="#249991")
        self.OutL04.configure(pady="0")
        self.OutL04.configure(text='''OFF''')
        self.OutL04.bind('<Button-1>',lambda e:ha_support.outLed4Control(self.OutL04['text']))

        self.GSFrame = Frame(top)
        self.GSFrame.place(relx=0.01, rely=0.74, relheight=0.15, relwidth=0.19)
        self.GSFrame.configure(relief=GROOVE)
        self.GSFrame.configure(borderwidth="2")
        self.GSFrame.configure(relief=GROOVE)
        self.GSFrame.configure(background="#249991")
        self.GSFrame.configure(width=125)

        self.GSLabel = Label(self.GSFrame)
        self.GSLabel.place(relx=0.5, rely=0.45, height=31, width=79, anchor=CENTER)
        self.GSLabel.configure(background="#27ae60")
        self.GSLabel.configure(font=font15)

        self.PCFrame = Frame(top)
        self.PCFrame.place(relx=0.2, rely=0.74, relheight=0.15, relwidth=0.40)
        self.PCFrame.configure(relief=GROOVE)
        self.PCFrame.configure(borderwidth="2")
        self.PCFrame.configure(relief=GROOVE)
        self.PCFrame.configure(background="#249991")
        self.PCFrame.configure(highlightbackground="#249991")
        self.PCFrame.configure(highlightcolor="black")
        self.PCFrame.configure(width=210)

        self.PeopleCountLabel = Label(self.PCFrame)
        self.PeopleCountLabel.place(relx=0.30, rely=0.45, height=31, width=180, anchor=CENTER)
        self.PeopleCountLabel.configure(background="#249991")
        self.PeopleCountLabel.configure(font=font15)
        self.PeopleCountLabel.configure(foreground="#FFFFFF")
        self.PeopleCountLabel.configure(justify=LEFT)
        
        self.PeopleCountU = Button(self.PCFrame)
        self.PeopleCountU.place(relx=0.98, rely=0.10, height=20, width=30, anchor=NE)
        self.PeopleCountU.configure(borderwidth="0")
        self.PeopleCountU.configure(image=self._fanUP)
        self.PeopleCountU.configure(background="#249991")
        self.PeopleCountU.configure(pady="0")
        self.PeopleCountU.configure(text='''U''')
        self.PeopleCountU.bind('<Button-1>',lambda e:ha_support.PeopleCountControl(self.PeopleCountU['text']))

        self.PeopleCountD = Button(self.PCFrame)
        self.PeopleCountD.place(relx=0.98, rely=0.80, height=20, width=30, anchor=SE)
        self.PeopleCountD.configure(borderwidth="0")
        self.PeopleCountD.configure(image=self._fanDOWN)
        self.PeopleCountD.configure(background="#249991")
        self.PeopleCountD.configure(pady="0")
        self.PeopleCountD.configure(text='''D''')
        self.PeopleCountD.bind('<Button-1>',lambda e:ha_support.PeopleCountControl(self.PeopleCountD['text']))
        

if __name__ == '__main__':
    vp_start_gui()
