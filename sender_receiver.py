import sys
import os
import requests
# Add parent directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from urls import (
    BASE_URL,
    auth,
)
from storage import (
    save_token,
)
from commin import *

class Communication():
    def __init__(self,  AUTH_TOKEN=None):
        self.AUTH_TOKEN = AUTH_TOKEN
        self.headers = {
        "Authorization": f"Bearer {self.AUTH_TOKEN}",
        "Content-Type": "application/json",
    }
    
    def login_user(self, username, password):        
        response = requests.post(auth, json={"username": username, "password": password})
        if response.status_code == 200:
            tokens = response.json()
            save_token(ACCESSTOKEN, token=tokens.get("access"))
            save_token(REFRESHTOKEN,  token=tokens.get("refresh"))
            print('done"login"')
        else:
            print("Failed to get tokens:", response.json())
            return f"Failed to get tokens: {response.json()}"
    
    def post(self,endpoint, data):
        response = requests.post(endpoint, headers=self.headers, json=data)
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.text)
    def get(self, endpoint, params=None):
        response = requests.get(endpoint, headers=self.headers, params=params)
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.text)
    def put(self, endpoint, data):
        response = requests.post(endpoint, headers=self.headers, json=data)
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.text)
    def delete(self, endpoint):
        pass