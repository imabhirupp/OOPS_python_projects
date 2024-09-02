import requests
from datetime import datetime

pixel_endpoint = "https://pixe.la/v1/users"
TOKEN = "Your API KEY"
USERNAME = "Your Username"
GRAPH_ID = "Your graph_id"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixel_endpoint, json=params)
# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hr",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

## POST
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_add_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2",
}

## POST
# response = requests.post(url=pixel_add_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "1"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
