import requests
from bs4 import BeautifulSoup

url = "https://open.spotify.com/playlist/37i9dQZF1DXcBOn0qcyd5C?si=775fec692cac4bd0&nd=1"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

songs = []

for span in soup.find_all('div', {'class': 'Type__TypeElement-sc-goli3j-0 kHHFyx t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line'}):
    songs.append(span.text.strip())

print(songs)
