from django.shortcuts import render
from .models import Sightings
from django.http import HttpResponse
from django.template import loader
from .forms import Sightingsform

def index(request):
    Unique_Squirrel_list = Sightings.objects.all()
    template = loader.get_template('sightings/index.html')
    context = {'Unique_Squirrel_list': Unique_Squirrel_list, 
            }
    return HttpResponse(template.render(context, request))


from django.http import HttpResponseRedirect
from .forms import Sightingsform

def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Sightingsform(request.POST)
        # check whether it's valid:
        if form.is_valid():

            form.save(commit=True)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/sightings/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Sightingsform()

    return render(request, 'yourname.html', {'form': form})


def edit(request, Unique_Squirrel_ID):
    squirrel = Sightings.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = Sightingsform(request.POST, instance=squirrel)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/sightings/')
    else:
        form = Sightingsform(instance=squirrel)

    return render(request, 'sightings/edit.html/', {'form': form})

def stats(request):
    pass




# Create your views here.
