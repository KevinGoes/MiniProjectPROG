import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import datetime

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Registreren, Stallen, Ophalen, Informatie):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welkom bij de NS!", background='yellow', foreground='blue', width=50, height=3, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        optie1 = tk.Button(text='Registreren', height=15, width=65, font=('Helvetica', 15, 'bold'),
                          background='royalblue',
                          foreground='white', command=lambda: controller.show_frame("Registreren"))
        optie1.place(x=0, y=75)

        optie2 = tk.Button(text='Stallen', height=15, width=65, font=('Helvetica', 15, 'bold'),
                           background='royalblue',
                           foreground='white', highlightbackground="Black",
                           command=lambda: controller.show_frame("Stallen"))
        optie2.place(x=775, y=75)

        optie3 = tk.Button(text='Ophalen', height=15, width=65, font=('Helvetica', 15, 'bold'),
                           background='royalblue',
                           foreground='white', highlightbackground="Black",
                           command=lambda: controller.show_frame("Ophalen"))
        optie3.place(x=0, y=450)

        optie4 = tk.Button(text='Informatie', height=15, width=65, font=('Helvetica', 15, 'bold'),
                           background='royalblue',
                           foreground='white', highlightbackground="Black",
                           command=lambda: controller.show_frame("Informatie"))
        optie4.place(x=775, y=450)

class Registreren(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Registreren", background='yellow', foreground='blue', width=50, height=3 , font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home", command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Stallen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Stallen", background='yellow', foreground='blue', width=50, height=3, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Ophalen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Ophalen", background='yellow', foreground='blue', width=50, height=3, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Informatie(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Informatie", background='yellow', foreground='blue', width=50, height=3, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()