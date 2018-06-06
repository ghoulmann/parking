# lot/lot.py



class Lot():

    def __init__(self):
        self.CAPACITY = 75


    def lot_details(self, used, *season, **ay):
        self.capacity = CAPACITY
        self.remaining = CAPACITY - used
        self.lot = {'capacity': capacity, 'assignments': assigned,'available_spots': remaining}
        return lot

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

        return plot(fig, include_plotlyjs=True, output_type='div')
