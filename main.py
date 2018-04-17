import pymongo
#from steam import SteamClient

from tkinter import *
from tkinter import ttk

def createGui():
    # Main window
    root = Tk()
    root.title = "Sale Tracker"  

    # Frame containing widgets to add a new game
    content = ttk.Frame(root, padding=(10, 5), borderwidth=5, relief="sunken", width=400, height=250)
    content.grid(column=0, row=0)

    addFrame = ttk.Frame(content, borderwidth=5, relief="sunken")
    content.grid(column=0, row=0)

    label = ttk.Label(addFrame, text="heelo")
    label.grid(column=1, row = 0)

    listFrame = ttk.Frame(content, borderwidth=5, relief="sunken")
    content.grid(column=1, row=0)

    root.mainloop()

def main():
    username = "admin"
    password = "passwordd"

    client = pymongo.MongoClient("mongodb+srv://" + username + ":" + password + "@cluster0-kaauu.mongodb.net")
    db = client['sale-tracker']

    createGui()

if __name__ == "__main__":
    main()