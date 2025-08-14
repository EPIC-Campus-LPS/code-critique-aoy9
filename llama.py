import requests
codeprob = input("code problem? ")
# URL of the Ollama API (default is localhost)
url = "http://localhost:11434/api/generate"

# JSON payload with model and prompt
payload = {
    "model": "llama3",
    "prompt": "Can you help me fix the issues in the following code"+codeprob,
    "stream": True
}

# Make the POST request, print the response as it is streamed
with requests.post(url, json=payload, stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode('utf-8'))
