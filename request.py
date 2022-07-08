import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Maintenance_cost':1, 'Marketing_cost':1, 'Profit_Margin':1,'Level_of_Course': 2,'Duration_of_coaching_in_Hours': 1})

print(r.json())
