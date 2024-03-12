import requests
import json
import time

with open('quoteList.txt', 'a') as file:
    for i in range(10):
        responses = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(responses.text)
        quote = f"\'{json_data[0]['q']}\' - {json_data[0]['a']}\n"
        if quote != "Too many requests. Obtain an auth key for unlimited access. - zenquotes.io":
            file.write(quote)
            time.sleep(1)

with open('quoteList.txt', 'r') as file:  
    for count, line in enumerate(file):
        pass
print(f'Total Lines: {count}')