from tkinter import *
from tkinter import ttk
from subtitution import Generator
from frame import FrameInput, StartFrame

class Main(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('CTF Flag Generator')
        self.minsize(width=300, height=150)
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self._frame=None
        self.frames = {}

        for F in [StartFrame, FrameInput]:
            frame = F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartFrame)   

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()
    def get_page(self, frame):
        return self.frames[frame]

if __name__=="__main__":
    app=Main()
    app.mainloop()