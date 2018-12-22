from django.shortcuts import render

from .models import Mineral


def list_minerals(request, letter=None):
    if letter:
        minerals = Mineral.objects.filter(name__istartswith=letter)
    else:
        minerals = Mineral.objects.all()

    return render(request, 'mineral_catalog/list.html', {'minerals': minerals})
