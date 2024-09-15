from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    all_destinations=models.Destination.objects.all()
    context={
        'destinations': all_destinations,
    }
    return render(request, 'destinations.html', context)

class DestinationDetailView(generic.DetailView):
    template_name='destination_detail.html'
    model=models.Destination
    context_object_name='destination'

class DestinationUpdateView(generic.UpdateView):
    template_name='destination_form.html'
    model=models.Destination
    fields=['name','description']

class DestinationCreateView(generic.CreateView):
    template_name='destination_form.html'
    model=models.Destination
    fields=['name','description']

class DestinationDeleteView(generic.DeleteView):
    template_name='destination_confirm_delete.html'
    model=models.Destination
    success_url=reverse_lazy('destinations')


class CruiseDetailView(generic.DetailView):
    template_name='cruise_detail.html'
    model=models.Cruise
    context_object_name='cruise'


