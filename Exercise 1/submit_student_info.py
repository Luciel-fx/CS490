import json
import requests

with open("student_info.json", "r") as file:
    student_info = json.load(file)

getURL = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info?UCID=iz26&section=101"

try:
    getRES = requests.get(getURL)
    if getRES.status_code == 200 and getRES.json():
        print("Records already exist in the database. No duplicates can be made.")
    else:
        postURL = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"
        response = requests.post(postURL, json = student_info)

        print("Status:", response.status_code)
        print("Body:", response.text)

        if response.status_code == 200:
            print("POST request successful.")
        else:
            print("POST request failed.")
except requests.exceptions.RequestException as err:
    print("Error:", err)