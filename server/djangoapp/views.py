from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
# from .models import related models
from .models import CarDealer, CarModel, CarMake
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
    if request.method == "GET":
        context = {}
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/3940b2d5-8cd9-42a0-ba15-e0eea243f2d7/dealership-package/get-dealership"
        dealerships = get_dealers_from_cf(url)
        context["dealership_list"] = dealerships
        # return HttpResponse(context["dealership_list"])
        return render(request, 'djangoapp/index.html', context)

# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
def get_dealer_details(request, id):
    if request.method == "GET":
        context = {}
        reviews_url = "https://us-south.functions.appdomain.cloud/api/v1/web/3940b2d5-8cd9-42a0-ba15-e0eea243f2d7/dealership-package/get-review"
        dealers_url = "https://us-south.functions.appdomain.cloud/api/v1/web/3940b2d5-8cd9-42a0-ba15-e0eea243f2d7/dealership-package/get-dealership-by-id"
        #Get the reviews
        review_results = get_dealer_reviews_from_cf(reviews_url, dealer_id=id, api_key="gajduij-_tA5a1xUfyOKbq799ewR89vvWDRxB1hvqP03")
        # get the details about the dealer itself
        dealer_result = get_dealer_by_id_from_cf(dealers_url, dealer_id=id, api_key="gajduij-_tA5a1xUfyOKbq799ewR89vvWDRxB1hvqP03")

        context['dealer'] = dealer_result
        context['reviews'] = review_results
        return render(request, 'djangoapp/dealer_details.html', context)

# Create a `add_review` view to submit a reviews
# def add_review(request, dealer_id):
# ...
@login_required
def add_review(request, id):

    # Prep and render the page we will need to post a review
    if request.method == 'GET':
        context = {}
        dealer_url = "https://us-south.functions.appdomain.cloud/api/v1/web/3940b2d5-8cd9-42a0-ba15-e0eea243f2d7/dealership-package/get-dealership-by-id"
        dealer = get_dealer_by_id_from_cf(dealer_url, dealer_id=id)
        context["dealer"] = dealer

        # Get cars for the dealer
        cars = CarModel.objects.all()
        print(cars)
        context["cars"] = cars
        return render(request, 'djangoapp/add_review.html', context)
    
    elif request.method == 'POST':
        if request.user.is_authenticated:
            username = request.user.username
            console.log(request.POST)
            payload = dict()
            car_id = request.POST["car"]
            car = CarModel.objects.get(pk=car_id)
            payload["time"] = datetime.utcnow().isoformat()
            payload["name"] = username
            payload["dealership"] = id
            payload["id"] = id
            payload["review"] = request.POST["content"]
            payload["purchase"] = False
            if "purchasecheck" in request.POST:
                if request.POST["purchasecheck"] == 'on':
                    payload["purchase"] = True
            payload["purchase_date"] = request.POST["purchasedate"]
            payload["car_make"] = car.CarMake.name
            payload["car_model"] = car.name
            payload["car_year"] = int(car.car_year.strftime("%Y"))

            new_payload = {}
            new_payload["review"] = payload
            review_post_url = "https://us-south.functions.cloud.ibm.com/api/v1/namespaces/3940b2d5-8cd9-42a0-ba15-e0eea243f2d7/actions/dealership-package/post_review"
            post_request(review_post_url, new_payload, id=id)
        return redirect("djangoapp:dealer_details", id=id)





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