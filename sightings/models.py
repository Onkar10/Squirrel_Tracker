from django.db import models

class Sightings(models.Model):


    def __str__(self):
        return self.Unique_Squirrel_ID


    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = (
            (AM, 'AM'),
            (PM,'PM'),
            )
    
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    
    PRIMARY_FUR_COLOR = (
            (GRAY, 'Gray'),
            (CINNAMON, 'Cinnamon'),
            (BLACK, 'Black'),
           )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE = (
            (ADULT,'Adult'),
            (JUVENILE, 'Juvenile'),
            )
    
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION = (
            (GROUND_PLANE, 'Ground Plane'),
            (ABOVE_GROUND, 'Above Gound'),
            )


    x = models.FloatField(default = 0.0)
    y = models.FloatField(default = 0.0)
    Unique_Squirrel_ID = models.CharField(max_length=100)
    Shift = models.CharField(max_length=2,choices = SHIFT_CHOICES )
    Date = models.IntegerField(default = 0)
    Age = models.CharField(max_length=100, choices = AGE)
    Primary_Fur_Color = models.CharField(max_length=100, choices = PRIMARY_FUR_COLOR)
    Location = models.CharField(max_length=100, choices = LOCATION)
    Specific_Location = models.CharField(max_length=100)
    Running = models.BooleanField(default='False')
    Chasing = models.BooleanField(default='False')
    Climbing = models.BooleanField(default='False')
    Eating = models.BooleanField(default='False')
    Foraging = models.BooleanField(default='False')
    Other_Activities = models.CharField(max_length=100)
    Kuks = models.BooleanField(default='False')
    Quaas = models.BooleanField(default='False')
    Moans = models.BooleanField(default='False')
    Tail_flags = models.BooleanField(default='False')
    Tail_twitches = models.BooleanField(default='False')
    Approaches = models.BooleanField(default='False')
    Indifferent = models.BooleanField(default='False')
    Runs_from = models.BooleanField(default='False')








#Latitude
#Longitude
#Unique Squirrel ID
#Shift
#Date
#Age
#Primary Fur Color
#Location
#Specific Location
#Running
#Chasing
#Climbing
#Eating
#Foraging
#Other Activities
#Kuks
#Quaas
#Moans
#Tail flags
#Tail twitches
#Approaches
#Indifferent
#Runs from

# Create your models here.
