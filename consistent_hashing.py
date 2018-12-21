import json
import requests
from csv_parser import csv_parser



if __name__ == '__main__':
    
    count = 0
    hash_key,hash_value = csv_parser()
    hash_servers = []
    consistent_hash = []
    data = {}

    servers = ['http://localhost:5000','http://localhost:5001','http://localhost:5002','http://localhost:5003']
    url = "/api/v1/entries"
    for serv in servers:
        hash_servers.append(hash(serv))
    hash_servers.sort()

    print('Uploading the data...')
    while count < len(hash_value):
        data[count]={   
                    hash_key[count]: hash_value[count]
                    }
        if ((hash_key[count] < hash_servers[0])|(hash_key[count] > hash_servers[3])):
            response = requests.post( servers[0]+url, json=data[count])
        elif ((hash_key[count] > hash_servers[0]) & (hash_key[count] < hash_servers[1])):
            response = requests.post( servers[1]+url, json=data[count])
        elif ((hash_key[count] > hash_servers[1]) & (hash_key[count] < hash_servers[2])):
            response = requests.post( servers[2]+url, json=data[count])
        elif ((hash_key[count] > hash_servers[2]) & (hash_key[count] < hash_servers[3])):
            response = requests.post( servers[3]+url, json=data[count])
        count += 1  


    print('Uploaded all {} entries'.format(count))
    print('Verifying the data.')
    for server_counter in servers:
        server_get = requests.get(server_counter+url)
        server_get_text = server_get.text
        print('GET {}\n{}'.format(server_counter, server_get_text))