import requests
import os

def search_jobs(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": os.getenv("GOOGLE_API_KEY"),
        "cx": os.getenv("GOOGLE_CSE_ID"),
        "num": 10
    }
    response = requests.get(url, params=params)
    return response.json().get("items", [])
