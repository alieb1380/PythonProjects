import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
try:
    from alarm_sound import AlarmSound
    from sql_connector import sqlConnector
except ImportError:
    from.alarm_sound import AlarmSound
    from.sql_connector import SqlConnector
    
class alarm(tk.frame):
    def __init__(self, parent, id, time, repeat, sound, message, active):
        self.db = SqlConnector()
        self.id = id
        self.time = time
        self.repeat = repeat
        # Path to sound that will play when alarm goes off
        self.sound = sound
        # Boolean value whether alarm will go off at time
        self.active = active
        # Message that shows when alarm goes off
        self.message = message    
        self.parent = parent
        self.alarm_sound = None
        tk.Frame.__init__(self, parent)
        self.add_widgets()
        self.configure(borderwidth=1, relief=tk.RAISED, background="black")

def add_widgets(self):
    days = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
    self.active_var = tk.StringVar()
    self.active_var.set(1 if self.active == "True" else 0)
    self.repeat_var = tk.StringVar(value=days)
    self.meassage_var = tk.StringVar(value=self.message)
    
    self.label_frame = tk.Frame(self)