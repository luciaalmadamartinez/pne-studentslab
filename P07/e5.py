from Seq1 import Seq
import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/lookup/symbol/human/'
PARAMS = '?content-type=application/json'

print("Server:", SERVER)

genes = ['FRAT1', 'ADA', 'FXN', 'RNU6-269P', 'MIR633', 'TTTY4C', 'RBMY2YP', 'FGFR3', 'KDR', 'ANK2']
for gene in genes:
    final_info = ENDPOINT + gene + PARAMS

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

        print("Gene:", gene)
        if "desc" in data:
            print("Description:", data["desc"])

        s = data["seq"]
        sequence = Seq(s)

        print(f"Total length: {sequence.len()}")
        print(sequence.count())
        count_dict = sequence.count()
        print(f"Most frequent base: {sequence.most_bases(count_dict)}")







