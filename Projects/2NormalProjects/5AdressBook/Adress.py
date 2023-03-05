import pickle
from tkinter import *
import os.path
import tkinter.messagebox
from tkinter import ttk

class address:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class AddressBook:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.initialization()
        self.bind()
        self.set_listbox()
        