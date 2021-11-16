import tkinter as tk


class SearchFrame:
    def __init__(self, wn):
        self.frame = tk.Frame(wn)

        self.targets = []
        self.targettext = tk.StringVar()
        self.targettext.set("none")

        search_lbl = tk.Label(self.frame, text="Search term: ", font=("Arial", 12, "bold"))
        search_lbl.grid(row=0, column=0, sticky="w")

        search_ent = tk.Entry(self.frame)
        search_ent.grid(row=0, column=1)

        search_type_lbl = tk.Label(self.frame, text="Search type: ", font=("Arial", 12, "bold"))
        search_type_lbl.grid(row=1, column=0, sticky="w")

        search_type = tk.Menubutton(self.frame, textvariable=self.targettext, font=("Arial", 12, "bold"))
        search_type.grid(row=1, column=1, sticky="w")

        type_menu = tk.Menu(search_type)
        search_type.configure(menu=type_menu)

        self.checks = {"artist": type_menu.add_checkbutton(label="artists"),
                       "album": type_menu.add_checkbutton(label="albums"),
                       "track": type_menu.add_checkbutton(label="songs"),
                       "playlist": type_menu.add_checkbutton(label="playlists"),
                       "show": type_menu.add_checkbutton(label="podcasts"),
                       "episode": type_menu.add_checkbutton(label="episodes")}



    def open_frame(self):
        self.frame.tkraise()
        self.targettext = ", ".join(self.targets)
