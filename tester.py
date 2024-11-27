import requests
BASE_URL = "http://127.0.0.1:8000/api"  
AUTH_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyNjgzMzczLCJpYXQiOjE3MzI2ODMwNzMsImp0aSI6IjFjYjAwYWQxYTk4YjQxMDdiY2ZkNGZmYzM1MmFjMjU1IiwidXNlcl9pZCI6MTB9.IMvxbKbRegoWnin8xQ5rjz-vPfOvEGXR1qpx1Axmf1A'
def tester_request(method, endpoint, data=None, params=None):
    """
    A generic function to test API requests with authentication.

    :param method: HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE').
    :param endpoint: API endpoint (relative to BASE_URL).
    :param data: Data to send in the request body (for POST/PUT).
    :param params: Query parameters for the request.
    :return: Response object.
    """
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json",
    }

    url = f"{BASE_URL}{endpoint}"

    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=data)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, json=data)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError("Invalid HTTP method")

        # Print response for debugging
        print(f"Request to {url} completed with status code {response.status_code}")
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.text)

        return response

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# response = requests.post(f"{BASE_URL}/token/", json={"username": "rayyan", "password": "idkidkidk"})
# if response.status_code == 200:
#     tokens = response.json()
#     print("Access Token:", tokens.get("access"))
#     print("Refresh Token:", tokens.get("refresh"))
# else:
#     print("Failed to get tokens:", response.json())

# response = tester_request("GET", "/meeps/")
# data = {
#     "body": "This is a test meep created via API."
# }
# response = tester_request("POST", "/meeps/", data=data)
# meep_id = 10
# response = tester_request("GET", f"/meeps/{meep_id}/")
meep_id = 11
response = tester_request("POST", f"/meeps/{meep_id}/like/")
# profile_id = 10
# response = tester_request("POST", f"/profile/follow/{profile_id}/")
# search_query = {"search": "test"}
# response = tester_request("POST", "/meeps/search/", data=search_query)
