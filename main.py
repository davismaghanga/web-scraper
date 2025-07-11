from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page =response.text

soup =  BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
article_upvotes = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find("a")["href"]
    article_links.append(link)
    upvote = int(article_tag.find_parent("tr").find_next_sibling("tr").find("span", class_="score").getText().split()[0])
    article_upvotes.append(upvote)

largest_upvote = max(article_upvotes)
index_largest_upvote = article_upvotes.index(largest_upvote)
article_text_largest_upvote = article_texts[index_largest_upvote]
article_link_largest_upvote = article_links[index_largest_upvote]

print(f"The largest upvote is: {largest_upvote}")
print(f"The text of the article with the largest upvote is: {article_text_largest_upvote}")
print(f"The link of the article with the largest upvote is: {article_link_largest_upvote}")

