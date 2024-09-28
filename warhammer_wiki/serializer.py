from rest_framework import serializers
from .models import Factions

class FactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factions
        fields = '__all__'
    