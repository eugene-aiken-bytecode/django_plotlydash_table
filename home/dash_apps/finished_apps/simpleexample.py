import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_table
from django_plotly_dash import DjangoDash
from home.dash_apps.finished_apps.looker_api import get_json
import pandas as pd
from home.models import Post

# query = Post.objects.values_list('post', flat=True)
# slug = str(query[3])
# print(slug)
# slug1 = get_json(slug)
#
# df = pd.read_json(slug1)
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)
#
# app.layout = html.Div(
#     [
#         dash_table.DataTable(
#             id="table",
#             columns=[{"name": i, "id": i} for i in df.columns],
#             data=df.to_dict("records"),
#             style_cell=dict(textAlign="left"),
#             style_header=dict(backgroundColor="paleturquoise"),
#             style_data=dict(backgroundColor="lavender"),
#         )
#     ]
#     )


# app.layout = html.Div([
#     html.H1('Square Root Slider Graph'),
#     dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
#     dcc.Slider(
#         id='slider-updatemode',
#         marks={i: '{}'.format(i) for i in range(20)},
#         max=20,
#         value=2,
#         step=1,
#         updatemode='drag',
#     ),
# ])


# @app.callback(
#                Output('slider-graph', 'figure'),
#               [Input('slider-updatemode', 'value')])
# def display_value(value):
#
#
#     x = []
#     for i in range(value):
#         x.append(i)
#
#     y = []
#     for i in range(value):
#         y.append(i*i)
#
#     graph = go.Scatter(
#         x=x,
#         y=y,
#         name='Manipulate Graph'
#     )
#     layout = go.Layout(
#         paper_bgcolor='#27293d',
#         plot_bgcolor='rgba(0,0,0,0)',
#         xaxis=dict(range=[min(x), max(x)]),
#         yaxis=dict(range=[min(y), max(y)]),
#         font=dict(color='white'),
#
#     )
#     return {'data': [graph], 'layout': layout}