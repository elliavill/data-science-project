#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Aurelia Villyani
"""

from dash import html
import dash

dash.register_page(__name__, path="/404")

layout = html.H1("Custom 404")