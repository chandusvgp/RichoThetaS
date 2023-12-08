#Begin Phyton Code
import requests
from requests.auth import HTTPDigestAuth
import cv2
import numpy as np
import time
#url = 192.168.1.1/osc/info
#[clientVersion](../theta-web-api-v2.0/options/client_version.md)
url = "http://192.168.1.1/osc/commands/execute"

#{
#    "name": "camera.startSession",
#    "parameters": {}
#}
payload = {
    "name": "camera.startSession",
    "parameters": {}
}

response = requests.post(url, json=payload)

print(response.status_code)
x= response.json()
sessionId = x['results']['sessionId']

# url = "http://192.168.1.1/osc/info"
# response = requests.post(url, json=payload)

# print(response.status_code)
# print(response.json())

# url = "http://192.168.1.1/osc/commands/execute"
payload = {
    "name": "camera.setOptions",
    "parameters": {
        #"sessionId": "SID_0009",
        "sessionId": sessionId,
        "options": {
            "clientVersion": 2
           #"clientVersion": "../theta-web-api-v2.0/options/client_version.md"
        }
    }
}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())

#getting file formates
payload={
    "name": "camera.getOptions",
    "parameters": {
        "optionNames": [
            "fileFormat",
            "fileFormatSupport"
        ]
    }
}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())

#setting file formate
payload={
    "name": "camera.setOptions",
    "parameters": {
        "options": {
            "fileFormat": {
                "type": "jpeg",
                "width": 2048,                
                "height": 1024
                #"width": 5376",
               # "height": 2688
            }
        }
    }
}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())

#capture image
payload={
    "name": "camera.takePicture"
}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
time.sleep(5)
#check for image
url1 = "http://192.168.1.1/osc/checkForUpdates"
payload={
    "stateFingerprint": "FIG_0005"
}

response = requests.post(url1,json=payload)
print(response.status_code)
print(response.json())

#request for image saving
url = "http://192.168.1.1/osc/state"

try:
    response = requests.post(url)
    response.raise_for_status()  # This will raise an HTTPError for bad responses
    print(response.status_code)
    print(response.json())
    Y=response.json()
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.RequestException as err:
    print(f"Request Error: {err}")
#saving image
url3 = Y['state']['_latestFileUrl']
img=url3.split('/')
response = requests.get(url3)
print(response.status_code)
#print(response.json())
#cv2.imwrite()
with open(img[6], "wb") as file:
    file.write(response.content)

def reset_camera(camera_ip):
    url = f"http://{camera_ip}/osc/commands/execute"
    
    # Define the reset command
    reset_command = {
        "name": "camera.reset",
        "parameters": {}
    }

    try:
        # Send the reset command to the camera
        response = requests.post(url, json=reset_command)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Print the response status code and content
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.json())

    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    # Replace 'your-camera-ip' with the actual IP address or hostname of your camera
    camera_ip_address = "192.168.1.1"

    # Call the reset_camera function
    reset_camera(camera_ip_address)

