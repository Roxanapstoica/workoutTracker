## API, POST requests, Authorization Headers, Environment variables
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import os


GENDER = "female"
WEIGHT_KG = 73
HEIGHT_CM = 171
AGE = 41

APP_ID = os.environ["ENV_NIX_API_ID"]
APP_KEY = os.environ["ENV_NIX_API_KEY"]
ENDPOINT_NUTRITIONIX = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]

plainttextinput = input("What exercices did you do today? [plaintext] ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}


parameters = {
    "query":plainttextinput,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE,
}

response = requests.post(url=ENDPOINT_NUTRITIONIX,json=parameters,headers=headers)
result = response.json()
print(result)

today = datetime.now()
today_date = today.strftime("%Y/%m/%d")
today_hour = today.strftime("%I:%M:%S")

bearer_headers = {
    "Authorization":f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
}

for exercise in result["exercises"]:
    sheet_input = {
        "workout":{
            "date":today_date,
            "time":today_hour,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheety_endpoint,json=sheet_input,headers=bearer_headers)
    print(sheet_response.text)
