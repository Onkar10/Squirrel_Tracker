from django.shortcuts import render
from django.http import HttpResponse
from sightings.models import Sightings
from django.template import loader
def index(request):
    sightings = Sightings.objects.all()
    template = loader.get_template('map/map.html')
    context = {'sightings':sightings}
    return HttpResponse(template.render(context, request))
