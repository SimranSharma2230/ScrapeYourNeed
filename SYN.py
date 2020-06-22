import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Job import Job
from Education import Education
from Housing import Housing




def scraph():
    
    top=tk.Toplevel()
    top["bg"] = "white"
    p = Housing(top)
    p.mainloop()
def scrapj():
    
    top=tk.Toplevel()
    top["bg"] = "white"
    g = Job(top)
    g.mainloop()
def scrape():
    
    top=tk.Toplevel()
    top["bg"] = "white"
    g = Education(top)
    g.mainloop()    

def aboutus():
    tk.messagebox.showinfo("About Us","used By: Simran and Himanshi")

def quit():
    top.destroy()

    
top = tk.Tk()
top.title("Scrape Your Need")
top["bg"] = "white"

img1 = tk.PhotoImage(file='image\logoimage.gif')
img = tk.PhotoImage(file='image\image.gif')



lblLogo = tk.Label(top, image=img1, bg='white')
lblLogo.grid(row=0, column=0,columnspan=6,sticky=tk.E+tk.W)

lbl = tk.Label(top, text='                                                                                                a python scrapper', bg='black', fg='white', borderwidth = 0,font=3)
lbl.grid(row=1, column=0, columnspan=5 ,sticky=tk.E+tk.W)

btnHouse = tk.Button(top, text='Housing', command = scraph, fg= 'white', width=7, borderwidth = 1,font=10, bg='light slate gray', activebackground='grey30', activeforeground='white')
btnHouse.grid(row=2, column=0,sticky=tk.E+tk.W)

btnJob = tk.Button(top, text='Job', command = scrapj, fg= 'white', width=7, borderwidth = 1,font=10, bg='light slate gray', activebackground='grey30', activeforeground='white')
btnJob.grid(row=2, column=1,sticky=tk.E+tk.W)

btnEdu = tk.Button(top, text='Education', command = scrape, fg= 'white', width=7, borderwidth = 1,font=10, bg='light slate gray', activebackground='grey30', activeforeground='white')
btnEdu.grid(row=2, column=2,sticky=tk.E+tk.W)

btnAboutUs = tk.Button(top, text='About Us', command = aboutus, fg= 'white', width=7, borderwidth = 1,font=10, bg='light slate gray', activebackground='grey30', activeforeground='white')
btnAboutUs.grid(row=2, column=3,sticky=tk.E+tk.W)

btnQuit = tk.Button(top, text='Quit', command = quit, fg= 'white', width=7, borderwidth = 1,font=10, bg='light slate gray', activebackground='grey30', activeforeground='white')
btnQuit.grid(row=2, column=4,sticky=tk.E+tk.W)


lblimg = tk.Label(top, image=img, bg='white')
lblimg.grid(row=3, column=0,columnspan=5)



lblFooter1 = tk.Label(top, text='About Web Scrapping ~ concept used in SCRAPE YOUR NEED', bg='light slate gray', fg='black',width=50, borderwidth = 0,font=3)
lblFooter1.grid(row=4, column=0, columnspan=5 ,sticky=tk.E+tk.W)

msg = "Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites.Web scrapping is the process of automatically mining  data or collecting information from the World wide Web.  \n\nIt is the field of active developments sharing a common goal with the semantic web vision, an ambitious initiative that still requires breakthroughs in text processing, semantic understanding, artificial intelligence and human-computer interactions."


lblFooter = tk.Label(top, text=msg,  bg='black', fg='white',width=50, borderwidth = 7,font=3,padx="0",wraplength=450 )
lblFooter.grid(row=5, column=0, columnspan=5 ,sticky=tk.E+tk.W)

top.mainloop()
