import requests

for i in range(5):
    info = requests.get('https://catfact.ninja/fact')
    fact = info.json()
    print(f' # {i+1}', fact['fact'])