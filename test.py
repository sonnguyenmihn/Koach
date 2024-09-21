import requests

# URL of the API endpoint
url = 'http://0.0.0.0:8000/sign_language/translate/'

# JSON data to be sent in the POST request
data = {
    'text': 'Hello'
}

# Sending the POST request
response = requests.post(url, json=data)

# Print the response status code and JSON response
print(response.status_code)
print(response.json()['message'])
print(response.json()['translated_text'])