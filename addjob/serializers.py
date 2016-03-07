from rest_framework import serializers
from .models import Branza


class BranzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branza
        fields = ('pk', 'name',)
