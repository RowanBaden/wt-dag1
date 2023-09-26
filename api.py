print("Start api read application")

Import requests

paginaresults = requests.get('https://catfact.ninja/facts')
print (paginaresults)

feitjes = paginaresults.json()
print(feitjes["current page"])
print(feitjes["data"][0]["fact"])