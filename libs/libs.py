import requests

resp = requests.get('https://api.github.com/users/Gingertonic')
data = resp.json()

breakpoint() # shortcut for import pdb; pdb.set_trace()

print(data.location)