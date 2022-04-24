import json
import csv
import pandas as pd

def dump_file():
    dict_inf = [
        {'id': '111111', 'name': 'Sam', 'age': '20'},
        {'id': '222222', 'name': 'Andrew', 'age': '22'},
        {'id': '333333', 'name': 'Jack', 'age': '24'},
        {'id': '444444', 'name': 'Daniel', 'age': '21'},
        {'id': '555555', 'name': 'Donald', 'age': '35'},
        {'id': '666666', 'name': 'Kris', 'age': '23'},
    ]
    filename = 'dict.json'
    with open(filename, 'w') as file_object:
        json.dump(dict_inf, file_object)

def load_open_create_csv():
    with open('D:\My Tanks\dict.json') as json_file:
        jsondata = json.load(json_file)

    data_file = open('D:\My Tanks\data_file.csv', 'w', newline='')
    csv_writer = csv.writer(data_file)

    count = 0
    for data in jsondata:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())

    data_file.close()

def add_phone():
    phone = open('input.csv', 'r')
    csv_phone = phone.readlines()
    phone.close()
    csv_input = pd.read_csv('data_file.csv')
    csv_input['phone'] = csv_phone
    csv_input.to_csv('data_file.csv', index=False)