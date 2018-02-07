import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 15)

class seaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=2)
        container.grid_columnconfigure(0, weight=3)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# def qf(param):
#     print(param)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(padx=25, pady=25)
        # button01 = tk.Button(self, text="Visit Page 1",
        #                     command=lambda: qf("Great Job!"))
        button01 = ttk.Button(self, text="Visit Page 1",
                              command=lambda: controller.show_frame(PageOne))
        button01.pack(padx=12, pady=12)
        button02 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button02.pack(padx=12, pady=12)

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(padx=25, pady=25)
        button01 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button01.pack(padx=12, pady=12)
        button02 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button02.pack(padx=12, pady=12)

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(padx=25, pady=25)
        button01 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button01.pack(padx=12, pady=12)
        button02 = ttk.Button(self, text="Visit Page 1",
                             command=lambda: controller.show_frame(PageOne))
        button02.pack(padx=12, pady=12)

app = seaofBTCapp()
app.mainloop()


    
