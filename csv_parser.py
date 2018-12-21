import csv
import sys

file_name = sys.argv[1]

hash_value = []
hash_key = []

def csv_parser():
    with open(file_name, newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        #next(csvfile)
        for row in spamreader:
            hash_value.append('{}, {}, {}, {}, {}, {}'.format(row['Year'],row['113 Cause Name'],row['Cause Name'],row ['State'],row['Deaths'],row['Age-adjusted Death Rate']))
            hash_key.append(hash('{}:{}:{}'.format(row['Year'],row['Cause Name'],row ['State'])))
            #print('{} :{}'.format(hash_key, hash_value))
        return hash_key, hash_value
           # print(', '.join(row))
if __name__ == '__main__':
    csv_parser()