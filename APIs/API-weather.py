import requests

ciudad = "Vitoria-Gasteiz"
API_KEY = "1dfc88f422f94f708c3225306241504"

uri = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={ciudad}&aqi=yes"

response = requests.get(uri) 

print(response.status_code)
print(response.text)
