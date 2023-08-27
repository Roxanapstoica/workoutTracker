## API, POST requests, Authorization Headers, Environment variables
import requests
import datetime

APP_ID = '436d9952'
API_KEY = '5c9581e55c1b57ddf3ab9cb2b4577382'
ENDPOINT_NUTRITIONIX = 'https://trackapi.nutritionix.com/v2/natural/exercise' ### https://trackapi.nutritionix.com/v2/natural/exercise
ENPOINT_SHEETY = "https://api.sheety.co/"
plainttextinput = input("What exercices did you do today? [plaintext] ")
# sheety_prj_name = "workoutTracker"
# sheety_sheet_name = "workouts"
sheety_url = "https://api.sheety.co/b2582ffea389e1ca201ad5d7b54dea55/workoutTracker/workouts"
print(sheety_url)
print(datetime.date)
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
#   'x-remote-user-id': 0,
}

parameters = {
    "query":plainttextinput,
    "gender":"female",
    "weight_kg":73,
    "height_cm":171,
    "age":41,
}

response = requests.post(url=ENDPOINT_NUTRITIONIX,json=parameters,headers=headers)
result = response.json()
print(result)

### use the Sheety API to generate a new row of data in your Google Sheet for each of the exercises that you get back from the Nutritionix API.
### The date and time columns should contain the current date and time from the Python datetime module.
### Sheety turns your spreadsheet into something called a Restful JSON API. It means you can access your spreadsheets data in a
# standard way using simple URLs and HTTP requests.
