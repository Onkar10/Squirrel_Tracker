from django.core.management.base import BaseCommand
import pandas as pd
import csv
from sightings.models import Sightings
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', nargs = '+', type = str)
    def handle(self, *args, **kwargs):
        with open(kwargs['path'][0]) as file:
            reader = csv.DictReader(file)
            data = list(reader)
        for item in data:
            s = Sightings(
            x = item['x'],
            y = item['y'],
            Unique_Squirrel_ID = item['unique_squirrel_id'],
            Shift = item['shift'],
            Date = item['date'],
            Age = item['age'],
            Primary_Fur_Color = item['primary_fur_color'],
            Location = item['location'],
            Specific_Location = item['specific_location'],
            Running = item['running'],
            Climbing = item['climbing'],
            Eating = item['eating'],
            Foraging = item['foraging'],
            Other_Activities = item['other_activities'],
            Kuks = item['kuks'],
            Quaas = item['quaas'],
            Moans = item['moans'],
            Tail_flags = item['tail_flags'],
            Tail_twitches = item['tail_twitches'],
            Approaches = item['approaches'],
            Indifferent = item['indifferent'],
            Runs_from = item['runs_from'],
            )
            s.save()  
