import requests, json

url = "http://api.exchangeratesapi.io/v1/latest?access_key=694a8a9830f3a6a6e529993740f8b190&format=1"

data = requests.get(url).json()

eur_rub_rate = {
    'RUB': data["rates"]["RUB"]
}

json_object = json.dumps(eur_rub_rate)

with open('data.json', 'a') as file:
    json.dump(json_object, file)

print(eur_rub_rate)

