from rest_framework import serializers
from .models import PretAnimInt

class PretAnimIntSerializer(serializers.ModelSerializer):
    class Meta:
        model = PretAnimInt
        fields = ['id', 'date_debut_livre', 'date_fin_livre', 'user', 'livre']
