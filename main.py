import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import json
import tkinter as tk
import frames

wn = tk.Tk()
wn.wm_geometry("500x500")
wn.title("Search")


search_frame = frames.SearchFrame(wn)

load_dotenv()

os.environ['SPOTIPY_CLIENT_ID'] = os.getenv('SPOTIPY_CLIENT_ID')
os.environ['SPOTIPY_CLIENT_SECRET'] = os.getenv('SPOTIPY_CLIENT_SECRET')
os.environ['SPOTIPY_REDIRECT_URI'] = os.getenv('SPOTIPY_REDIRECT_URI')

auth_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=auth_manager)

search_frame.frame.grid(row=0, column=0, sticky="news")
search_frame.frame.tkraise()
wn.mainloop()
