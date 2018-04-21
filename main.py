import datetime

import pymongo

from tkinter import *
from tkinter import ttk

from urllib.request import urlopen
from bs4 import BeautifulSoup  

def addGame():
    lstGames.insert(END, txtTitle.get())

    strDate = txtExp.get().split("/")
    date = datetime.datetime(int(strDate[2]), int(strDate[0]), int(strDate[1]))

    entry = {"title": txtTitle.get(),
             "price": int(txtPrice.get()),
             "expiration": date}

    db["games"].insert_one(entry)

def deleteGame():
    lstGames.delete(lstGames.curselection())

def scrape():
    term = txtTitle.get().replace(' ', '+')
    url = "http://store.steampowered.com/search/?term=" + term

    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    price = soup.find("div", {"class": "search_price"})
    if(price.span): # If there's a sale, the original price will be in a span so get rid of it
        price.span.extract()       
    price = price.text.strip()
      
    print(price)  

username = "admin"
password = "passwordd"
    
client = pymongo.MongoClient("mongodb+srv://" + username + ":" + password + "@cluster0-kaauu.mongodb.net")
db = client['sale-tracker']

# Main window
root = Tk()
root.title = "Sale Tracker"  

# Frame containing widgets to add a new game
content = ttk.Frame(root, padding=(10, 5), width=400, height=250)
content.grid(column=0, row=0, sticky = (N, S, E, W))

addFrame = ttk.Frame(content, borderwidth=5, relief=SOLID)
addFrame.grid(column=0, row=0, sticky = (N, S, E, W))
# ---v
label1 = ttk.Label(addFrame, text="Title:")
label1.grid(column=0, row = 0, sticky=W)   

label2 = ttk.Label(addFrame, text="Stores:")
label2.grid(column=1, row = 1)
    
title = StringVar()
txtTitle = ttk.Entry(addFrame, textvariable=title)
txtTitle.grid(column=0, row=1, sticky=NW)

storesFrame = ttk.Frame(addFrame, borderwidth=5, relief="solid")
storesFrame.grid(column=1, row=2, rowspan=3)
#---v
checkSteam = StringVar()
chkSteam = ttk.Checkbutton(storesFrame, text="Steam", variable=checkSteam)
chkSteam.grid(column=0, row=0)

checkOrigin = StringVar()
chkOrigin = ttk.Checkbutton(storesFrame, text="Origin", variable=checkOrigin)
chkOrigin.grid(column=0, row=1)
# ----

label3 = ttk.Label(addFrame, text="Price:")
label3.grid(column=0, row = 2, sticky=W)   

price = StringVar()
txtPrice = ttk.Entry(addFrame, textvariable=price)
txtPrice.grid(column=0, row=3)

label4 = ttk.Label(addFrame, text="Expiration:")
label4.grid(column=0, row = 4, sticky=W)

expiration = StringVar()
txtExp = ttk.Entry(addFrame, textvariable=expiration)
txtExp.grid(column=0, row=5)

btnAdd = ttk.Button(addFrame, text='Add', command=addGame)
btnAdd.grid(column=0, row=6, columnspan=2)
#-----------------------------------------------------

listFrame = ttk.Frame(content, borderwidth=5, relief=SOLID)
listFrame.grid(column=1, row=0, sticky=(N, S))

gamesScrollbar = Scrollbar(listFrame)
gamesScrollbar.grid(column=1, row=0, sticky=(N, S))

lstGames = Listbox(listFrame)
lstGames.grid(column=0, row=0)

lstGames.config(yscrollcommand=gamesScrollbar.set)
gamesScrollbar.config(command=lstGames.yview)

#gamesFrame = ttk.Frame(listFrame, borderwidth=5, relief="sunken", padding = 10)
#gamesFrame.grid(column=0, row=0)

#label4 = ttk.Label(gamesFrame, text="Fallout 4")
#label4.grid(column=0, row = 0) 

#label5 = ttk.Label(gamesFrame, text="Nier: Automata")
#label5.grid(column=0, row = 1) 

btnDelete = ttk.Button(listFrame, text='Delete', command=deleteGame)
btnDelete.grid(column=0, row=1)

root.mainloop()
