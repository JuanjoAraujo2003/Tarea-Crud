from django.shortcuts import render, redirect
from .serializer import FactionSerializer
from .models import Factions
from rest_framework import viewsets
from .forms import CreateNewFaction

class FactionView(viewsets.ModelViewSet):
    queryset = Factions.objects.all()
    serializer_class = FactionSerializer

def index(request):
    form = CreateNewFaction()
    if request.method == 'POST':
        if "save" in request.POST:
            form = CreateNewFaction(request.POST)
            form.save()
    factions = Factions.objects.all()
    return render(request, 'index.html', {'form': form, 'factions': factions})