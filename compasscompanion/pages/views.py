from django.shortcuts import render

from .forms import StartPointCreate

# Create your views here.
def map_view(request):
    context = {
        
    }

    return render(request, 'map.html', context)

def home_view(request):
    context = {

    }

    return render(request, 'front_page.html', context)

def home_form_view(request):
    form = StartPointCreate(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, 'front_page.html', context)