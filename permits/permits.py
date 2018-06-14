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




class Permit():
    def __init__(self, id):
        setattr(self, self.permit_id, id)
        self.permit_id = ''
        self.permit_student = str('')
        self.creation_date = str('')
        self.permit_issued = str('')
        self.issue_season = str('')
        self.created = time.strftime("%c")
