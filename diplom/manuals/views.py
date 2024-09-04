from django.shortcuts import render, redirect
from .models import Manuals, UsersSite

def home(request):
    title = "Каталог инструкций"
    manuals = Manuals.objects.all()
    context = {'manuals': manuals,'title':title}

    return render(request, 'manuals/index.html', context)

def authors(request):
    title = "Наши авторы"
    authors = UsersSite.objects.all()
    manuals = Manuals.objects.all()
    context = {'authors':authors, 'manuals':manuals,'title':title}
    return render(request, 'manuals/authors.html', context)

def manual(request,pk):
    manual = Manuals.objects.get(id=pk)
    context = {'manual':manual}
    return render(request, 'manuals/manual.html',context)
