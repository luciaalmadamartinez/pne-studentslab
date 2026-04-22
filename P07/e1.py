import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print("Server:", SERVER)
print("URL:", URL)

conn = http.client.HTTPConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)

response = conn.getresponse()
data = json.loads(response.read().decode())

if data['ping'] == 1:
    print("ALIVE!")
else:
    print("ERROR")


