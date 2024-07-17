from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.find_all(name="h3",class_="listicleItem_listicle-item__title__BfenH")

movies_names = [movie.get_text() for movie in movies]
movies_names.reverse()

with open("movies.txt", "w") as file:
    file.write("\n".join(movies_names))

