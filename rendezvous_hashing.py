import json
import requests
from csv_parser import csv_parser
import operator

if __name__ == '__main__':
    
    count = 0
    hash_key,hash_value = csv_parser()
    hrw_hash = {}

    servers = ['http://localhost:5000','http://localhost:5001','http://localhost:5002','http://localhost:5003']
    url = "/api/v1/entries"

    print('Uploading the data...')
    while count < len(hash_value):
        for serv in servers:
            hrw_string = hash(serv+str(hash_key[count]))
            hrw_hash[serv] = hrw_string

        max_server = max(hrw_hash.items(), key=operator.itemgetter(1))[0]
        data = {hash_key[count]: hash_value[count]
                    }

        response = requests.post( max_server+url, json=data)
        count=count+1

    print('Uploaded all {} entries'.format(count))
    print('Verifying the data.')


    for server_counter in servers:
        server_get = requests.get(server_counter+url)
        server_get_text = server_get.text
        print('GET {}\n{}'.format(server_counter, server_get_text))