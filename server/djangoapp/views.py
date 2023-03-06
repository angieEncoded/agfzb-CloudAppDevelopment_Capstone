from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# from .models import related models
# from .models import CarDealer, CarModel, CarMake
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import re
from datetime import datetime
import logging
import json
from .restapis import *

# Get an instance of a logger
logger = logging.getLogger(__name__)


# some refactoring, and some utility things to make my life more comfortable
from .util import angie
console = angie.Console()

# Create a `contact` view to return a static contact page
def contact(request):
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', {'navcontact': True})

# Create an `about` view to return a static contact page
def about(request):
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', {'navabout': True})

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

# Create a `login_request` view to handle sign in request
def login_request(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Successfully logged you in!')
            return HttpResponseRedirect(reverse("djangoapp:index"))
        else:
            messages.add_message(request, messages.ERROR, 'Unable to log you in. Please try again.')
            return render(request, 'djangoapp/login.html', {'onLoginPage':True} )
    else:
        return render(request, 'djangoapp/login.html', {'onLoginPage':True} )


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Successfully logged you out, have a lovely day!')
    return HttpResponseRedirect(reverse("djangoapp:index"))

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html')
    
    if request.method == 'POST':
        # get the form's data
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        userExists = False

        # Check if the username exists
        try: 
            User.objects.get(username=username)
            userExists = True
        except Exception as error:
            logger.info(error)
            logger.debug("{} is new user".format(username))

        # Send user feedback that the username is taken
        if userExists:
            messages.add_message(request, messages.ERROR, 'That username is taken, please select a different username.')
            return render(request, 'djangoapp/registration.html', {'firstname': first_name, 'lastname': last_name})
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Succesfully signed you in!')
            return HttpResponseRedirect(reverse("djangoapp:index"))
       


