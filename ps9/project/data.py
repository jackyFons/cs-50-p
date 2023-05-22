import pandas as pd
import matplotlib.pyplot as plt


class Data:
	def __init__(self, file):
		self.data = pd.read_csv(file)
		self.data = self.clean_data(self.data)

		# These are used for labeling menu items
		gen_list = self.data["Genre"].str.split(", ")
		self.genres = sorted(gen_list.explode().unique().tolist())
		self.p_ratings = sorted(self.data["Parental Rating"].unique().tolist())
		self.decades = {
		"30s": list(range(1930, 1940)),
		"40s": list(range(1940, 1950)),
		"50s": list(range(1950, 1960)),
		"60s": list(range(1960, 1970)),
		"70s": list(range(1970, 1980)),
		"80s": list(range(1980, 1990)),
		"90s": list(range(1990, 2000)),
		"10s": list(range(2000, 2016))
		}


	def clean_data(self, data):
		# Renames columns, deletes unused columns, and removes unnecessary characters

		data = data.drop(["index", "votes"], axis=1)
	
		data = data.rename(columns={"movie_name": "Movie Name", "year_of_release": "Release Year",
		 "category": "Parental Rating", "run_time": "Run Time", "genre": "Genre", "imdb_rating": "IMDb Rating",
		 "gross_total": "Gross Total"})

		data["Release Year"] = data["Release Year"].replace(r"[^\d.]", "", regex=True)

		return data


	def filter_movies(self, key: str, boundary: str):
		# Returns new DataFrame containing filtered content
		movies = self.data
		match key:
			case "Decades":
				years = self.decades[boundary]
				movies = movies[movies["Release Year"].apply(lambda x: int(x) in years)]
			case "Genre":
				movies = movies[movies[key].apply(lambda x: boundary in x)]
			case "Parental Rating":
				movies = self.data[self.data[key] == boundary]
		return movies


	def make_fig(self, key: str):
		# Returns created bar chart 
		count = []
		bounds = []
		x_prompt = ""

		match key:
			case "Decades":
				bounds = list(self.decades.keys())
				x_prompt = "Decades"
			case "Genre":
				bounds = self.genres
				x_prompt = "Genres"
			case "Parental Rating":
				bounds = self.p_ratings
				x_prompt = "Parental Ratings"
		
		for b in bounds:
			count.append(len(self.filter_movies(key, b)))
		
		fig = plt.figure(figsize = (12, 7))
		plt.bar(bounds, count)
		plt.xlabel(x_prompt)
		plt.ylabel("Number of movies")
		plt.xticks(rotation=45)
		plt.subplots_adjust(bottom=.25)
		return fig