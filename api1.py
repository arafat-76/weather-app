import requests
import json
city=input("Enter city to see temperature:")
response=requests.get("https://wttr.in/"+city+"?format=j1")
data=response.json()
temp=data["current_condition"][0]["temp_C"]
feels=data["current_condition"][0]["FeelsLikeC"]
desc=data["current_condition"][0]["weatherDesc"][0]["value"]
print(city,"weather:")
print("Temperature:",temp,"°C")
print("Feels like:",feels,"°C")
print("condition:",desc)
print(response.status_code)
