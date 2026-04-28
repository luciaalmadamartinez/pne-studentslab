import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/lookup/symbol/human/'
PARAMS = '?content-type=application/json'

print("Server:", SERVER)

final_info = ENDPOINT + 'MIR633' + PARAMS

conn = http.client.HTTPConnection(SERVER)
conn.request("GET", final_info)
response = conn.getresponse()
data = json.loads(response.read().decode())

if "id" in data:
    number_id = data["id"]

    ENDPOINT_2 = '/sequence/id/'
    final_info_2 = ENDPOINT_2 + number_id + PARAMS
    final_URL = SERVER + final_info_2
    print("URL:", final_URL)

    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", final_info_2)
    response = conn.getresponse()
    data = json.loads(response.read().decode())

    print("Gene: MIR633")
    if "desc" in data:
        print("Description:", data["desc"])

    if "seq" in data:
        print("Bases:", data["seq"])







