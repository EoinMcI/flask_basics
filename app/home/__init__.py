"""
| Module: __init__.py
| Location: app.home
| Purpose: configuration for home blueprint registered in factory
"""
from flask import Blueprint

home = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static'
)

# Must be here
from . import views
