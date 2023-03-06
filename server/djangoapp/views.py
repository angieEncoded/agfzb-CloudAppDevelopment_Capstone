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