import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve the API key from the .env file
API_KEY = os.getenv("NVIDIA_API_KEY")

# Define your headers with the API key
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# Define the API endpoint and payload
url = "https://integrate.api.nvidia.com/v1/models/meta/llama3-70b-instruct/generate"
payload = {
    "messages": [{"role": "user", "content": "Write a limerick about the wonders of GPU computing."}],
    "temperature": 0.5,
    "top_p": 1,
    "max_tokens": 1024,
}

# Send the POST request
response = requests.post(url, headers=headers, json=payload)

# Check the response status and print the result
if response.status_code == 200:
    data = response.json()
    for chunk in data.get('choices', []):
        content = chunk.get('delta', {}).get('content')
        if content:
            print(content, end="")
else:
    print(f"Error: {response.status_code} - {response.text}")
