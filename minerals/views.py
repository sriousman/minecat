from django.shortcuts import render, get_object_or_404

from .models import Mineral

def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals':minerals})


def detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/detail.html', {'mineral':mineral})
