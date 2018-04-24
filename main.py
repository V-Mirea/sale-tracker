import datetime
import decimal
from decimal import Decimal

import pymongo

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from urllib.request import urlopen
from bs4 import BeautifulSoup

from uuid import getnode as getMac

def clearForm():
    for txtbox in filter(lambda w:isinstance(w, Entry), addFrame.children.values()):
        txtbox.delete(0, END)

def addGame():
    title = txtTitle.get()

    #strDate = txtExp.get().split("/")
    #date = datetime.datetime(int(strDate[2]), int(strDate[0]), int(strDate[1]))

    entry = {"title": title}

    try:
        amount = Decimal(txtPrice.get())
    except (ValueError, decimal.InvalidOperation):
        amount = getPrice(title, False)[0] - Decimal("0.01") # If no/bad price supplied, set limit to just below current regular price

    price = getPrice(title, True)
    if (amount > price[0]): # Notify user if the game is already cheaper than the price they set
        messagebox.showinfo("It's your lucky day!", title + " is already on sale for " + price[1] + str(price[0]))
    else:
        entry.update({"price": float(amount)})

        try:
            strDate = txtExp.get().split("/")
            date = datetime.datetime(int(strDate[2]), int(strDate[0]), int(strDate[1]))

            entry.update({"expiration": date})
        except (ValueError, IndexError):
            pass

        db["games"].insert_one(entry)
        lstGames.insert(END, title)

    clearForm()

def deleteGame():
    db["games"].find_one_and_delete({"title": lstGames.get(lstGames.curselection())})
    lstGames.delete(lstGames.curselection())

# Takes string with game name and optional boolean for price to get
# Returns price of given game and a character representing currency. Regular price or sale price depending on second argument
def getPrice(game, sale = True):
    term = txtTitle.get().replace(' ', '+')
    url = "http://store.steampowered.com/search/?term=" + term

    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    price = soup.find("div", {"class": "search_price"})
    if(price.strike):
        if(sale == True): # If there's a sale, the original price will be striked so look for that and get rid of it
            price.strike.extract()
        elif(sale == False):
            price = price.strike

    price = price.text.strip()
      
    return Decimal(price[1:]), price[0] # Remove currency sign, convert to number, and return, along with currency

def populateGamesList():
    games = db["games"].find()
    for game in games:
        lstGames.insert(END, game["title"])

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
   
#title = StringVar()
txtTitle = ttk.Entry(addFrame)
txtTitle.grid(column=0, row=1, sticky=NW)

#label2 = ttk.Label(addFrame, text="Stores:")
#label2.grid(column=1, row = 1)
#
#storesFrame = ttk.Frame(addFrame, borderwidth=5, relief="solid")
#storesFrame.grid(column=1, row=2, rowspan=3)
##---v
##checkSteam = StringVar()
#chkSteam = ttk.Checkbutton(storesFrame, text="Steam")
#chkSteam.grid(column=0, row=0)

##checkOrigin = StringVar()
#chkOrigin = ttk.Checkbutton(storesFrame, text="Origin")
#chkOrigin.grid(column=0, row=1)
## ----

label3 = ttk.Label(addFrame, text="Price:")
label3.grid(column=0, row = 2, sticky=W)   

#price = StringVar()
txtPrice = ttk.Entry(addFrame)
txtPrice.grid(column=0, row=3)

label4 = ttk.Label(addFrame, text="Expiration:")
label4.grid(column=0, row = 4, sticky=W)

#expiration = StringVar()
txtExp = ttk.Entry(addFrame)
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

populateGamesList()

lstGames.config(yscrollcommand=gamesScrollbar.set)
gamesScrollbar.config(command=lstGames.yview)

btnDelete = ttk.Button(listFrame, text='Delete', command=deleteGame)
btnDelete.grid(column=0, row=1)

messagebox.showinfo("", getMac())

root.mainloop()
