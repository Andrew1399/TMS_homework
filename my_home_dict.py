import json
import csv
import pandas as pd
import random

def dump_file():
    data = {}
    for el in range(6):
        random_id  =''.join([str(random.randint(1, 9)) for _ in range(6)])
def load_open_create_csv():
    with open('D:\My Tanks\dict.json') as json_file:
        jsondata = json.load(json_file)

    for key, items in json_file.

def add_phone():
    phone = open('input.csv', 'r')
    csv_phone = phone.readlines()
    phone.close()
    csv_input = pd.read_csv('data_file.csv')
    csv_input['phone'] = csv_phone
    csv_input.to_csv('data_file.csv', index=False)