from rest_framework import serializers
from .models import Projetos

class ProjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = ['title', 'description', 'linkProject', 'linkRepo', 'image']
