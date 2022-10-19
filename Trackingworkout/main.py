# 함수호출
from time import strftime
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv(verbose=True, override=True)

# 구글시트 사본 생성
# api key 생성, https://developer.nutritionix.com
appID = os.environ['appID']
appKeys = os.environ['appKeys']

# Solution - https://gist.github.com/angelabauer/dd71d7072626afd728e1730584c6e4b8
# Nutritionix API_Docs - https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#

GENDER = 'male'
WEIGHT_KG = '65'
HEIGHT_CM = '165'
AGE = '27'

exercise_endpoint = os.environ['exercise_endpoint']
exercise_test = input('Which exercise you did? ')

headers = {
    'x-app-id': appID,
    'x-app-key': appKeys,
}

parameters = {
    'query': exercise_test,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

# Step4
# Sol - https://gist.github.com/angelabauer/164864b78175bb1ecd3d3fd7f4ee39b7

sheety_endpoint = os.environ['sheety_endpoint']

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime('%X')

for exercise in result['exercises']:
    sheet_inputs = {
        'workout': {
            'date': today_date,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheet_response = requests.post(sheety_endpoint,
                                   json=sheet_inputs,
                                   auth=(
                                       os.environ['ID'],
                                       os.environ['PW'],
                                   ))

    print(sheet_response.text)

# Step5
# Sol - https://gist.github.com/TheMuellenator/974c39779ec516c4c60e918c001e48ba
