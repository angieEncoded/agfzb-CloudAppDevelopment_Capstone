from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30, default='Subaru')
    description = models.CharField(max_length=1000, null=True, default="A Japanese Manufacturer")

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):

    SEDAN = "Sedan"
    WAGON = "Wagon"
    SUV = "SUV"
    VAN = "Van"
    TYPE = [
        (SEDAN, "Sedan"),
        (WAGON, "Wagon"),
        (SUV, "SUV"),
        (VAN, "Van")
    ]


    id = models.AutoField(primary_key=True)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='Forester')
    dealerId = models.IntegerField(default=15)
    type = models.CharField(max_length=20, choices=TYPE, default=SEDAN)
    year = models.IntegerField(default=2023)
    description = models.CharField(max_length=1000, null=True, default="An epic car")

    def __str__(self):
        return "Name: " + self.name + "Description" + self.description



# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
