import requests
import socket

# Get local IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"Testing API on {local_ip}...")
try:
    response = requests.get(f'http://{local_ip}:8000/api/placements/companies/')
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.text}")
except Exception as e:
    print(f"Error connecting to {local_ip}: {e}")

print("\nTesting API on 127.0.0.1...")
try:
    response = requests.get('http://127.0.0.1:8000/api/placements/companies/')
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.text}")
except Exception as e:
    print(f"Error connecting to 127.0.0.1: {e}")
