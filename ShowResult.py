
from tkinter import *
import tkinter.ttk as ttk
import csv
import webbrowser

class ShowResult(Frame):
    def __init__(self,master=None,csvFile="scrapResult.csv",url=None):
        Frame.__init__(self,master)
        self.master=master
        self.csvFile=csvFile
        self.url=url
        self.init_window()
        
    def init_window(self):
        self.master.title("Scrape Your Need")
        self.pack(fill=BOTH,expand=1)
        
        width = 1100
        height = 500
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.master.resizable(0, 0)

        b1 = Button(self.master,text="Go Online",command=self.go_online)
        b1.pack()
        TableMargin = Frame(self.master, width=600)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("Job Title","Organization","Posted","Description","Location"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Job Title', text="Job Title", anchor=W)
        tree.heading('Organization', text="Organization", anchor=W)
        tree.heading('Posted', text="Posted", anchor=W)
        tree.heading('Description', text="Description", anchor=W)
        tree.heading('Location', text="Location", anchor=W)


        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=200)
        tree.column('#4', stretch=NO, minwidth=0, width=200)
        tree.column('#5', stretch=NO, minwidth=0, width=300)

        tree.pack()

        with open(self.csvFile) as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Job_Title = row['Job Title']
                Organization = row['Organization']
                Posted = row['Posted']
                Description = row['Description']
                Location = row['Location']
                tree.insert("", 0, values=(Job_Title, Organization, Posted,Description,Location))

    def go_online(self):
        webbrowser.open_new(self.url)


