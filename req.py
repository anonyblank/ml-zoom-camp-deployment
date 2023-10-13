import requests

#url = "https://bank-score-0865bf0b3f81.herokuapp.com/predict"
url = "http://0.0.0.0/predict"

# client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
client = {"job": "retired", "duration": 445, "poutcome": "success"}

client = requests.post(url, json=client)
print(client.json())
