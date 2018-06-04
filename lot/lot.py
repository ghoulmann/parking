# lot/lot.py

import plotly

global CAPACITY
CAPACITY = 75


def lot_details(used, *season, **ay):
    capacity = CAPACITY
    remaining = CAPACITY - used
    lot = {'capacity': capacity, 'assignments': assigned,'available_spots': remaining}
    return lot

def donut(values, labels, *x, *y, title):
    """returns div"""
    import plotly.plotly as py
    import plotly.graph_objs as go

    fig = {
        'data': [
            'values': values,
            'labels': labels
            ],
            'hole': 0.4,
            'hoverinfo': "label+percent+name",
            'type': 'pie'
        'layout': {
            "title":title
        }
    }

    return = plotly.offline.plot(figure, include_plotlyjs=True, output_type='html')
