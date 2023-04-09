from django.shortcuts import render
from django.http import HttpResponseRedirect


from .forms import CoordForm
from django.views.generic import TemplateView

#from .calculations import reason_list

# Create your views here.

class HomeView(TemplateView):
    template_name = 'front_page.html'


def get_coords(request):
    form = CoordForm(request.POST or None)

    freader = open('output.txt', 'r')
    data = freader.read()


    if form.is_valid():
        form.save()
        form = CoordForm()

    else:
        form = CoordForm()

    context = {
        'form': form,
        'data': data
    }
    return render(request, 'front_page.html', context)