"""mineral_catalog views"""
from django.db.models import Q
from django.shortcuts import redirect, render

from .models import Mineral


def redirect_to_list(request):
    """Permanently redirect to the home list page"""
    return redirect('catalog:list', letter='a', permanent=True)


def list_minerals_by_letter(request, letter='a'):
    """List minerals starting with the provided letter (A if none)"""
    minerals = Mineral.objects.filter(name__istartswith=letter)

    return render(request, 'mineral_catalog/list.html', {'minerals': minerals})


def list_minerals_by_group(request, group):
    """List minerals by which group they belong to"""
    group = group.replace('_', ' ')
    minerals = Mineral.objects.filter(group__iexact=group)

    return render(request, 'mineral_catalog/list.html', {'minerals': minerals})


def detail_mineral(request, mineral_slug):
    """Show all the attributes of a particular mineral"""
    mineral = Mineral.objects.get(slug=mineral_slug)
    fields = (
        'category',
        'formula',
        'strunz_classification',
        'crystal_system',
        'unit_cell',
        'color',
        'crystal_symmetry',
        'cleavage',
        'mohs_scale_hardness',
        'luster',
        'streak',
        'diaphaneity',
        'optical_properties',
        'refractive_index',
        'crystal_habit',
        'specific_gravity',
        'group',
    )

    return render(request, 'mineral_catalog/detail.html', {'mineral': mineral, 'fields': fields})


def search(request):
    """Show all the minerals whose name contains the search query"""
    query = request.GET['query']
    minerals = Mineral.objects.filter(
        Q(name__istartswith=query)
        | Q(slug__istartswith=query)
        | Q(image_filename__istartswith=query)
        | Q(image_caption__istartswith=query)
        | Q(category__istartswith=query)
        | Q(formula__istartswith=query)
        | Q(strunz_classification__istartswith=query)
        | Q(crystal_system__istartswith=query)
        | Q(unit_cell__istartswith=query)
        | Q(color__istartswith=query)
        | Q(crystal_symmetry__istartswith=query)
        | Q(cleavage__istartswith=query)
        | Q(mohs_scale_hardness__istartswith=query)
        | Q(luster__istartswith=query)
        | Q(streak__istartswith=query)
        | Q(diaphaneity__istartswith=query)
        | Q(optical_properties__istartswith=query)
        | Q(refractive_index__istartswith=query)
        | Q(crystal_habit__istartswith=query)
        | Q(specific_gravity__istartswith=query)
        | Q(group__istartswith=query)
    )

    return render(request, 'mineral_catalog/list.html', {'minerals': minerals})


def search_by_color(request):
    """Show all minerals that match a query minerals' color field"""
    query = request.GET['query']
    minerals = Mineral.objects.filter(color__search=query)

    return render(request, 'mineral_catalog/list.html', {'minerals': minerals})
