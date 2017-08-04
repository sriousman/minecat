from django.shortcuts import render

from minerals import models


def home(request):
    minerals = models.Mineral.objects.all()

    return render(request, 'minerals/index.html', {'minerals': minerals})


