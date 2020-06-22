from tkinter import *
from bs4 import BeautifulSoup
from showResultEdu import ShowResult
import tkinter as tk
from tkinter import messagebox
import requests
import csv


class College(object):

    def __init__(self, url):

        self.url = url


    def retrive_colleges(self):
        rows=[]
        rows.append(["College","Location","Course","Degree"])

        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
    
        all_colleges = soup.find_all('div', class_='cntnt side_spce')
        i=0
        print("length of all_colleges : "+ str(len(all_colleges)))
        for college in all_colleges:
            row=[]
            i=i+1
            college_title = ""
        
            college_loc = ""
            college_course =  ""
            college_degree = ""
            #college_image = ""
           
        
            if(i==5):break
        
            t = college.find('ul',class_='location')
            if t is not None:
                a = t.find('li')
                college_loc = a.getText().strip()
            
            
                t = college.find('div',class_='more_courses')
                if t is not None:
                     a = t.find('a')
                     college_course = a.getText().strip()
                     a = t.find('li')
                     college_degree = a.getText().strip()
                     
                
                t = college.find('div',class_='details')
                if t is not None:
                    a = t.find('h2')
                    college_title = a.getText().strip()

                

                row.append(college_title)
                row.append(college_loc)
                row.append(college_course)
                row.append(college_degree)
                
                
                rows.append(row)
                
            
            
                print("********************************  " , i," ********************************")
                print("\n",college_title)
                print("**********************************************************************")        
                print("\n\t location: ",college_loc)
                print("\n\t ",college_course)
                print("\n\t  ",college_degree)
        if (len(rows)-1)>0:
            #store in csv file
            csv.register_dialect('myDialect', delimiter = ',')

            with open('scrapResult.csv', 'w') as f:
                writer = csv.writer(f, dialect='myDialect')
                writer.writerows(rows)

            f.close()
            root=Tk()
            s = ShowResult(root,"scrapResult.csv",self.url)
            s.mainloop()
        else:
            tk.messagebox.showinfo("Scrape Your Needs","No matching colleges found")
    
if __name__ == '__main__':
    a=College("https://www.jagranjosh.com/institutes-colleges/engineering-colleges-in-hyderabad")
    a.retrive_colleges()
