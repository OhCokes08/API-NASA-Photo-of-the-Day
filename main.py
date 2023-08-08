import requests
from send_email import sendEmail

subject = "nasa"

api_key = "df379cdfdfef4813a2a24fe1d462487a"
url = f"https://newsapi.org/v2/everything?q={subject}&"\
      "from=2023-07-08&sortBy=publishedAt&"\
      "apiKey=df379cdfdfef4813a2a24fe1d462487a&"\
      "language=en"

request = requests.get(url)

content = request.json()

body = ""
for article in content["articles"]:
    body = "Subject: Todays Space News" + "\n" + body + article["title"] + "\n" + article["url"] + 2*"\n"
    message = body

body = body.encode("utf-8")
sendEmail(message=body)