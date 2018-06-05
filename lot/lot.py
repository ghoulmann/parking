# lot/lot.py



class Lot():

    def __init__:
        CAPACITY = 75


    def lot_details(used, *season, **ay):
        capacity = CAPACITY
        remaining = CAPACITY - used
        lot = {'capacity': capacity, 'assignments': assigned,'available_spots': remaining}
        return lot

    def donut(data, markers, title):
        """returns div"""
        import plotly
        import plotly.graph_objs as go
        from plotly.offline import plot

        fig = {
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
