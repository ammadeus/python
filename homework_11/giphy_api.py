import requests

api_key = "nWbuaJunIa1dCSpxZ5Klq1HoRGVCfMRG"
search_word = input("Enter keyworld for the GIF: ")

url = f"https://api.giphy.com/v1/gifs/search?q={search_word}&api_key={api_key}&limit=5"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    gif_links = [item['images']['downsized']['url'] for item in data['data']]
else:
    print("Error API.")
    gif_links = []

if gif_links:
    print("Giphy Links GIFs:")
    for link in gif_links:
        print(link)
else:
    print("No-one GIFs.")