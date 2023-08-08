import requests

api_key = "df379cdfdfef4813a2a24fe1d462487a"
url = "https://newsapi.org/v2/everything?q=nasa&from=2023-07-08&sortBy=publishedAt&"\
      "apiKey=df379cdfdfef4813a2a24fe1d462487a"

request = requests.get(url)

content = request.json()

for article in content["articles"]:
    print(article["title"])
