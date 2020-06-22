from tkinter import *
from bs4 import BeautifulSoup
from showResultHouse import ShowResult
import tkinter as tk
from tkinter import messagebox
import requests
import csv


class Sale(object):

    def __init__(self, url):

        self.url = url


    def retrive_housing(self):
        rows=[]
        rows.append(["Title","Location","Price","Detail"])

        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
    
        all_houses = soup.find_all('li', class_='EIR5N')
        i=0
        print("length of all_houses : "+ str(len(all_houses)))
        for house in all_houses:
            row=[]
            i=i+1
            house_title = ""
        
            house_loc = ""
            house_price =  ""
            house_detail = ""
           
           
        
            if(i==5):break
        
            t = house.find('span',class_='tjgMj')
            if t is not None:
                house_loc = t.getText().strip()
            
            
                t = house.find('span',class_='_89yzn')
                if t is not None:
                    house_price = t.getText().strip()
                
                t = house.find('span',class_='_2TVI3')
                if t is not None:
                    house_detail = t.getText().strip()
                
                t = house.find('span',class_='_2tW1I')
                if t is not None:
                    house_title = t.getText().strip()

                

                row.append(house_title)
                row.append(house_loc)
                row.append(house_price)
                row.append(house_detail)
                #row.append(house_image)
                
                
                rows.append(row)
                
            
            
                print("********************************  " , i," ********************************")
                print("\n",house_title)
                print("**********************************************************************")        
                print("\n\t Location: ",house_loc)
                print("\n\t Price: ",house_price)
                #print("\n\t Org: ",house_org)
                print("\n\t Detail: ",house_detail)
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
            tk.messagebox.showinfo("house Scrapper","No matching houses found")
    
if __name__ == '__main__':
    a=Sale("https://www.olx.in/delhi_g2001152/for-Sale-houses-apartments_c1723")
    a.retrive_housing()
