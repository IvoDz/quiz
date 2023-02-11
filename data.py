import requests

parametres = {
    "amount":10,
    "type":"boolean",
    "category":19
}

response = requests.get(url = "https://opentdb.com/api.php", params=parametres)
response.raise_for_status()
question_data = response.json()["results"]
