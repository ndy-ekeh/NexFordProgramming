import zipfile
import os
import pandas as pdr
import matplotlib.pyplot as plot
import seaborn as sns

# Unzip the file
#with zipfile.ZipFile("/Users/ndubisiekeh/Documents/GitHub/NexFordProgramming/VisualAssisgnments/netflix_data.zip", "r") as zip_ref:
  #  zip_ref.extractall(".")

os.rename("netflix_data.csv", "Netflix_shows_movies.csv")

# Load the data
dataValue = pdr.read_csv("Netflix_shows_movies.csv")

print(dataValue.isnull().sum())


dataValue['director'].fillna('Unknown', inplace=True)
dataValue['cast'].fillna('Unknown', inplace=True)
dataValue['country'].fillna('Unknown', inplace=True)
dataValue.dropna(subset=['date_added', 'rating'], inplace=True)


print(dataValue.info())
print(dataValue.describe(include='all'))


print(dataValue['type'].value_counts())
print(dataValue['rating'].value_counts())

genres = dataValue['listed_in'].str.split(', ', expand=True).stack()
top_genres = genres.value_counts().head(10)

plot.figure(figsize=(10,6))
sns.barplot(y=top_genres.index, x=top_genres.values, palette="Set2")
plot.title("The Most Top 10 Watched Genres on Netflix")
plot.xlabel("Count")
plot.ylabel("Genre")
plot.tight_layout()
plot.show()

plot.figure(figsize=(10,6))
sns.countplot(data=dataValue, x='rating', order=dataValue['rating'].value_counts().index, palette="muted")
plot.title("Netflix Distribution Ratings")
plot.xlabel("Rating")
plot.ylabel("Count")
plot.xticks(rotation=45)
plot.tight_layout()
plot.show()