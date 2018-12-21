import json
import requests
from csv_parser import csv_parser

if __name__ == '__main__':
    
    count = 0
    hash_key,hash_value = csv_parser()
    #hash_key = []

    url = "http://127.0.0.1:5000/api/v1/entries"

    while count < len(hash_value):

        data = {   hash_key[count]:hash_value[count]
                }

        print ("Posting %s" % data)

        response = requests.post( url, json=data)
        count += 1                        
        print (response)
    
    #server_get = requests.get(url)
    #print(server_get.text)
    


    #curl http://localhost:5000/api/v1/entries -d "hash_key=1234&hash_value=Devashish" -X POST -v