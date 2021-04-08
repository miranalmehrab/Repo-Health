import json

def get_csv_contents(filename):
    fp = open('data/'+filename, 'r')
    contents = fp.read()
    contents = contents.split('\n')
    
    contents.pop()
    return contents

def convert_str_to_dict(contents):
    dict_contents = []
    for content in contents:
        dict_contents.append(json.loads(content))

    return dict_contents
