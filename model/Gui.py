import tkinter as tk
import datetime

from model.ApiRequest import ApiRequest


class Gui:
    root = None
    header = None
    results = None
    footer = None
    FONT = "black"
    BG1 = "light grey"
    BG2 = "beige"
    BTN_BKG = "black"
    INPUT_BOX_WIDTH = 20
    MAX_LISTINGS = 15

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Least Busy Business Locator")
        self.root.geometry('1200x400')

        self.initialize_frames()
        self.configure_rows_and_columns()
        self.initialize_inputs()
        self.initialize_results_list()

        tk.mainloop()

    def initialize_results_list(self):
        self.resultsList = tk.Listbox(self.results)
        self.resultsList.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nsew')

        self.scrollbar = tk.Scrollbar(self.results, orient='vertical')
        self.scrollbar.grid(row =0, column = 2, rowspan=2, sticky='nsew')
        self.scrollbar.config(command=self.resultsList.yview)
        #self.resultsList.config(yscrollcommand = self.scrollbar.set)

    def initialize_inputs(self):
        self.message_label = tk.Label(self.header, width=100, text="Welcome User!")
        self.message_label.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=10)

        self.keyword_entry = tk.Entry(self.entryFrame1, width=self.INPUT_BOX_WIDTH)
        self.keyword_entry.grid(row=0, column=1, sticky='w')
        self.keyword_label = tk.Label(self.entryFrame1,
                                      text="Enter Keyword", width=self.INPUT_BOX_WIDTH, bg=self.BG1)
        self.keyword_label.grid(row=0, column=0, sticky='w', padx=20, pady=20)

        self.radius_entry = tk.Entry(self.entryFrame2, width=self.INPUT_BOX_WIDTH)
        self.radius_entry.grid(row=0, column=1, sticky='w')
        self.radius_label = tk.Label(self.entryFrame2,
                                     text="Enter Max Distance (in km)", width=self.INPUT_BOX_WIDTH, bg=self.BG1)
        self.radius_label.grid(row=0, column=0, sticky='w', padx=20)

        self.search_btn = tk.Button(self.entryFrame3, text="Search", width=self.INPUT_BOX_WIDTH, )
        self.search_btn.grid(row=0, column=0, sticky='e', padx=80)
        self.search_btn.configure(command=self.search)

    def initialize_frames(self):
        self.header = tk.Frame(self.root, bg=self.BG1)
        self.results = tk.Frame(self.root, bg=self.BG2)
        self.entryFrame1 = tk.Frame(self.root, bg=self.BG1)
        self.entryFrame2 = tk.Frame(self.root, bg=self.BG1)
        self.entryFrame3 = tk.Frame(self.root, bg=self.BG1)

        self.header.grid(row=0, column=0, sticky='news')
        self.results.grid(row=1, column=0, rowspan=3, columnspan=2, sticky='news')
        self.entryFrame1.grid(row=2, column=0, sticky='news')
        self.entryFrame2.grid(row=3, column=0, sticky='news')
        self.entryFrame3.grid(row=4, column=0, sticky='news')

    def configure_rows_and_columns(self):
        self.root.rowconfigure(0, weight=1)  # 10%
        self.root.rowconfigure(1, weight=8)  # 80%
        self.root.rowconfigure(2, weight=1)  # 10%
        self.root.rowconfigure(3, weight=1)  # 10%
        self.root.rowconfigure(4, weight=1)  # 10%
        self.root.columnconfigure(0, weight=1)

        self.results.columnconfigure(0, weight=1)
        self.results.columnconfigure(1, weight=1)
        self.results.rowconfigure(0, weight=1)
        self.results.rowconfigure(1, weight=1)

        self.header.columnconfigure(0, weight=1)
        self.header.columnconfigure(1, weight=1)
        self.header.rowconfigure(1, weight=0)

    def search(self):
        api_request = ApiRequest()
        radius = self.radius_entry.get()
        keyword = self.keyword_entry.get()
        search_list = api_request.get_place_information(radius, keyword, self.MAX_LISTINGS)
        self.update_results(search_list)
        self.radius_entry.delete(0, 'end')
        self.keyword_entry.delete(0, 'end')
        self.update_message_label(api_request.latitude, api_request.longitude)

    def update_message_label(self, latitude, longitude):
        date = datetime.date.today()
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        string_msg = f"Search results from your coordinates of {latitude}, {longitude} at {date} {hour}:{minute}"
        self.message_label['text'] = string_msg

    def update_results(self, biz_list):
        self.resultsList.delete(0, 'end')
        counter = 0
        pos = 1
        for biz in biz_list:
            name = biz.name
            address = biz.address
            number = biz.number
            rating = biz.rating
            busyness = biz.busyness
            d = biz.distance
            distance = f"{d} km" if d != "N/A" else d
            entry = f"#{pos}. Name: {name} | Address: {address} | Number: {number} | " \
                    f"Rating: {rating} | Busyness: {busyness} | Distance: {distance}"
            self.resultsList.insert(counter, entry)
            counter += 1
            pos += 1


gui = Gui()
