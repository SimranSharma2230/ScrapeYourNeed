from tkinter import *
from bs4 import BeautifulSoup
from showResultEdu1 import ShowResult
import tkinter as tk
from tkinter import messagebox
import requests
import csv


class Schools(object):

    def __init__(self, url):

        self.url = url


    def retrive_schools(self):
        rows=[]
        rows.append(["School","Location"])

        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
    
        all_schools = soup.find_all('div', class_='flex-child')
        i=0
        print("length of all_schools : "+ str(len(all_schools)))
        for school in all_schools:
            row=[]
            i=i+1
            school_title = ""
        
            school_loc = ""
            #school_price =  ""
            #school_detail = ""
            #school_image = ""
           
        
            if(i==5):break
        
            t = school.find('a')
            if t is not None:
                title = t.getText().strip()
                a = title.split('[',1)
                school_title = a[0]
                
            
            
                t = school.find('span',class_='address')
                if t is not None:
                    school_loc = t.getText().strip()
                
                #t = school.find('span',class_='_2TVI3')
                #if t is not None:
                    #school_detail = t.getText().strip()
                
                #t = school.find('span',class_='_2tW1I')
                #if t is not None:
                    #school_title = t.getText().strip()

                #t = school.find('figure',class_='_2grx4')
                #if t is not None:
                    #school_image = t.pic['src']

                row.append(school_title)
                row.append(school_loc)
                
                rows.append(row)
                
            
            
                print("********************************  " , i," ********************************")
                print("\n",school_title)
                print("**********************************************************************")        
                print("\n\t Location: ",school_loc)
                #print("\n\t Price: ",school_price)
                #print("\n\t Org: ",school_org)
                #print("\n\t Detail: ",school_detail)
        if (len(rows)-1)>0:
            #store in csv file
            
            csv.register_dialect('myDialect', delimiter = ',')

            with open('scrapResult.csv', 'w' , encoding='utf-8') as f:
                writer = csv.writer(f, dialect='myDialect')
                writer.writerows(rows)

            f.close()
            root=Tk()
            s = ShowResult(root,"scrapResult.csv",self.url)
            s.mainloop()
        else:
            tk.messagebox.showinfo("school Scrapper","No matching schools found")
    
if __name__ == '__main__':
    a=Schools("https://www.meritnation.com/schools-in-haridwar-50012")
    a.retrive_schools()
