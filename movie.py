from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movie_page = response.text

soup = BeautifulSoup(movie_page,"html.parser")
movie_info = soup.find_all(name="span", class_="content_content__i0P3p")
movie_titles = []
for span in movie_info:
    h2 = span.find("h2")
    if h2:
        strong = h2.find("strong")
        if strong:
            movie_titles.append(strong.getText())

movie_titles.reverse()
with open("Top 100 movies.txt","w") as file:
    for title in movie_titles:
        file.write(f"{title}\n")
