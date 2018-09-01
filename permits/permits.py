import string
import random
import copy
import json
#import python_jsonschema_objects as pjs


#permits_needed = 75

model_permit = {"static":{"permit_id":"example","lot":"student lot"},"dynamic":{"AY":"2018-2019","assigned_name":"Jolene"}}



def bulk_create(total=75):
    batch = []
    for i in range(total):
        current = Permit(i)
        with open("/home/ghoulmann/parking_app/data/permits.json", 'a+') as permits:
            permits.write('\n\n')
            json.dump(current.__dict__, permits, encoding="utf-8", indent=4)
        batch.append(json.dumps(current.__dict__))
    return batch




    #for obj in gc.get_objects():
    #    if isinstance(obj, Permit):
    #        print(obj.__dict__)
    #return ids

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))




import time
from random import choice
from string import digits, ascii_lowercase

def bulk_permit_gen(count=75):
    create = count

    for i in range(count):
        chars = digits + ascii_lowercase
        strings = ["".join([choice(chars) for i in range(2)]) for j in range(count)]
    return strings
    for s in strings:
        id = Permit(s)
        id.permit_id = id




class Permit(object):
    def __init__(self, id):
        setattr(self, self.permit_id, id)
        self.permit_id = ''
        self.permit_student = str('')
        self.creation_date = str('')
        self.permit_issued = str('')
        self.issue_season = str('')
        self.created = time.strftime("%c")
