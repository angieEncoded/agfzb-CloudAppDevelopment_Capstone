# My notes and any issues I ran into with the labs
- Ran into a problem with installing requirements needed to use this command
    - ```pip3 install -r requirements.txt --user```
- Ran into a problem installing django too
    - ```pip3 install django --user```
- Problem with installing pillow
    - Per the forums took out the versioning number in ./server/requirements.txt
- 03052023 Completed and tested all items in module 1. 
    - Took all requested screenshots
    - Everything for module 1 located in the module 1 folder
    - Git commit and push done
- 03062023
    - Completed the User Management half of the module
        - Created the superuser
        - Created the login, logout, and registration modules
        - pushed code changes up to github
    - Completed the CICD half of the module
        - Note that the banner to manually run the workflow never appeared for me
        - Could not find any threads in the forums or any information online about why except a vague possibility that something wasn't defaulted to the correct default branch name (this one is still legacy master)
        - The linter DID run correctly on push so I am considering this module complete
- 03092023
    - Completed the get-dealership nodeJS function, tested and working
        - endpoint url is https://us-south.functions.appdomain.cloud/api/v1/web/3940b2d5-8cd9-42a0-ba15-e0eea243f2d7/dealership-package/get-dealership
    - Completed the get-review Python function, tested and working
        - endpoint url is https://us-south.functions.cloud.ibm.com/api/v1/namespaces/3940b2d5-8cd9-42a0-ba15-e0eea243f2d7/actions/dealership-package/get-review
    - Completed the post-review Python function, tested and working (see example from Upkar for details on how the review body should look like for the post)
        - endpoint url is https://us-south.functions.cloud.ibm.com/api/v1/namespaces/3940b2d5-8cd9-42a0-ba15-e0eea243f2d7/actions/dealership-package/post_review
        - Params is as follows 
        ```js
        review = {
            "review": 
                {
                    "id": 1114,
                    "name": "Upkar Lidder",
                    "dealership": 15,
                    "review": "Great service!",
                    "purchase": False,
                    "another": "field",
                    "purchase_date": "02/16/2021",
                    "car_make": "Audi",
                    "car_model": "Car",
                    "car_year": 2021
                }
            }```
    - Completed the get-dealership-by-state NodeJS function, tested and working
        - endpoint is https://us-south.functions.cloud.ibm.com/api/v1/namespaces/3940b2d5-8cd9-42a0-ba15-e0eea243f2d7/actions/dealership-package/get-dealership-by-state
        - Params is ```STATE="STATE ABBREVIATION"```
    - Created the CarModel and CarMake models and ran the migrations
        - NOTE - in this project you have to specify the location ```python manage.py makemigrations djangoapp``` this is not the same as other projects unsure what is different in their skeleton
    - Created the root\root superuser for the peer review. Took the screen shots requested of carmake and the carmakelist
    - Committed all changes to github
    - LEFT OFF ON CREATE DJANGO PROXY SERVICES OF CLOUD FUNCTIONS
- 03122023
    - Created the views, models, and urls for getting dealerships, getting reviews, and posting reviews
    - Complted Module 3
    - MODULE 4
        - FINALLY got bootstrap 5, jquery, and bootstrap table playing nicely together. Finished up the drop down and took dealerships.png and dealerships_filter.png for peer review
- 03182023
    - Module 4 continued
    - completed the POST request for dealer reviews. I was trying to use the POST api and it wasn't accepting my token. I guess for this one we were supposed to just use the ANY link. So it's working fine with that.
    - Took screenshots
    - Moved all the api keys into environment vars
    - moved on
- 03192023
    - DEcided to go ahead and factor out the api keys into django-environ - make sure that the requirements.txt has been updated
    - This project will require a .env file in the root of djangoapp with the following entries:
    ```s
        REVIEWS_URL=
        DEALERS_URL=
        API_KEY=
        REVIEWS_POST_URL=
        ALL_DEALERSHIPS_URL=
        DEALER_BY_ID_URL=
        REVIEW_SENTIMENTS_URL=
    ```
    - 


# Final Project Template

The final project for this course has several steps that you must complete. 
To give you an overview of the whole project, all the high-level steps are listed below. 
The project is then divided into several smaller labs that give the detailed instructions for each step. 
You must complete all the labs to successfully complete the project.

## Project Breakdown

**Prework: Sign up for IBM Cloud account and create a Watson Natural language Understanding service**
1. Create an IBM cloud account if you don't have one already.
2. Create an instance of the Natural Language Understanding (NLU) service.

**Fork the project Github repository with a project then build and deploy the template project**
1. Fork the repository in your account
2. Clone the repository in the theia lab environment
3. Create static pages to finish the user stories
4. Deploy the application on IBM Cloud

**Add user management to the application**
1. Implement user management using the Django user authentication system.
2. Set up continuous integration and delivery

**Implement backend services**
1. Create cloud functions to manage dealers and reviews
2. Create Django models and views to manage car model and car make
3. Create Django proxy services and views to integrate dealers, reviews, and cars together
 
**Add dynamic pages with Django templates**
1. Create a page that shows all the dealers
2. Create a page that show reviews for a selected dealer
3. Create a page that let's the end user add a review for a selected dealer

**Containerize your application**
1. Add deployment artifacts to your application
2. Deploy your application
