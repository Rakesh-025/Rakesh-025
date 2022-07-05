import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Maintenance_cost':50000, 'Marketing_cost':9000, 'Profit_Margin':6500,'Level_of_Course': 2,'Duration_of_coaching_in_Hours': 120})

print(r.json())