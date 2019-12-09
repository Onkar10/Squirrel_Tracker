from django.shortcuts import render
from .models import Sightings
from django.http import HttpResponse
from django.template import loader
from .forms import Sightingsform
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter 
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image 
from io import BytesIO


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
    s = Sightings.objects.all().values()
    df=pd.DataFrame(s)
    df2=pd.read_csv('file.csv')
    df2.groupby('primary_fur_color').count()['x']
    explode=(0,0,0)
    labels='Black','Cinnamon','Gray'
    s=df2.groupby('primary_fur_color').count()['x'].sum()
    x1=(df2.groupby('primary_fur_color').count()['x'][0])/s*100
    x2=(df2.groupby('primary_fur_color').count()['x'][1])/s*100
    x3=(df2.groupby('primary_fur_color').count()['x'][2])/s*100
    sizes=[x1,x2,x3]
    lst=[df2.groupby('shift').count()['x'][f] for f in range(2)]
    x=['AM','PM']

    fig, (ax1, ax2) = plt.subplots(2)
    ax1.pie(sizes, explode=explode, labels=labels)
    ax2.bar(x, height=lst)
    ax2.title.set_text('Variations in shift sightings')
    ax2.set_xlabel('Shift')
    ax2.set_ylabel('Frequency of Sightings')

    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer,"PNG")
    pylab.close()

    return HttpResponse(buffer.getvalue(), content_type= "image/png")

    pass




# Create your views here.
