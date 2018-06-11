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
            if key == 'job':
                class_instance.qualifier['weekday_job'] = 1
            if key == 'parent_letter':
                class_instance.parent_letter = 1
            if key == 'insurance':
                class_instance.insurance = 1
            if key == 'license':
                class_instance.license = 1
            if key == 'registration':
                class_instance.registration = 1

        class_instance.full_name = form_results['full_name']
        class_instance.student_id = form_results['student_id']
        class_instance.email = form_results['email']
        class_instance.license_plate = form_results['l_plate']
        class_instance.state = form_results['state']
        #class_instance.grade = form_results['grade']
        class_instance.make = form_results['make']
        class_instance.model = form_results['model']
        class_instance.year = form_results['year']
        class_instance.narrative = form_results['narrative']


        #    pass
        #setattr(class_instance, key, value)

class Application(str):
    def __init__(self, str):
        self.instances = []
        #self.grade = False
        self.qualifier = {}
        #self.id = self.id_generator(self)
        self.id = ""
        self.name = self.id.title()
        self.full_name = ""
        self.qualifier['hardship'] = bool()
        self.qualifier['internship'] = bool()
        self.qualifier['d_enrollment'] = bool()
        self.qualifier['weekday_job'] = bool()
        self.qualifier['distance'] = bool()
        self.qualifier['athletics'] = bool()
        self.qualifier['athletics_carpool'] = bool()
        self.qualifier['athletics_captain'] = bool()
        self.qualifier['sga'] = bool()
        self.qualifier['extracurricular'] = bool()
        self.qualifier['gpa'] = bool()
        self.qualifier['attendance'] = bool()
        self.qualifier['service'] = bool()
        self.insurance = bool()
        self.license = bool()
        self.registration = bool()
        self.parent_letter = bool()
        self.license_plate = ""
        self.plate_state = ""
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""
        self.email = ""
        self.narrative = ''

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
