import string
import random

#def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#    return ''.join(random.choice(chars) for _ in range(size))

from random import randint

def process_form_results(form_results, class_instance):
    print(form_results.items)

    for key, value in form_results.iteritems():
        setattr(class_instance, key, value)

class Application(str):
    def __init__(self, str):
        self.instances = []
        self.grade = randint(9, 12)
        #self.id = self.id_generator(self)
        self.id = str.capitalize()
        self.name = self.id
        self.qualifier = {}
        self.qualifier['hardship'] = randint(0,1)
        self.qualifier['internship'] = randint(0,1)
        self.qualifier['d_enrollment'] = randint(0,1)
        self.qualifier['weekday_job'] = randint(0,1)
        self.qualifier['distance'] = randint(0,1)
        self.qualifier['athletics'] = randint(0,1)
        self.qualifier['athletics_carpool'] = randint(0,1)
        self.qualifier['athletics_captain'] = randint(0,1)
        self.qualifier['sga'] = randint(0,1)
        self.qualifier['extracurricular'] = randint(0,1)
        self.qualifier['gpa'] = randint(0,1)
        self.qualifier['attendance'] = randint(0,1)
        self.qualifier['service'] = randint(0, 1)
        self.insurance = True
        self.licence_plate = randint(666, 777)
        self.plate_state = 'Maryland'
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""
        self.license = True
        self.registration = True
        self.parent_letter = True
        self.raw_score = (sum(self.qualifier.values())) * 2
        self.scaled_score = self.expo_bloom(self.qualifier, self.raw_score)
        self.instances.append(self)
    def expo_bloom(self, dictionary, multiplier):
        if dictionary['hardship']:
            self.scaled_score = multiplier ** 11
            self.determiner = 'hardship'
        elif dictionary['internship']:
            self.scaled_score = multiplier ** 10
            self.determiner = 'internship'
        elif dictionary['d_enrollment']:
            self.scaled_score = multiplier ** 9
            self.determiner = 'dual enrollment'
        elif dictionary['weekday_job']:
            self.determiner = 'weekday job'
            self.scaled_score = multiplier ** 8
        elif dictionary['athletics_carpool']:
            self.scaled_score = multiplier ** 7
            self.determiner = 'athletics carpool'
        elif dictionary['athletics_captain']:
            self.scaled_score = multiplier ** 6
            self.determiner = 'team captain'
        elif dictionary['athletics']:
            self.scaled_score = multiplier ** 5
            self.determiner = 'team athlete'
        elif dictionary['distance']:
            self.scaled_score = multiplier ** 4
            self.determiner = 'distance'
        elif dictionary['sga']:
            self.scaled_score = multiplier ** 3
            self.determiner = "student govenment"
        elif dictionary['extracurricular']:
            self.scaled_score = multiplier ** 2
            self.determiner = 'extracurricular activities'


        else:
	        self.scaled_score = multiplier

        return self.scaled_score

    #def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
    #     return ''.join(random.choice(chars) for _ in range(size))
