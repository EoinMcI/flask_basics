"""
| Module: views.py
| Location: app.home
| Purpose: contains route endpoints for home.
e.g. url http://localhost/
"""
from flask import (render_template,
                   redirect,
                   url_for,
                   request,
                   flash)
# Locals
from . import home
from .forms import ProcessTestUsersForm
from .controllers import process_loop_controller

@home.route('/')
def index():
    """Routes the endpoint / to an actual html file."""
    return render_template('index.html', title='Eoin Code Homepage')

@home.route('/endpoint1/')
def endpoint1():
    """Connects the endpoint or url target to a function that provides
    the route to the actual html page to be returned to the user.
    """
    return "You have clicked EPOne and displayed this message. Very useful as a placeholder when creating the routes. Replace it with an actual html page."

@home.route('/endpoint2/')
def endpoint2():
    """Connects the endpoint or url target to a function that provides
    the route to the actual html page to be returned to the user.
    """
    return render_template('endpoint_2.html') # app/home/templates/

@home.route('/endpoint3/', methods=['GET', 'POST'])
def endpoint3():
    """Connects the endpoint or url target to a function that provides
    the route to the actual html page to be returned to the user.
    It is normally accessed using either a POST or GET from the html
    page.
    """

    if request.method == 'POST':
        # grab the form data and print it
        data = request.form.to_dict()
        args = request.args.to_dict()
        print('data->', data)
        print('args->', args)

        # Do some processing with the form data
        if process_loop_controller(data):
            msg = 'We are go.'
        else:
            msg = 'We are going nowhere fast.'
        flash(msg)
        # send user back to the index page when finished everything
        return redirect(url_for('home.index'))

    else: # assumed to be GET
        # add a form to the html
        form = ProcessTestUsersForm()
        # send enpoint_3.html to the user
        return render_template('endpoint_3.html',  # app/home/templates/
                                form=form,
                                action='start')
