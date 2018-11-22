from app.panels.__common__ import *

layout = html.Div([
    html.Div(style={'textAlign': 'center'},children = 'bonjour'),
    html.Img(src='PNG_transparency_demonstration_1.png'),
    html.Img(src=app.get_asset_url('téléchargement.jpg'))
    ])
"""
import dash
import dash_html_components as html
import base64

image_filename = 'PNG_transparency_demonstration_1.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

layout = html.Div([
    html.Img(src='data:image/png;base64,{}'.format(encoded_image))
    ])
"""
