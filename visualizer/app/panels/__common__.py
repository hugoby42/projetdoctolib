import dash
import dash_core_components as dcc
import dash_html_components as html
import math as m
import pandas as pd
import flask as fl
import plotly.plotly as py
import app.panels.auth
from datetime import datetime as dt
from plotly import graph_objs as go
from dash.dependencies import Input, Output, State
import db

# Code permettant de formatter le style des trois KPIs
def indicator(color, text, value):
    return html.Div(
        [

            html.P(
                text,
                className="twelve columns indicator_text"
            ),
            html.P(
                value,
                className="indicator_value"
            ),
        ],
        className="four columns indicator")
