import tkinter as tk


class Gui:
    root = None
    header = None
    content = None
    footer = None
    font = "black"
    bg1 = "light grey"
    bg2 = "beige"
    btn_bkg = "black"


    def __init__(self):
        self.root = tk.Tk("Least Busy Business Locator")
        self.root.geometry('400x300')

        self.header = tk.Frame(self.root, bg = self.bg1)
        self.content = tk.Frame(self.root, bg= self.bg2)
        self.footer1 = tk.Frame(self.root, bg= self.bg1)
        self.footer2 = tk.Frame(self.root, bg=self.bg1)


        self.root.columnconfigure(0, weight=1)  # 100%

        self.root.rowconfigure(0, weight=1)  # 10%
        self.root.rowconfigure(1, weight=8)  # 80%
        self.root.rowconfigure(2, weight=1)  # 10%

        self.header.grid(row=0, columnspan = 3, sticky='news')
        self.content.grid(row=1, columnspan = 5, sticky='news')
        self.footer1.grid(row=2, columnspan = 3, sticky='news')
        self.footer2.grid(row=3, columnspan=3, sticky='news')

        self.initializeLabels()
        self.initializeButtons()
        self.initializeListBox()
        self.initializeTextInput()

        self.root.mainloop()

    def initializeLabels(self):
        title = tk.Label(self.root, text="Welcome!", bg = "light grey")
        title.grid(row=0, sticky='n')

        radius_label = tk.Label(self.root, text = "Enter Distance")
        radius_label.grid(row= 2, column = 0, sticky='w')

        keyword_label = tk.Label(self.root, text="Enter Keyword")
        keyword_label.grid(row=3, column=0, sticky='w')


    def initializeTextInput(self):
        radius_input = tk.Entry(self.root, width = 10)
        keyword_input = tk.Entry(self.root, width = 10)

        radius_input.grid(row=2, column = 1)
        keyword_input.grid(row=3, column=1)


    def initializeButtons(self):
        search = tk.Button(self.root, text = "Search", activebackground = self.btn_bkg)
        search.grid(row=2, column= 2, columnspan = 2, sticky = 'e')



    def initializeListBox(self):
        test = ["text", "1", "testing"]
        listbox = tk.Listbox(self.root, height = 15, width = 30)
        listbox.grid(row=1)


gui = Gui()