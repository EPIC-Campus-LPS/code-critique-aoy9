import requests
import sys

pyfile = sys.argv[1]
codeprob = open(f"/home/ericy/{pyfile}")
codeproblem = codeprob.read()
# URL of the Ollama API (default is localhost)
url = "http://localhost:11434/api/generate"

# JSON payload with model and prompt
payload = {
    "model": "llama3",
    "prompt": "Can you help me fix the issues in the following code"+codeproblem,
    "stream": False
}


# Make the POST request
response = requests.post(url, json=payload)

# Parse and print the response
if response.status_code == 200:
    data = response.json()
    print(data['response'])
else:
    print("Error:", response.text)