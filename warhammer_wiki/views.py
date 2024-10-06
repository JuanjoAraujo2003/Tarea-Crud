from django.shortcuts import render, redirect
from .serializer import FactionSerializer
from .models import Factions
from rest_framework import viewsets
from .forms import CreateNewFaction
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class FactionView(viewsets.ModelViewSet):
    queryset = Factions.objects.all()
    serializer_class = FactionSerializer
@login_required
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = CreateNewFaction(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('index'))
                
        else:
            form = CreateNewFaction()
                    
        factions = Factions.objects.all()
        return render(request, 'index.html', {'form': form, 'factions': factions})
    
@login_required
def delete_faction(request, id):
    faction = get_object_or_404(Factions, id=id)
    if request.method == 'POST':
        faction.delete()
        return redirect('index')
    
@login_required   
def update_faction(request, id):
    faction = get_object_or_404(Factions, id=id)
    if request.method == 'POST':
        form = CreateNewFaction(request.POST, instance=faction)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateNewFaction(instance=faction)
    return render(request, 'update.html', {'form': form})