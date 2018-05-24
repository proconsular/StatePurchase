from django.shortcuts import render
from .source.primary.Map import Map

# Create your views here.
def index(request):
    map = Map()
    context = {
        'map': map.render()
    }
    return render(request, 'game/index.html', context)


# IGNORE THIS ------ JED