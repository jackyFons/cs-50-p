import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from pandastable.core import Table, config
from data import Data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
    NavigationToolbar2Tk)


global data
data = Data("movies.csv")

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.style = ThemedStyle()
        self.style.theme_use("elegance")

        self.geometry("1300x700")
        self.title("IMDb Top 100 Movies")
        self.resizable(0,0)
        
        self.add_menubar()

        self.frame = ttk.Frame(self, width=1250, height=650)
        self.frame.pack(expand=True)

        self.table = self.create_table(self.frame)
        self.table.show()


    def add_menubar(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Creating menus for filtering
        filter_menu = tk.Menu(menubar, tearoff=False) 

        genre_menu = tk.Menu(filter_menu, tearoff=False)
        genres = data.genres
        for genre in genres:
            genre_menu.add_command(label=genre, command=lambda genre=genre:self.update_data("Genre", genre))

        p_ratings_menu = tk.Menu(filter_menu, tearoff=False)
        p_ratings = data.p_ratings
        for p in p_ratings:
            p_ratings_menu.add_command(label=p, command=lambda p=p:self.update_data("Parental Rating", p))

        dec_menu = tk.Menu(filter_menu, tearoff=False)
        decade = data.decades.keys()
        for d in decade:
            dec_menu.add_command(label=d, command=lambda d=d:self.update_data("Decades", d))

        menubar.add_cascade(label="Filter by", menu=filter_menu)
        filter_menu.add_cascade(label="Genres", menu=genre_menu)
        filter_menu.add_cascade(label="Decades", menu=dec_menu)
        filter_menu.add_cascade(label="Parental Ratings", menu=p_ratings_menu)
        filter_menu.add_command(label="Show All", command=lambda: self.update_data("All", ""))

        # Creating menus for charts
        chart_menu = tk.Menu(menubar, tearoff=False)

        chart_menu.add_command(label="Genres", command=lambda:self.create_chart("Genre"))
        chart_menu.add_command(label="Decades", command=lambda:self.create_chart("Decades"))
        chart_menu.add_command(label="Parental Ratings", command=lambda:self.create_chart("Parental Rating"))

        menubar.add_cascade(label="Create chart by", menu=chart_menu)


    def create_table(self, frame):
        # Creates table to show the CSV contents
        t = Table(self.frame, dataframe=data.data, width=1250, height=650)
        options = config.load_options()
        options = {"fontsize":12,"cellwidth": 120, "align": "center", "floatprecision": 1}
        config.apply_options(options, t)
        t.editable = False
        t.autoResizeColumns()
        return t

 
    def update_data(self, key, boundary):
        # Gets filtered contents of CSV file
        if key == "All":
            self.table.model.df = data.data
        else:
            self.table.model.df = data.filter_movies(key, boundary)
        self.table.redraw()


    def create_chart(self, key):
        # Creates a new window with charts
        chartWindow = tk.Toplevel(self)
        chartWindow.geometry("1150x700")
        fig = data.make_fig(key)
        canvas = FigureCanvasTkAgg(fig, master=chartWindow)
        canvas.draw()
        canvas.get_tk_widget().pack()


if __name__ == "__main__":
    window = Window()
    window.mainloop()