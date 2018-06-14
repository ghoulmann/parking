# lot/lot.py

import json

global DATA_PATH
DATA_PATH = '/home/ghoulmann/parking_app/data/lot.json'
class Lot():

    def __init__(self):

        with open(DATA_PATH, 'r') as data:
            self.stored_data = json.load(data)
        self.name = self.stored_data['name']
        self.capacity = self.stored_data['details']['capacity']
        self.description = self.stored_data['details']['description']
        self.assigned = self.stored_data['details']['assigned']
        self.available = self.capacity - self.assigned

    def write_data(self):
        self.write_info = {'name': self.name, 'details': {'capacity': self.capacity, 'description': self.description, 'available': self.available, 'assigned': self.assigned}}
        with open(DATA_PATH, 'w') as data:
            json.dump(self.write_info, data, indent=4)

        #with open(file, 'r') as data:
        #    stored_data = data.read()
        #    stored_data = json.load(stored_data)
        #return stored_data
    '''
    def lot_details(self, used, *season, **ay):
        self.capacity = CAPACITY
        self.remaining = CAPACITY - used
        self.lot = {'capacity': capacity, 'assignments': assigned,'available_spots': remaining }
        return lot
    '''
    def donut(self, data, markers, title):
        """returns div"""
        import plotly
        import plotly.graph_objs as go
        from plotly.offline import plot

        self.fig = {
            'data': [
            {'values': data,
             'labels': markers, 'hole': .4,
                'hoverinfo': "label+percent+name",
                'type': 'pie'
                }],
            'layout': {
                "title":title
                }
            }

        return plot(self.fig, include_plotlyjs=True, output_type='div', show_link=False)
