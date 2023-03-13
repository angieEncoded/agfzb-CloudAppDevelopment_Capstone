# Installation process problems
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
    - LEFT OFF ON DEALER DETAILS AND REVIEWS PAGE

