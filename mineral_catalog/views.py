from django.shortcuts import redirect, render

from .models import Mineral


def redirect_home(request):
    return redirect('catalog:list')


def list_minerals(request, letter=None):
    if letter:
        minerals = Mineral.objects.filter(name__istartswith=letter)
    else:
        minerals = Mineral.objects.all()

    return render(request, 'mineral_catalog/list.html', {'minerals': minerals})


def detail_mineral(request, mineral_slug):
    mineral = Mineral.objects.get(slug=mineral_slug)
    fields = ('category', 'formula', 'strunz_classification', 'crystal_system',
              'unit_cell', 'color', 'crystal_symmetry', 'cleavage',
              'mohs_scale_hardness', 'luster', 'streak', 'diaphaneity', 'optical_properties',
              'refractive_index', 'crystal_habit', 'specific_gravity', 'group')

    return render(request, 'mineral_catalog/detail.html', {'mineral': mineral, 'fields': fields})
