"""
| Module: controllers.py
| Location: app.home
| Purpose: provides controllers for processing data for home views.
"""

from flask import flash
import time
from datetime import datetime

# models is one folder up from home
from ..models import Testers
from ..extensions import db

def process_loop_controller(data):
    """Processes the data and launches test of user registration.
    data-> {'nbr_users': '3'}
    """
    successful = False
    nbr_users = 0
    if 'nbr_users' in data and data['nbr_users'] != '':
        nbr_users = int(data['nbr_users'])

    if nbr_users > 0:
        emails = []
        for reg in range(0, nbr_users): # 0 is 1st one, not 1
            # build strings
            suffix = datetime.now().microsecond
            firstname = 'De'
            lastname = 'Tester'
            username = 'tester' + str(suffix)
            password_str = 'Test' + str(suffix)
            email = username + '@example.com'
            # process the strings
            if process_one_controller(email,
                                      firstname,
                                      lastname,
                                      password_str):
                # save to db
                try:
                    newt = Testers(email,
                                         firstname,
                                         lastname,
                                         password_str)
                    db.session.add(newt)
                    db.session.commit()
                    successful = True
                except Exception as error:
                    print(str(error))
                    db.session.rollback()
            else:
                successful = False

    return successful

def process_one_controller(email, firstname, lastname, password):
    """Further processing here as required before persistance.
    """
    # Do something here

    return True
