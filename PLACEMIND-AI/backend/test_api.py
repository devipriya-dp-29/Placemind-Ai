import requests
import json

try:
    print("Testing API locally...")
    response = requests.get('http://127.0.0.1:8000/api/placements/companies/')
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.text}")
    
    data = response.json()
    print(f"Count from API: {len(data)}")
except Exception as e:
    print(f"Error: {e}")
