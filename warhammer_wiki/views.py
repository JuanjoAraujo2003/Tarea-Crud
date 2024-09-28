from django.shortcuts import render
from .serializer import FactionSerializer
from .models import Factions
from rest_framework import viewsets
# Create your views here.

class FactionView(viewsets.ModelViewSet):
    queryset = Factions.objects.all()
    serializer_class = FactionSerializer
    
def index(request):
    forms = Factions.objects.all()
    return render(request, 'index.html', {'forms': forms})