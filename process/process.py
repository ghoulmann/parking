import json

def read_output(output):
    with open(output) as file:
        records = file.read()
    records = records.split('\n\n')
    js = []
    for r in records:
        try:
            js.append(json.loads(r))
        except:
            Exception
            pass


    return js

def json_dict_list(data):

    with open(data, 'r') as data:
        strings = data.read()

    list = strings.split('\n\n')
    json_data = []
    for i in list:
        i = i.strip()
    
        #i = json.loads(i)[0]
        json_data.append(json.loads(i))
    from operator import itemgetter
    sorted_applications = sorted(json_data, key=itemgetter('scaled_score'), reverse=True)
    return sorted_applications
