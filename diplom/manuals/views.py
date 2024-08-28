from django.shortcuts import render, redirect
from .models import Manuals
def home(request):
    manuals = Manuals.objects.all()
    context = {'manuals': manuals}

    return render(request, 'manuals/index.html', context)

