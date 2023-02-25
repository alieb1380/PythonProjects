# import datetime
# import random
# import sys
# from matplotlib import animation
# import matplotlib.pyplot as plt
# import seaborn as sns

# def update(frame_number, rolls, faces, frequencies):
    
#     random.seed(datetime.datetime.now())
#     for i in range(rolls):
#         frequencies[random.randrange(1, 7) - 1] += 1
    
#     plt.cla()
    
#     axes = sns.barplot(faces, frequencies, palette="bright")
#     axes.set_title(f"Dice frequencies for {sum(frequencies):,} rolls")
#     axes.set(xlabel="Dice Value", ylabel="Frequency")
#     axes.set_ylim(top=max(frequencies) * 1.15)
    
#     for bar, frequency in zip(axes.patches, frequencies):
#         text_x = bar.get_x() + bar.get_width() / 2.0
#         text_y = bar.get_height()
#         text = f"{frequency:,}\n{frequency / sum(frequencies):.3%}"
#         axes.text(text_x, text_y, text, ha="center", va="bottom")

# number_of_frames = 1000 # for command line args use int(sys.argv[1]) instead  
# rolls_per_frame = 1 # for command line args use int(sys.argv[2]) instead

# sns.set_style("darkgrid")
# figure = plt.figure("Rolling a 6-sided dice")
# values = list(range(1, 7))
# frequencies = [0] * 6

# die_animation = animation.FuncAnimation(
#     figure, update, repeat=False, frames=number_of_frames,
#     interval=33, fargs=(rolls_per_frame, values, frequencies))

# plt.show()

import math
import random
import secrets
import itertools
import threading
import functools

from types import SimpleNamespace

from tkinter import *
from tkinter.scrolledtext import ScrolledText


def gen_rainbow(domain=None):
    if domain is None:
        domain = itertools.cycle(x/50 for x in range(50))  # interval = 0.2
    for _ in range(secrets.randbelow(50)):
        next(domain)  # advance ? cycles for a random start color
    while True:
        x = next(domain)
        RGB = [
            math.sin(x * 2 * math.pi) / 2 + 0.5,
            math.sin(x * 2 * math.pi + 2 * math.pi/3) / 2 + 0.5,
            math.sin(x * 2 * math.pi + 4 * math.pi / 3) / 2 + 0.5,
        ]
        yield '#' + bytes(int(y*255) for y in RGB).hex()
    

class Die(SimpleNamespace):
    @classmethod
    def roll(cls, nsides=6, **kwargs):
        
        result = secrets.randbelow(nsides)+1
        return cls(value=result, range=range(1, nsides+1), **kwargs)

    def __str__(self):
        return str(self.value) + ('!' if self.value == self.max else '')
    
    @property
    def min(self):
        return self.range[0]
    
    @property
    def max(self):
        return self.range[-1]


class ReadOnlyText(ScrolledText):
    
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(state=DISABLED)
        self.insert = self._unlock(super().insert)
        self.delete = self._unlock(super().delete)
    
    def _unlock(self, f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            nonlocal self
            self.config(state=NORMAL)
            ret = f(*args, **kwargs)
            self.config(state=DISABLED)
            return ret
        return wrapped


class BlackFrame(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(bg='black')


class RollingDie(Frame):    
    die_font = 'courier 40 bold'
    longest_delay = 200 #ms
    
    def __init__(self, master=None, **kwargs):
        self.die = kwargs.pop('die')
        super().__init__(master, **kwargs)
        
        # to change the die's border color we change the color of self
        self.config(height=30, width=30, background='white')
        self.total_bounces = random.randint(20,30)
        self.bounce_count = 0
        
        # this is the number's black background
        self.inner_frame = BlackFrame(self)
        self.inner_frame.pack(padx=1, pady=1, fill=BOTH, expand=YES)
        
        self.die_label = Label(
            self.inner_frame, text='', foreground='white', 
            background='black', font=self.die_font,
        )
        self.die_label.pack(anchor=CENTER)
        
        self.advance_state()
        
    def advance_state(self):
        if self.bounce_count < self.total_bounces:

            self.die_label.configure(text=random.randint(self.die.min, self.die.max))

            self.bounce_count += random.randint(1,3)
            delay = int(self.bounce_count / self.total_bounces * self.longest_delay)
            self.after(delay, self.advance_state)
        else:
            self.configure(background=self.die.color)
            self.die_label.config(
                text=str(self.die.value), foreground=self.die.color
            )


class DiceRoller(ReadOnlyText):
    """Scrolled textbox filled with animated labels"""
    def __init__(self, master=None, **kwargs):
        self.nsides = kwargs.pop('sidevar', None)  # IntVar
        super().__init__(master, **kwargs)
        
        self.hide_vbar()
        
        self.configure(bg='black', borderwidth=0)

        # when there is no sidevar, make a default var
        if self.nsides is None:
            self.nsides = IntVar(self)
            self.nsides.set(6)
            
        self.color = gen_rainbow()
        self.bind('<Return>', self.roll)
        self.bind('<space>', self.roll)
        self.focus_set()


    def roll(self, _event=None):
        die = Die.roll(nsides=self.nsides.get(), color=next(self.color))
        
        self.window_create(INSERT, window=RollingDie(die=die), padx=5, pady=5)
        self.see(INSERT)
        
        
        
    def hide_vbar(self):
        self.vbar.pack_forget()
    
    def show_vbar(self):
        self.vbar.pack(side=LEFT, fill=BOTH, expand=True)
        

class ScrollableSpinbox(Spinbox):
    """https://stackoverflow.com/questions/38329996/enable-mouse-wheel-in-spinbox-tk-python
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind('<MouseWheel>', self.mouseWheel)
        self.bind('<Button-4>', self.mouseWheel)
        self.bind('<Button-5>', self.mouseWheel)

    def mouseWheel(self, event):
        if event.num == 5 or event.delta == -120:
            self.invoke('buttondown')
        elif event.num == 4 or event.delta == 120:
            self.invoke('buttonup')


class App(BlackFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.sidevar = IntVar(self)
        self.sidevar.set(6)
        
        # create spinbox for controlling die sides
        BlackFrame(self).pack(fill=X)  # Horizontal spacer
        f = BlackFrame(self)
        f.pack(pady=10)
        Label(
            f, text='Sides:', foreground='white', background='black'
        ).pack(padx=5, side=LEFT, anchor=CENTER)
        s = ScrollableSpinbox(
            f, textvariable=self.sidevar, from_=1, to=99999999,
            background='black', foreground='white',
        )
        s.pack(side=LEFT)
        BlackFrame(self).pack(fill=X)  # Horizontal spacer
        
        # dice screen
        f = Frame(self, background='white')
        f.pack(expand=YES, fill=BOTH, padx=10, pady=10)
        DiceRoller(f, borderwidth=0, sidevar=self.sidevar)\
        .pack(expand=YES, fill=BOTH, padx=1, pady=1)


class Root(Tk):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.title('2D Dice')
        App(self).pack(expand=YES, fill=BOTH)
        

def main():
    Root().mainloop()


if __name__ == '__main__':
    main()