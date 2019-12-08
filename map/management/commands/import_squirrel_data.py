from django.core.management.base import BaseCommand, CommandError
import requests

class Command(BaseCommand):
    help = 'Imports squirrel data from NYC open Data website'

    def add_arguments(self, parser):
        parser.add_argument('path',  nargs='+', type=str)

    def handle(self,*args,**filepath):

        response = requests.get('https://data.cityofnewyork.us/resource/vfnx-vebw.csv').content.decode('latin1')
        path = filepath['path']
        with open('/home/ok2294/squirrel/file.csv','w') as f:
            f.truncate()
            f.write(response)
            f.close()



        
