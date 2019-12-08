from django import forms
from django.forms import ModelForm
from sightings.models import Sightings

# Create the form class.
class Sightingsform(ModelForm):
    class Meta:
        model = Sightings
        fields = '__all__'

# Creating a form to add an article.
form = Sightingsform()

# Creating a form to change an existing article.
formobj = Sightings.objects.get(pk=1)
form = Sightingsform(instance=formobj)
