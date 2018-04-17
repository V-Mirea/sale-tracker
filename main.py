import pymongo
from steam import SteamClient

from tkinter import *
from tkinter import ttk

def createGui():
    root = Tk()
    root.title("Sale Tracker")


def main():
    username = "admin"
    password = "passwordd"

    client = pymongo.MongoClient("mongodb+srv://" + username + ":" + password + "@cluster0-kaauu.mongodb.net")
    db = client['sale-tracker']

    #createGui()

    cli = SteamClient()

    session = cli.get_web_session()  # returns requests.Session
    session.get('https://store.steampowered.com')

if __name__ == "__main__":
    main()