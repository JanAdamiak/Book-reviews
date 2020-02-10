import requests

res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "MfTaW4OWrDbaVyjZPn4A8w", "isbns": "9781632168146"})

print(res.json())
