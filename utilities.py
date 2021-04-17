import csv
import json


def get_csv_contents(filename):
    fp = open(filename, 'r')
    contents = fp.read()
    contents = contents.split('\n')
    
    contents.pop()
    return contents

def convert_str_to_dict(contents):
    dict_contents = []
    for content in contents:
        dict_contents.append(json.loads(content))

    return dict_contents


def write_data_to_csv_file(filepath, contents):

    with open(filepath, mode='w+') as fp:
        csv_writer = csv.writer(fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for content in contents:
            csv_writer.writerow(content)
        