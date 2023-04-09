from django.shortcuts import render

# Create your views here.
def map_view(request):
    context = {
        
    }

    return render(request, 'map.html', context)

def home_view(request):
    context = {

    }

    return render(request, 'front_page.html', context)