import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Maintenance_cost':1000, 'Marketing_cost':100, 'Profit_Margin':100,'Level_of_Course': 2,'Duration_of_coaching_in_Hours': 100})

print(r.json())
