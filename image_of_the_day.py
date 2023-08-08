import streamlit as st
import requests


api_key = "RAP7x1wQJExt5dvaeLVzXXehFAb9DdVbcA7jB6M1"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"


request1 = requests.get(url)
data = request1.json()

heading = data['title']
explanation = data['explanation']
image = data['url']

img_filepath = "img.png"
request2 = requests.get(image)
with open(img_filepath,"wb") as file:
    file.write(request2.content)

st.title(heading)
st.image(img_filepath)
st.info(explanation)