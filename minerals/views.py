from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count, Sum

from .models import Mineral


def list_minerals(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})


def detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/detail.html', {'mineral': mineral})


def minerals_by_first_letter(request, alpha):
    minerals = Mineral.objects.filter(name__startswith=alpha.lower())
    return render(request, 'minerals/index.html', {'minerals': minerals, 'current': alpha})


def minerals_by_group(request, group):
    g = group.lower()
    minerals = Mineral.objects.filter(group__icontains=g)
    return render(request, 'minerals/index.html', {'minerals': minerals, 'current': g})


def search(request):
    term = request.GET['q']
    minerals = Mineral.objects.filter(Q(name__icontains=term)|Q(image_caption__icontains=term))
    return render(request, 'minerals/index.html', {'minerals': minerals})