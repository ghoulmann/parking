import string
import random

#def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#    return ''.join(random.choice(chars) for _ in range(size))

from random import randint

def process_form_results(form_results, class_instance):

    for key, value in form_results.iteritems():

        if value == 'y':

            if key == 'internship':
                class_instance.qualifier['internship'] = 1
            if key == 'distance':
                class_instance.qualifier['distance'] = 1
            if key == 'attendance':
                class_instance.qualifier['attendance'] = 1
            if key == 'service':
                class_instance.qualifier['service'] = 1
            if key == 'athletics_carpool':
                class_instance.qualifier['athletics_carpool'] = 1
            if key == 'gpa':
                class_instance.qualifier['gpa'] = 1
            if key == 'd_enrollment':
                class_instance.qualifier['d_enrollment'] = 1
            if key == 'extracurricular':
                class_instance.qualifier['extracurricular'] = 1
            if key == 'weekday_job':
                class_instance.qualifier['weekday_job'] = 1
            if key == 'athletics':
                class_instance.qualifier['athletics'] = 1
            if key == 'athletics_captain':
                class_instance.qualifier['athletics_captain'] = 1
            if key == 'distance':
                class_instance.qualifier['distance'] = 1
            if key == 'sga':
                class_instance.qualifier['sga'] = 1
            if key == 'service':
                class_instance.qualifier['service'] = 1
            if key == 'media':
                class_instance.qualifier['media'] = 1
        #    pass
        #setattr(class_instance, key, value)

class Application(str):
    def __init__(self, str):
        self.instances = []
        self.grade = randint(9, 12)
        #self.id = self.id_generator(self)
        self.id = str.capitalize()
        self.name = self.id
        self.qualifier = {}
        self.qualifier['hardship'] = int(0)
        self.qualifier['internship'] = int(0)
        self.qualifier['d_enrollment'] = int(0)
        self.qualifier['weekday_job'] = int(0)
        self.qualifier['distance'] = int(0)
        self.qualifier['athletics'] = int(0)
        self.qualifier['athletics_carpool'] = int(0)
        self.qualifier['athletics_captain'] = int(0)
        self.qualifier['sga'] = int(0)
        self.qualifier['extracurricular'] = int(0)
        self.qualifier['gpa'] = int(0)
        self.qualifier['attendance'] = int(0)
        self.qualifier['service'] = int(0)
        self.insurance = bool()
        self.licence_plate = randint(666, 777)
        self.plate_state = 'Maryland'
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""
        self.license = True
        self.registration = True
        self.parent_letter = True

        #if (sum(self.qualifier.values()) * 2) > 0:
        #    self.raw_score = (sum(self.qualifier.values()))

        #if self.raw_score:
        #    self.scaled_score = self.expo_bloom(self.qualifier.items(), self.raw_score)
        self.instances.append(self)

    def multiply(self, dictionary):
        if (sum(dictionary.values()) * 2) > 0:
            score = (sum(dictionary.values()) *2)
            self.raw_score = score

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
        #self.determiner = determiner
        return self.scaled_score

    #def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
    #     return ''.join(random.choice(chars) for _ in range(size))
