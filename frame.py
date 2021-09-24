from tkinter import *
from tkinter import ttk, filedialog
from subtitution import Generator
import os

class StartFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Configure Your Flag", font=("Verdana", 14))
        label.pack(pady=10,padx=10)
        self._frame=self
        self.parent=parent
        self.controller=controller
        self.APPEND=lambda: self.append_flag.get()
        self.FLAG_FILE=lambda: self.flag_format.get()
        self.LEN_APPEND=lambda: self.len_appended.get()

        Label(self, text="Format Flag").pack()
        self.flag_format=StringVar()
        flag_format_entry = Entry(self, width=20, textvariable=self.flag_format)
        flag_format_entry.pack()

        Label(self, text="Append Random Char").pack()
        self.append_flag = BooleanVar()
        append_no = Radiobutton(self, text="No", variable=self.append_flag, value=False, command=lambda: self.is_append(self.append_flag.get(), label_append, len_appended_entry))
        append_no.pack()
        append_yes = Radiobutton(self, text="Yes", variable=self.append_flag, value=True, command=lambda: self.is_append(self.append_flag.get(), label_append, len_appended_entry))
        append_yes.pack()
        
        label_append=Label(self, text="Set length random char")
        label_append.config(state='disabled')
        label_append.pack()

        self.len_appended=IntVar()
        len_appended_entry=Entry(self, width=10, textvariable=self.len_appended)
        len_appended_entry.config(state="disabled")
        len_appended_entry.pack()


        Label(self, text="Choose list flag files").pack()
        self.flag_file=StringVar()
        sc_flag_file=Button(self, text="Choose file", command=lambda: self.get_file(flag_loc_label))
        sc_flag_file.pack()
        flag_loc_label=Label(self, text="~")
        flag_loc_label.pack()

        button=Button(self, text="Next", command=lambda: self.controller.show_frame(FrameInput))
        button.pack(pady=5)
    def get_file(self, label):
        file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
        if file:
            filepath = os.path.abspath(file.name)
            label.configure(text=filepath)
            self.flag_file.set(filepath)
            self.FLAG_FILE=filepath
    def is_append(self,append, label, entry):
        if append==True:
            label.config(state='normal')
            label.pack()
            entry.config(state='normal')
            entry.pack()

        else:
            label.config(state='disabled')
            entry.config(state='disabled')

    def show_frame(self, frame, data):
        new_frame=frame(self.parent, data)
        if self._frame:
            self._frame.destroy()
        self._frame=new_frame
        self._frame.pack()



class FrameInput(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller=controller
        self._frame=self
        self.parent=parent
        self.SAVE_AS=""
        label = Label(self, text="Flag Generator", font=("Verdana", 14))
        label.pack(padx=10, pady=10)
        Label(self, text="Choose location to save generated flag").pack(pady=5)
        sc_flag_file=Button(self, text="Choose Location", command=lambda: self.save_file(flag_loc_label))
        sc_flag_file.pack(pady=10)
        flag_loc_label=Label(self, text="~")
        flag_loc_label.pack()

        # check_button=Button(self,background="green",text="Check", command=self.get_data)
        # check_button.pack()
        process=Button(self,background="blue",text="Generate Flag", command=self.generate)
        process.pack()

        self.label_confirm=Label(self, text=" ")
        self.label_confirm.pack()

        back_button = Button(self, text="Back to Home",
                            command=lambda: self.controller.show_frame(StartFrame))
        back_button.pack(pady=10)

        

    def get_data(self):
        data = {
            "FORMAT":self.controller.get_page(StartFrame).flag_format.get(),
            "FLAG_FILE":self.controller.get_page(StartFrame).FLAG_FILE,
            "APPEND":self.controller.get_page(StartFrame).append_flag.get(),
            "LEN_APPEND":self.controller.get_page(StartFrame).len_appended.get()
        }
        print(data)
    def save_file(self, label):
        file = filedialog.asksaveasfilename(initialfile='flag.txt', defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
        if file:
            filepath = os.path.abspath(file)
            self.SAVE_AS=filepath
            label.configure(text=filepath)
            print(filepath)
    def check(self, data):
        print(data)
    def generate(self):
        data = {
            "FORMAT":self.controller.get_page(StartFrame).flag_format.get(),
            "FLAG_FILE":self.controller.get_page(StartFrame).FLAG_FILE,
            "APPEND":self.controller.get_page(StartFrame).append_flag.get(),
            "LEN_APPEND":self.controller.get_page(StartFrame).len_appended.get()
        }
        gen=Generator(fmt=data["FORMAT"], append=data["APPEND"])
        flags=gen.flags_generate(filepath=data["FLAG_FILE"], len_append=data['LEN_APPEND'])

        file=open(self.SAVE_AS,'w')
        file.write("\n".join(flags))
        self.label_confirm.config(text="Flags succesfully generated")
        self.label_confirm.pack()

    def show_frame(self, frame):
        new_frame=frame(self.parent)
        if self._frame:
            self._frame.destroy()
        self._frame=new_frame
        self._frame.pack()