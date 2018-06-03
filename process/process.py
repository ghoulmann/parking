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
