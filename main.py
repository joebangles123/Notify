import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import json
import tkinter as tk

wn = tk.Tk()
wn.wm_geometry("500x500")
wn.title("Search")

search_frame = tk.Frame(wn)

search_lbl = tk.Label(search_frame, text="Search term: ", font=("Arial", 12, "bold"))
search_lbl.grid(row=0, column=0, sticky="w")

search_ent = tk.Entry(search_frame)
search_ent.grid(row=0, column=1)

search_type_lbl = tk.Label(search_frame, text="Search type", font=("Arial", 12, "bold"))
search_type_lbl.grid(row=1, column=0, sticky="w")

checks = {"artist": tk.Checkbutton(search_frame, text="artists"),
          "album": tk.Checkbutton(search_frame, text="albums"),
          "track": tk.Checkbutton(search_frame, text="songs"),
          "playlist": tk.Checkbutton(search_frame, text="playlists"),
          "show": tk.Checkbutton(search_frame, text="podcasts"),
          "episode": tk.Checkbutton(search_frame, text="episodes")}

n = 2
for check in checks.values():
    check.grid(row=n, column=0, sticky="w")
    n += 1

load_dotenv()

os.environ['SPOTIPY_CLIENT_ID'] = os.getenv('SPOTIPY_CLIENT_ID')
os.environ['SPOTIPY_CLIENT_SECRET'] = os.getenv('SPOTIPY_CLIENT_SECRET')
os.environ['SPOTIPY_REDIRECT_URI'] = os.getenv('SPOTIPY_REDIRECT_URI')

auth_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=auth_manager)

search_frame.grid(row=0, column=0, sticky="news")
search_frame.tkraise()
wn.mainloop()
