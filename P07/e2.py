import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/lookup/symbol/human/'
PARAMS = '?content-type=application/json'

genes = ['FRAT1', 'ADA', 'FXN', 'RNU6-269P', 'MIR633', 'TTTY4C', 'RBMY2YP', 'FGFR3', 'KDR', 'ANK2']
genes_dictionary = {}

for gene in genes:
    new_endpoint = ENDPOINT + gene
    URL = SERVER + new_endpoint + PARAMS

    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", new_endpoint + PARAMS)

    response = conn.getresponse()
    data = json.loads(response.read().decode())

    if "id" in data:
        genes_dictionary[gene] = data["id"]

print(genes_dictionary)

